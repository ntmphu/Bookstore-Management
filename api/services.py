from datetime import date, timedelta
from django.db.models import Sum
from api.models import BaoCaoTon, CT_BCTon, Sach, CT_NhapSach, HoaDon, CT_HoaDon, BaoCaoCongNo, CT_BCCongNo, KhachHang, PhieuThuTien

def first_day_of_month(dt: date) -> date:
    return dt.replace(day=1)

def prev_month_date(dt: date) -> date:
    first = first_day_of_month(dt)
    return (first - timedelta(days=1)).replace(day=1)

def generate_baocaoton_for_month(target_month: date = None):
    if not target_month:
        target_month = first_day_of_month(date.today())

    # Get previous month for TonDau lookup
    prev_month = prev_month_date(target_month)
    # Create or get BaoCaoTon for the month
    baocao, created = BaoCaoTon.objects.get_or_create(Thang=target_month)

    # For each Sach, compute TonDau, PhatSinh, TonCuoi
    for sach in Sach.objects.all():
        # TonDau = TonCuoi of prev month or current stock if no prev month report
        prev_ct = CT_BCTon.objects.filter(MaBCTon__Thang=prev_month, MaSach=sach).first()
        print(sach.MaSach)
        ton_dau = prev_ct.TonCuoi if prev_ct else sach.SLTon

        # PhatSinh = total imported this month
        phat_sinh = CT_NhapSach.objects.filter(
            MaPhieuNhap__NgayNhap__year=target_month.year,
            MaPhieuNhap__NgayNhap__month=target_month.month,
            MaSach=sach
        ).aggregate(total=Sum('SLNhap'))['total'] or 0

        # SoLuongBan = total sold this month
        so_luong_ban = CT_HoaDon.objects.filter(
            MaHD__NgayLap__year=target_month.year,
            MaHD__NgayLap__month=target_month.month,
            MaSach=sach
        ).aggregate(total=Sum('SLBan'))['total'] or 0
        print(ton_dau, phat_sinh, so_luong_ban)
        ton_cuoi = ton_dau + phat_sinh - so_luong_ban
        
        # Create or update CT_BCTon for sach
        ct_bcton, _ = CT_BCTon.objects.update_or_create(
            MaBCTon=baocao,
            MaSach=sach,
            defaults={
                'TonDau': ton_dau,
                'PhatSinh': phat_sinh,
                'TonCuoi': ton_cuoi,
            }
        )

    return baocao

def generate_baocaocongno_for_month(target_month: date = None):
    if not target_month:
        target_month = first_day_of_month(date.today())

    # Get previous month for NoDau lookup
    prev_month = prev_month_date(target_month)

    # Create or get BaoCaoCongNo for the month
    baocao, created = BaoCaoCongNo.objects.get_or_create(Thang=target_month)

    # For each KhachHang, compute NoDau, PhatSinh, NoCuoi
    for khachhang in KhachHang.objects.all():
        # NoDau = NoCuoi of prev month or current debt if no prev month report
        prev_ct = CT_BCCongNo.objects.filter(MaBCCN__Thang=prev_month, MaKH=khachhang).first()
        no_dau = prev_ct.NoCuoi if prev_ct else khachhang.SoTienNo

        # PhatSinh = total remain of invoices this month
        phat_sinh = HoaDon.objects.filter(
            NgayLap__year=target_month.year,
            NgayLap__month=target_month.month,
            MaKH=khachhang
        ).aggregate(total=Sum('ConLai'))['total'] or 0

        # TienTra = total money returned this month
        TienTra = PhieuThuTien.objects.filter(
            NgayThu__year=target_month.year,
            NgayThu__month=target_month.month,
            MaKH=khachhang
        ).aggregate(total=Sum('SoTienThu'))['total'] or 0

        no_cuoi = no_dau + phat_sinh - TienTra

        # Create or update CT_BCCongNo for sach
        ct_bccn, _ = CT_BCCongNo.objects.update_or_create(
            MaBCCN=baocao,
            MaKH=khachhang,
            defaults={
                'NoDau': no_dau,
                'PhatSinh': phat_sinh,
                'NoCuoi': no_cuoi,
            }
        )

    return baocao