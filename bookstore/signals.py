from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import *
from django.db import transaction
import logging

logger = logging.getLogger(__name__)
# Helper function to get or create a report for a specific month and year
def get_or_create_report(model, month, year):
    try:
        if model == CT_BCTon:
            report = BaoCaoTon.objects.filter(Thang=month, Nam=year).first()
            if not report:
                report = BaoCaoTon.objects.create(Thang=month, Nam=year)
        elif model == CT_BCCongNo:
            report = BaoCaoCongNo.objects.filter(Thang=month, Nam=year).first()
            if not report:
                report = BaoCaoCongNo.objects.create(Thang=month, Nam=year)
        else:
            logger.error(f"Unsupported model passed to get_or_create_report: {model}")
            raise ValueError("Unsupported model for report creation.")
        return report
    except Exception as e:
        logger.error(f"Error creating or retrieving report for {month}/{year}: {e}")
        raise ValueError(f"Error creating or retrieving report for {month}/{year}: {e}")
# Signal for HoaDon

@receiver(pre_save, sender=CT_HoaDon)
def validate_ct_hoadon(sender, instance, **kwargs):
    # Get ThamSo constraints
    thamso = ThamSo.objects.get(id=1)
    if instance.SLBan <= 0:
        raise ValueError("Số lượng bán phải là số dương.")
    # Check KhachHang.SoTienNo ≤ NoTD
    hoadon = instance.MaHD
    khachhang = hoadon.MaKH
    if khachhang.SoTienNo > thamso.NoTD:
        raise ValueError(f"Khách hàng có nợ vượt quá {thamso.NoTD}")

    # Check Sach.SLTon - SLBan ≥ TonTT
    sach = instance.MaSach
    if (sach.SLTon - instance.SLBan) < thamso.TonTT:
        raise ValueError(f"Tồn kho sau bán phải ≥ {thamso.TonTT}")

    # Check GiaBan = GiaNhap * (TiLe / 100)
    last_nhap = CT_NhapSach.objects.filter(MaSach=sach).order_by('-MaPhieuNhap').first()
    if last_nhap:
        expected_giaban = last_nhap.GiaNhap * (thamso.TiLe / 100)
        if instance.GiaBan != expected_giaban:
            raise ValueError(f"Giá bán phải = giá nhập x {thamso.TiLe}%")

@receiver(post_save, sender=HoaDon)
def handle_hoadon_insert(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            # Get the report
            report = get_or_create_report(CT_BCCongNo, instance.NgayLap.month, instance.NgayLap.year)
            
            # Get or create CT_BCCongNo for this customer in this month
            ct_bccongno, is_new = CT_BCCongNo.objects.get_or_create(
                MaBCCN=report,
                MaKH=instance.MaKH,
                defaults={
                    'NoDau': instance.MaKH.SoTienNo - (instance.TongTien - instance.SoTienTra),  # Initial debt before this invoice
                    'PhatSinh': instance.TongTien - instance.SoTienTra,  # This invoice's remaining debt
                    'NoCuoi': instance.MaKH.SoTienNo  # Current total debt
                }
            )
            
            # If report already exists, update the values
            if not is_new:
                ct_bccongno.PhatSinh += instance.TongTien - instance.SoTienTra
            
            # Calculate total payments for this month
            total_sotienthu = PhieuThuTien.objects.filter(
                MaKH=instance.MaKH,
                NgayThu__month=instance.NgayLap.month,
                NgayThu__year=instance.NgayLap.year
            ).aggregate(total=models.Sum('SoTienThu'))['total'] or 0
            
            # Update NoCuoi
            ct_bccongno.NoCuoi = ct_bccongno.NoDau + ct_bccongno.PhatSinh - total_sotienthu
            ct_bccongno.save()

# Signal for CT_HoaDon
@receiver(post_save, sender=CT_HoaDon)
def handle_ct_hoadon_insert(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            # Update stock first
            instance.MaSach.SLTon -= instance.SLBan
            instance.MaSach.save()

            report = get_or_create_report(CT_BCTon, instance.MaHD.NgayLap.month, instance.MaHD.NgayLap.year)
            ct_bcton, created = CT_BCTon.objects.get_or_create(
                MaBCTon=report,
                MaSach=instance.MaSach,
                defaults={'TonDau': instance.MaSach.SLTon, 'PhatSinh': 0, 'TonCuoi': 0}
            )
            total_banra = CT_HoaDon.objects.filter(
                MaSach=instance.MaSach,
                MaHD__NgayLap__month=instance.MaHD.NgayLap.month,
                MaHD__NgayLap__year=instance.MaHD.NgayLap.year
            ).aggregate(total=models.Sum('SLBan'))['total'] or 0
            ct_bcton.TonCuoi = ct_bcton.TonDau + ct_bcton.PhatSinh - total_banra
            print(
                "DEBUG:",
                "TonDau:", ct_bcton.TonDau,
                "PhatSinh:", ct_bcton.PhatSinh,
                "total_banra:", total_banra,
                "SLTon:", instance.MaSach.SLTon,
                "SLBan:", instance.SLBan
            )
            ct_bcton.save()
@receiver(post_delete, sender=CT_HoaDon)
def handle_ct_hoadon_delete(sender, instance, **kwargs):
    with transaction.atomic():
         # Restore Sach.SLTon first
        instance.MaSach.SLTon += instance.SLBan
        instance.MaSach.save()
        report = get_or_create_report(CT_BCTon, instance.MaHD.NgayLap.month, instance.MaHD.NgayLap.year)
        ct_bcton = CT_BCTon.objects.get(MaBCTon=report, MaSach=instance.MaSach)
        # Recalculate BanRa and update TonCuoi
        total_banra = CT_HoaDon.objects.filter(
            MaSach=instance.MaSach,
            MaHD__NgayLap__month=instance.MaHD.NgayLap.month,
            MaHD__NgayLap__year=instance.MaHD.NgayLap.year
        ).aggregate(total=models.Sum('SLBan'))['total'] or 0
        ct_bcton.TonCuoi = ct_bcton.TonDau + ct_bcton.PhatSinh - total_banra
        ct_bcton.save()
# Signal for PhieuThuTien
@receiver(pre_save, sender=PhieuThuTien)
def validate_phieuthutien(sender, instance, **kwargs):
    # Get ThamSo constraints
    thamso = ThamSo.objects.get(id=1)

    # Check SoTienThu ≤ KhachHang.SoTienNo if SDQD4 is True
    if thamso.SDQD4:
        khachhang = instance.MaKH
        if instance.SoTienThu > khachhang.SoTienNo:
            raise ValueError("Số tiền thu không được vượt quá số tiền khách đang nợ")
@receiver(post_save, sender=PhieuThuTien)
def handle_phieuthutien_insert(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            # Ensure BaoCaoCongNo exists
            report = get_or_create_report(CT_BCCongNo, instance.NgayThu.month, instance.NgayThu.year)
            ct_bccongno, created = CT_BCCongNo.objects.get_or_create(
                MaBCCN=report,
                MaKH=instance.MaKH,
                defaults={'NoDau': instance.MaKH.SoTienNo, 'PhatSinh': 0, 'NoCuoi': 0}
            )
            # Recalculate NoCuoi
            total_sotienthu = PhieuThuTien.objects.filter(
                MaKH=instance.MaKH,
                NgayThu__month=instance.NgayThu.month,
                NgayThu__year=instance.NgayThu.year
            ).aggregate(total=models.Sum('SoTienThu'))['total'] or 0
            ct_bccongno.NoCuoi = ct_bccongno.NoDau + ct_bccongno.PhatSinh - total_sotienthu
            ct_bccongno.save()
@receiver(post_delete, sender=PhieuThuTien)
def handle_phieuthutien_delete(sender, instance, **kwargs):
    with transaction.atomic():
        report = get_or_create_report(CT_BCCongNo, instance.NgayThu.month, instance.NgayThu.year)
        ct_bccongno = CT_BCCongNo.objects.get(MaBCCN=report, MaKH=instance.MaKH)
        # Recalculate NoCuoi
        total_sotienthu = PhieuThuTien.objects.filter(
            MaKH=instance.MaKH,
            NgayThu__month=instance.NgayThu.month,
            NgayThu__year=instance.NgayThu.year
        ).aggregate(total=models.Sum('SoTienThu'))['total'] or 0
        ct_bccongno.NoCuoi = ct_bccongno.NoDau + ct_bccongno.PhatSinh - total_sotienthu
        ct_bccongno.save()
    
# Signal for CT_NhapSach
@receiver(pre_save, sender=CT_NhapSach)
def validate_ct_nhapsach(sender, instance, **kwargs):
    # Get ThamSo constraints
    if instance.SLNhap <= 0:
        raise ValueError("Số lượng nhập phải là số dương.")
    thamso = ThamSo.objects.get(id=1)

    # Check SLNhap >= SLNhapTT
    if instance.SLNhap < thamso.SLNhapTT:
        raise ValueError(f"Số lượng nhập phải ≥ {thamso.SLNhapTT}")

    # Check SLTon < TonTD
    sach = Sach.objects.get(pk=instance.MaSach.pk)
    if sach.SLTon >= thamso.TonTD:
        raise ValueError(f"Không thể nhập vì tồn kho hiện tại ≥ {thamso.TonTD}")
@receiver(post_save, sender=CT_NhapSach)
def handle_ct_nhapsach_insert(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            # Get the report
            report = get_or_create_report(CT_BCTon, instance.MaPhieuNhap.NgayNhap.month, instance.MaPhieuNhap.NgayNhap.year)
            
            # Get or create CT_BCTon for this book in this month
            ct_bcton, is_new = CT_BCTon.objects.get_or_create(
                MaBCTon=report,
                MaSach=instance.MaSach,
                defaults={
                    'TonDau': instance.MaSach.SLTon - instance.SLNhap,  # Initial stock before this import
                    'PhatSinh': instance.SLNhap,  # This import's quantity
                    'TonCuoi': instance.MaSach.SLTon  # Current stock after import
                }
            )
            
            # If report already exists, update the values
            if not is_new:
                ct_bcton.PhatSinh += instance.SLNhap
            
            # Calculate total sales for this month
            total_banra = CT_HoaDon.objects.filter(
                MaSach=instance.MaSach,
                MaHD__NgayLap__month=instance.MaPhieuNhap.NgayNhap.month,
                MaHD__NgayLap__year=instance.MaPhieuNhap.NgayNhap.year
            ).aggregate(total=models.Sum('SLBan'))['total'] or 0
            
            # Update TonCuoi
            ct_bcton.TonCuoi = ct_bcton.TonDau + ct_bcton.PhatSinh - total_banra
            ct_bcton.save()
@receiver(post_delete, sender=CT_NhapSach)
def handle_ct_nhapsach_delete(sender, instance, **kwargs):
    with transaction.atomic():
        report = get_or_create_report(CT_BCTon, instance.MaPhieuNhap.NgayNhap.month, instance.MaPhieuNhap.NgayNhap.year)
        ct_bcton = CT_BCTon.objects.get(MaBCTon=report, MaSach=instance.MaSach)
        # Update PhatSinh and recalculate TonCuoi
        ct_bcton.PhatSinh -= instance.SLNhap
        total_banra = CT_HoaDon.objects.filter(
            MaSach=instance.MaSach,
            MaHD__NgayLap__month=instance.MaPhieuNhap.NgayNhap.month,
            MaHD__NgayLap__year=instance.MaPhieuNhap.NgayNhap.year
        ).aggregate(total=models.Sum('SLBan'))['total'] or 0
        ct_bcton.TonCuoi = ct_bcton.TonDau + ct_bcton.PhatSinh - total_banra
        ct_bcton.save()
@receiver(pre_save, sender=HoaDon)
def handle_hoadon_update(sender, instance, **kwargs):
    if instance.pk:  # Ensure this is an update
        old_instance = HoaDon.objects.get(pk=instance.pk)
        if old_instance.SoTienTra != instance.SoTienTra:
            delta = instance.SoTienTra - old_instance.SoTienTra
            instance.ConLai = instance.TongTien - instance.SoTienTra
            instance.MaKH.SoTienNo -= delta
            instance.MaKH.save()
            
@receiver(post_delete, sender=HoaDon)
def handle_hoadon_delete(sender, instance, **kwargs):
    instance.MaKH.SoTienNo -= instance.ConLai
    instance.MaKH.save()
    

@receiver(pre_save, sender=CT_HoaDon)
def handle_ct_hoadon_update(sender, instance, **kwargs):
    if instance.pk:  # Ensure this is an update
        try:
            old_instance = CT_HoaDon.objects.get(pk=instance.pk)
        except CT_HoaDon.DoesNotExist:
            logger.warning(f"CT_HoaDon with ID {instance.pk} does not exist. Skipping update.")
            return

        if old_instance.SLBan != instance.SLBan:
            delta = instance.SLBan - old_instance.SLBan
            instance.MaSach.SLTon -= delta
            instance.MaSach.save()

            report = get_or_create_report(CT_BCTon, instance.MaHD.NgayLap.month, instance.MaHD.NgayLap.year)
            report.PhatSinh += delta
            report.TonCuoi = report.TonDau + report.PhatSinh
            report.save()

# def rollover_report(model, month, year):
#     try:
#         current_report = model.objects.get(MaBCTon__Thang=month, MaBCTon__Nam=year) if model == CT_BCTon else model.objects.get(MaBCCN__Thang=month, MaBCCN__Nam=year)
#         next_month = (month % 12) + 1
#         next_year = year + (1 if next_month == 1 else 0)
#         next_report, created = model.objects.get_or_create(
#             MaBCTon__Thang=next_month, MaBCTon__Nam=next_year
#         ) if model == CT_BCTon else model.objects.get_or_create(
#             MaBCCN__Thang=next_month, MaBCCN__Nam=next_year
#         )
#         next_report.TonDau = current_report.TonCuoi if model == CT_BCTon else next_report.NoDau
#         next_report.save()
#     except Exception as e:
#         raise ValueError(f"Error rolling over report for {month}/{year}: {e}")
# @receiver(post_save, sender=CT_BCTon)
# def handle_ct_bcton_save(sender, instance, created, **kwargs):
#     if created:
#         # Get the parent BaoCaoTon object
#         baocao_ton = instance.MaBCTon
#         # Rollover TonCuoi to the next month
#         rollover_report(CT_BCTon, baocao_ton.Thang, baocao_ton.Nam)

# @receiver(post_save, sender=CT_BCCongNo)
# def handle_ct_bccongno_save(sender, instance, created, **kwargs):
#     if created:
#         # Get the parent BaoCaoCongNo object
#         baocao_congno = instance.MaBCCN
#         # Rollover NoCuoi to the next month
#         rollover_report(CT_BCCongNo, baocao_congno.Thang, baocao_congno.Nam)
# @receiver(pre_save, sender=ThamSo)
# def ensure_single_thamso(sender, instance, **kwargs):
#     if ThamSo.objects.exists() and not instance.pk:
#         # Delete the old object before saving the new one
#         ThamSo.objects.all().delete()
def rollover_report(model, month, year, recursion_limit=12):
    """
    Roll over reports with a recursion limit to prevent infinite loops
    """
    if recursion_limit <= 0:
        return

    try:
        # Get current report based on model type
        if model == CT_BCTon:
            current_baocao = BaoCaoTon.objects.get(Thang=month, Nam=year)
            next_month = (month % 12) + 1
            next_year = year + (1 if next_month == 1 else 0)
            
            next_baocao, created = BaoCaoTon.objects.get_or_create(
                Thang=next_month,
                Nam=next_year
            )
            
            for ct_bcton in CT_BCTon.objects.filter(MaBCTon=current_baocao):
                CT_BCTon.objects.get_or_create(
                    MaBCTon=next_baocao,
                    MaSach=ct_bcton.MaSach,
                    defaults={
                        'TonDau': ct_bcton.TonCuoi,
                        'PhatSinh': 0,
                        'TonCuoi': ct_bcton.TonCuoi
                    }
                )

        elif model == CT_BCCongNo:
            current_baocao = BaoCaoCongNo.objects.get(Thang=month, Nam=year)
            next_month = (month % 12) + 1
            next_year = year + (1 if next_month == 1 else 0)
            
            next_baocao, created = BaoCaoCongNo.objects.get_or_create(
                Thang=next_month,
                Nam=next_year
            )
            
            for ct_bccongno in CT_BCCongNo.objects.filter(MaBCCN=current_baocao):
                CT_BCCongNo.objects.get_or_create(
                    MaBCCN=next_baocao,
                    MaKH=ct_bccongno.MaKH,
                    defaults={
                        'NoDau': ct_bccongno.NoCuoi,
                        'PhatSinh': 0,
                        'NoCuoi': ct_bccongno.NoCuoi
                    }
                )

        
    except Exception as e:
        logger.error(f"Error in rollover_report for {month}/{year}: {e}")

@receiver(post_save, sender=CT_BCTon)
def handle_ct_bcton_save(sender, instance, created, **kwargs):
    if created:
        # Get the parent BaoCaoTon object
        baocao_ton = instance.MaBCTon
        # Rollover TonCuoi to the next month with recursion limit
        transaction.on_commit(lambda: rollover_report(CT_BCTon, baocao_ton.Thang, baocao_ton.Nam))

@receiver(post_save, sender=CT_BCCongNo)
def handle_ct_bccongno_save(sender, instance, created, **kwargs):
    if created:
        # Get the parent BaoCaoCongNo object
        baocao_congno = instance.MaBCCN
        # Rollover NoCuoi to the next month with recursion limit
        transaction.on_commit(lambda: rollover_report(CT_BCCongNo, baocao_congno.Thang, baocao_congno.Nam))