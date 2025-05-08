from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as NguoiDung
from django.contrib.auth.models import Group as NhomNguoiDung
from django.contrib.auth.models import Permission as ChucNang
from django.conf import settings

class TheLoai(models.Model):
    MaTheLoai = models.AutoField(primary_key=True)
    TenTheLoai = models.CharField(max_length=100)
    
    def __str__(self):
        return self.TenTheLoai

class DauSach(models.Model):
    MaDauSach = models.AutoField(primary_key=True)
    TenSach = models.CharField(max_length=200)
    MaTheLoai = models.ForeignKey(TheLoai, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.TenSach

class TacGia(models.Model):
    MaTG = models.AutoField(primary_key=True)
    TenTG = models.CharField(max_length=100)
    
    def __str__(self):
        return self.TenTG

class DauSach_TacGia(models.Model):
    MaDauSach = models.ForeignKey(DauSach, on_delete=models.CASCADE)
    MaTG = models.ForeignKey(TacGia, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('MaDauSach', 'MaTG')

class Sach(models.Model):
    MaSach = models.AutoField(primary_key=True)
    MaDauSach = models.ForeignKey(DauSach, on_delete=models.CASCADE)
    NXB = models.CharField(max_length=100)
    NamXB = models.IntegerField()
    SLTon = models.IntegerField()
    
    def __str__(self):
        return f"{self.MaDauSach.TenSach} - {self.NXB} ({self.NamXB})"

class KhachHang(models.Model):
    MaKH = models.AutoField(primary_key=True)
    HoTen = models.CharField(max_length=100)
    DiaChi = models.CharField(max_length=200, null=True, blank=True)
    DienThoai = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    SoTienNo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    def __str__(self):
        return self.HoTen

class PhieuNhapSach(models.Model):
    MaPhieuNhap = models.AutoField(primary_key=True)
    NgayNhap = models.DateField()
    NguoiNhap = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='phieunhapsach_created',
        verbose_name='Người nhập'
    )
    def __str__(self):
        return f"Phiếu nhập #{self.MaPhieuNhap} - {self.NgayNhap}"

class CT_NhapSach(models.Model):
    MaPhieuNhap = models.ForeignKey(PhieuNhapSach, on_delete=models.CASCADE)
    MaSach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    SLNhap = models.IntegerField()
    GiaNhap = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        unique_together = ('MaPhieuNhap', 'MaSach')

class HoaDon(models.Model):
    MaHD = models.AutoField(primary_key=True)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NgayLap = models.DateField()
    NguoiLapHD = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='hoadon_created',
        verbose_name='Người lập HĐ'
    )
    TongTien = models.DecimalField(max_digits=15, decimal_places=2)
    SoTienTra = models.DecimalField(max_digits=15, decimal_places=2)
    ConLai = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"Hóa đơn #{self.MaHD} - {self.MaKH.HoTen}"

class CT_HoaDon(models.Model):
    MaHD = models.ForeignKey(HoaDon, on_delete=models.CASCADE)
    MaSach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    SLBan = models.IntegerField()
    GiaBan = models.DecimalField(max_digits=15, decimal_places=2)
    ThanhTien = models.DecimalField(max_digits=15, decimal_places=2, editable=False)  # Make it non-editable

    class Meta:
        unique_together = ('MaHD', 'MaSach')

    def save(self, *args, **kwargs):
        # Automatically calculate GiaBan based on GiaNhap and TiLe
        thamso = ThamSo.objects.first()
        last_nhap = CT_NhapSach.objects.filter(MaSach=self.MaSach).order_by('-MaPhieuNhap').first()
        if last_nhap:
            self.GiaBan = last_nhap.GiaNhap * (thamso.TiLe / 100)
        else:
            raise ValueError("No GiaNhap found for this Sach.")

        # Automatically calculate ThanhTien
        self.ThanhTien = self.SLBan * self.GiaBan
        super().save(*args, **kwargs)

class PhieuThuTien(models.Model):
    MaPhieuThu = models.AutoField(primary_key=True)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NgayThu = models.DateField()
    NguoiThu = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='phieuthutien_created',
        verbose_name='Người thu'
    )
    SoTienThu = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"Phiếu thu #{self.MaPhieuThu} - {self.MaKH.HoTen}"

class BaoCaoTon(models.Model):
    MaBCTon = models.AutoField(primary_key=True)
    Thang = models.IntegerField()
    Nam = models.IntegerField()
    def __str__(self):
        return f"Báo cáo tồn - Tháng {self.Thang}/{self.Nam}"
class CT_BCTon(models.Model):
    MaBCTon = models.ForeignKey(BaoCaoTon, on_delete=models.CASCADE)
    MaSach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    TonDau = models.IntegerField()
    PhatSinh = models.IntegerField()
    TonCuoi = models.IntegerField(editable=False)  # Make it non-editable

    def save(self, *args, **kwargs):
        # Automatically calculate TonCuoi
        self.TonCuoi = self.TonDau + self.PhatSinh
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('MaBCTon', 'MaSach')

class BaoCaoCongNo(models.Model):
    MaBCCN = models.AutoField(primary_key=True)
    Thang = models.IntegerField()
    Nam = models.IntegerField()
    def __str__(self):
        return f"Báo cáo công nợ - Tháng {self.Thang}/{self.Nam}"


class CT_BCCongNo(models.Model):
    MaBCCN = models.ForeignKey(BaoCaoCongNo, on_delete=models.CASCADE)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NoDau = models.DecimalField(max_digits=15, decimal_places=2)
    PhatSinh = models.DecimalField(max_digits=15, decimal_places=2)
    NoCuoi = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        unique_together = ('MaBCCN', 'MaKH')

class ThamSo(models.Model):
    id = models.AutoField(primary_key=True)  # Django requires a primary key
    SLNhapTT = models.IntegerField()  # Minimum import quantity
    TonTD = models.IntegerField()    # Maximum inventory
    NoTD = models.DecimalField(max_digits=15, decimal_places=2)  # Maximum customer debt
    TonTT = models.IntegerField()    # Minimum inventory before restocking
    TiLe = models.DecimalField(max_digits=5, decimal_places=2)  # Ratio/Rate
    SDQD4 = models.BooleanField() # Decision number reference
    def save(self, *args, **kwargs):
        # Ensure only one object exists
        if ThamSo.objects.exists() and not self.pk:
            raise ValueError("Only one ThamSo object is allowed.")
        # Validate edge cases
        if self.SLNhapTT <= 0:
            raise ValueError("SLNhapTT must be greater than 0.")
        if self.TonTD <= 0:
            raise ValueError("TonTD must be greater than 0.")
        if self.NoTD <= 0:
            raise ValueError("NoTD must be greater than 0.")
        if self.TonTT < 0:
            raise ValueError("TonTT cannot be negative.")
        if self.TiLe <= 0:
            raise ValueError("TiLe must be more than 0.")
        super().save(*args, **kwargs)

class GroupModelPermission(models.Model):
    group = models.ForeignKey(NhomNguoiDung, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_change = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('group', 'model_name')