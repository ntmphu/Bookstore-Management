from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group as NhomNguoiDung
from django.contrib.auth.models import Permission as ChucNang
from django.conf import settings

# Add this after the imports
from django.db.models.signals import post_save
from django.dispatch import receiver

# Add this with your other models
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gioiTinh = models.CharField(max_length=3, choices=GENDER_CHOICES, default='Nam')

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class TheLoai(models.Model):
    MaTheLoai = models.AutoField(primary_key=True)
    TenTheLoai = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.TenTheLoai

class TacGia(models.Model):
    MaTG = models.AutoField(primary_key=True)
    TenTG = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.TenTG

class DauSach(models.Model):
    MaDauSach = models.AutoField(primary_key=True)
    TenSach = models.CharField(max_length=200, unique=True)
    MaTheLoai = models.ForeignKey(TheLoai, blank=True, null=True, on_delete=models.SET_NULL, related_name='DauSach')
    MaTG = models.ManyToManyField(TacGia, blank=True, related_name='DauSach')

    def __str__(self):
        return self.TenSach

class Sach(models.Model):
    MaSach = models.AutoField(primary_key=True)
    MaDauSach = models.ForeignKey(DauSach, on_delete=models.CASCADE, related_name='sach')
    NXB = models.CharField(max_length=200)
    NamXB = models.IntegerField()
    SLTon = models.PositiveIntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.MaDauSach.TenSach
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MaDauSach', 'NXB', 'NamXB'], name='unique_sach')
        ]

class KhachHang(models.Model):
    MaKhachHang = models.AutoField(primary_key=True)
    HoTen = models.CharField(max_length=200)
    DiaChi = models.CharField(max_length=200)
    DienThoai = models.CharField(max_length=200, unique=True)
    Email = models.EmailField(max_length=200)
    SoTienNo = models.DecimalField(max_digits=15,  decimal_places=0, default=0, editable=False, null=True)

    def __str__(self):
        return self.HoTen

class PhieuNhapSach(models.Model):
    MaPhieuNhap = models.AutoField(primary_key=True)
    NgayNhap = models.DateField()
    NguoiNhap = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='NguoiNhap',
        verbose_name='Người nhập'
    )
    MaSach = models.ManyToManyField(Sach, through='CT_NhapSach', related_name='PhieuNhapSach')

    def __str__(self):
        return f"Phiếu nhập #{self.MaPhieuNhap} - {self.NgayNhap}"

class CT_NhapSach(models.Model):
    # MaCT_NhapSach = models.AutoField(primary_key=True)
    MaPhieuNhap = models.ForeignKey(
        PhieuNhapSach,
        on_delete=models.CASCADE,
        related_name='ct_nhap'
    )
    MaSach = models.ForeignKey(Sach, on_delete=models.RESTRICT)
    SLNhap = models.PositiveIntegerField()
    GiaNhap = models.DecimalField(max_digits=15, decimal_places=0)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MaPhieuNhap', 'MaSach'], name='unique_ct_nhap_sach')
        ]
        # unique_together = ('MaPhieuNhap', 'MaSach')

    def __str__(self):
        return f"Chi tiết nhập #{self.MaPhieuNhap} - {self.MaSach}"
    
    # def clean(self):
    #     thamso = ThamSo.objects.first()
    #     if not thamso:
    #         raise ValidationError("Chưa cấu hình tham số hệ thống.")

    #     # Rule 1: SLNhap >= SLNhapTT
    #     if self.SLNhap < thamso.SLNhapTT:
    #         raise ValidationError(
    #             f"Số lượng nhập phải ≥ {thamso.SLNhapTT}."
    #         )

    #     # Rule 2: SLTon (after update) must not exceed TonTD
    #     current_slton = self.MaSach.SLTon
    #     if self.pk:
    #         old_slnhap = CT_NhapSach.objects.get(pk=self.pk).SLNhap
    #         diff = self.SLNhap - old_slnhap
    #     else:
    #         diff = self.SLNhap
    #     new_slton = current_slton + diff
        
    #     if new_slton > thamso.TonTD:
    #         raise ValidationError(
    #             f"Tồn sau khi nhập ({new_slton}) vượt quá giới hạn tồn tối đa ({thamso.TonTD})."
    #         )
    
    def save(self, *args, **kwargs):
        # self.clean()  # Validate before saving
        # --- Update case ---
        if self.pk:
            # Get the previous SLNhap from the database
            old = CT_NhapSach.objects.get(pk=self.pk)
            diff = self.SLNhap - old.SLNhap
        else:
            # New object
            diff = self.SLNhap

        super().save(*args, **kwargs)

        # Update SLTon
        self.MaSach.SLTon += diff
        self.MaSach.save()

    def delete(self, *args, **kwargs):
        # When deleting, subtract the imported quantity
        self.MaSach.SLTon -= self.SLNhap
        self.MaSach.save()
        super().delete(*args, **kwargs)

class PhieuThuTien(models.Model):
    MaPhieuThu = models.AutoField(primary_key=True)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.RESTRICT)
    NgayThu = models.DateField()
    NguoiThu = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='NguoiThu',
        verbose_name='Người thu'
    )
    SoTienThu = models.DecimalField(max_digits=15, decimal_places=0)
    
    def __str__(self):
        return f"Phiếu thu #{self.MaPhieuThu} - {self.MaKH.HoTen}"
    
    def save(self, *args, **kwargs):
        if self.pk:
            # Update case
            old = PhieuThuTien.objects.get(pk=self.pk)
            diff = self.SoTienThu - old.SoTienThu
        else:
            # New object
            diff = self.SoTienThu
        
        super().save(*args, **kwargs)
        # Update customer's debt
        self.MaKH.SoTienNo -= diff
        if self.MaKH.SoTienNo < 0:
            raise ValueError("Số tiền nợ không thể âm.")
        self.MaKH.save()
              
    def delete(self, *args, **kwargs):
        # When deleting, add the amount back to the customer's debt
        self.MaKH.SoTienNo += self.SoTienThu
        self.MaKH.save()
        super().delete(*args, **kwargs)
    
class ThamSo(models.Model):
    # id = models.AutoField(primary_key=True)  # Django requires a primary key
    SLNhapTT = models.PositiveIntegerField()  # Minimum import quantity
    TonTD = models.PositiveIntegerField()    # Maximum inventory
    NoTD = models.DecimalField(max_digits=15, decimal_places=0)  # Maximum customer debt
    TonTT = models.PositiveIntegerField()    # Minimum inventory before restocking
    TiLe = models.DecimalField(max_digits=5, decimal_places=2)  # Ratio/Rate
    SDQD4 = models.BooleanField() # Decision number reference
    
class HoaDon(models.Model):
    MaHD = models.AutoField(primary_key=True)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.RESTRICT, related_name='hoadon')
    NgayLap = models.DateField()
    NguoiLapHD = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='NguoiLapHD',
        verbose_name='Người lập Hóa Đơn'
    )
    TongTien = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, null=True)
    SoTienTra = models.DecimalField(max_digits=15, decimal_places=0, blank=True, default=0, null=True)
    ConLai = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, null=True)
    MaSach = models.ManyToManyField(Sach, through='CT_HoaDon', related_name='HoaDon')

    def __str__(self):
        return f"Hóa đơn #{self.MaHD} - {self.MaKH.HoTen}"
    
    def save(self, *args, **kwargs):
        self.TongTien = sum(ct.ThanhTien for ct in self.ct_hoadon.all())
        self.ConLai = self.TongTien - self.SoTienTra

        # Update customer's debt
        if self.pk:
            # Update case
            old = HoaDon.objects.get(pk=self.pk)
            diff = self.ConLai - old.ConLai
        else:
            diff = self.ConLai
        self.MaKH.SoTienNo += diff

        if self.MaKH.SoTienNo < 0:
            raise ValueError("Số tiền nợ không thể âm.")
        
        super().save(*args, **kwargs)
        self.MaKH.save()
    
class CT_HoaDon(models.Model):
    MaHD = models.ForeignKey(HoaDon, on_delete=models.CASCADE, related_name='ct_hoadon')
    MaSach = models.ForeignKey(Sach, on_delete=models.RESTRICT)
    SLBan = models.PositiveIntegerField()
    GiaBan = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, null=True)
    ThanhTien = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, null=True)  # Make it non-editable

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MaHD', 'MaSach'], name='unique_ct_hoa_don')
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update HoaDon: TongTien and ConLai
        hoadon = self.MaHD
        hoadon.save()

        sach = self.MaSach
        sach.SLTon -= self.SLBan
        if sach.SLTon < 0:
            raise ValueError("Số lượng sách không đủ để bán.")
        sach.save()

    def delete(self, *args, **kwargs):
        # Update HoaDon: TongTien and ConLai
        hoadon = self.MaHD
        super().delete(*args, **kwargs)
        hoadon.save()

        sach = self.MaSach
        sach.SLTon += self.SLBan
        sach.save()

class BaoCaoTon(models.Model):
    MaBCTon = models.AutoField(primary_key=True)
    Thang = models.DateField(unique=True)
    MaSach = models.ManyToManyField(Sach, through='CT_BCTon', related_name='BaoCaoTon')

    def __str__(self):
        return f"Báo cáo tồn - Tháng {self.Thang}"
    
class CT_BCTon(models.Model):
    MaBCTon = models.ForeignKey(BaoCaoTon, on_delete=models.CASCADE)
    MaSach = models.ForeignKey(Sach, on_delete=models.RESTRICT)
    TonDau = models.PositiveIntegerField(blank=True, default=0, editable=False, null=True)
    PhatSinh = models.PositiveIntegerField(blank=True, default=0, editable=False, null=True)
    TonCuoi = models.PositiveIntegerField(blank=True, default=0, editable=False, null=True)  # Make it non-editable
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['MaBCTon', 'MaSach'], name='unique_ct_bao_cao_ton')
        ]

    def __str__(self):
        return f"Chi tiết báo cáo tồn - {self.MaBCTon} - {self.MaSach}"

class BaoCaoCongNo(models.Model):
    MaBCCN = models.AutoField(primary_key=True)
    Thang = models.DateField(unique=True)
    MaKH = models.ManyToManyField(KhachHang, through='CT_BCCongNo', related_name='BaoCaoCongNo')

    def __str__(self):
        return f"Báo cáo công nợ - Tháng {self.Thang}"
    
class CT_BCCongNo(models.Model):
    MaBCCN = models.ForeignKey(BaoCaoCongNo, on_delete=models.CASCADE)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.RESTRICT)
    NoDau = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, null=True)
    PhatSinh = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, null=True)
    NoCuoi = models.DecimalField(max_digits=15, decimal_places=0, default=0, editable=False, null=True)
    
    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['MaBCCN', 'MaKH'], name='unique_ct_bao_cao_congno')
        ]
    
    def __str__(self):
        return f"Chi tiết báo cáo công nợ - {self.MaBCCN} - {self.MaKH}"

class GroupModelPermission(models.Model):
    group = models.ForeignKey(NhomNguoiDung, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_change = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('group', 'model_name')