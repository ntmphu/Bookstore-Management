from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group as NhomNguoiDung
from django.contrib.auth.models import Permission as ChucNang
from django.conf import settings

class TheLoai(models.Model):
    MaTheLoai = models.AutoField(primary_key=True)
    TenTheLoai = models.CharField(max_length=200)

    def __str__(self):
        return self.TenTheLoai

class TacGia(models.Model):
    MaTG = models.AutoField(primary_key=True)
    TenTG = models.CharField(max_length=200)

    def __str__(self):
        return self.TenTG

class DauSach(models.Model):
    MaDauSach = models.AutoField(primary_key=True)
    TenSach = models.CharField(max_length=200)
    MaTheLoai = models.ForeignKey(TheLoai, blank=True, null=True, on_delete=models.CASCADE, related_name='DauSach')
    MaTG = models.ManyToManyField(TacGia, blank=True, related_name='DauSach')

    def __str__(self):
        return self.TenSach

class Sach(models.Model):
    MaSach = models.AutoField(primary_key=True)
    MaDauSach = models.ForeignKey(DauSach, on_delete=models.CASCADE, related_name='sach')
    NXB = models.CharField(max_length=200)
    NamXB = models.IntegerField()
    SLTon = models.IntegerField()

    def __str__(self):
        return self.DauSach.TenSach

class KhachHang(models.Model):
    MaKhachHang = models.AutoField(primary_key=True)
    HoTen = models.CharField(max_length=200)
    DiaChi = models.CharField(max_length=200)
    DienThoai = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    SoTienNo = models.IntegerField()

    def __str__(self):
        return self.HoTen

class PhieuNhapSach(models.Model):
    MaPhieuNhap = models.AutoField(primary_key=True)
    NgayNhap = models.DateField()
    NguoiNhap = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='NguoiNhap',
        verbose_name='Người nhập'
    )
    MaSach = models.ManyToManyField(Sach, through='CT_NhapSach', related_name='PhieuNhapSach')

    def __str__(self):
        return f"Phiếu nhập #{self.MaPhieuNhap} - {self.NgayNhap}"

class CT_NhapSach(models.Model):
    MaPhieuNhap = models.ForeignKey(PhieuNhapSach, on_delete=models.CASCADE)
    MaSach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    SLNhap = models.IntegerField()
    GiaNhap = models.DecimalField(max_digits=15, decimal_places=2)
    
    class Meta:
        unique_together = ('MaPhieuNhap', 'MaSach')

    def __str__(self):
        return f"Chi tiết nhập #{self.MaPhieuNhap} - {self.MaSach}"

class PhieuThuTien(models.Model):
    MaPhieuThu = models.AutoField(primary_key=True)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NgayThu = models.DateField()
    NguoiThu = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='NguoiThu',
        verbose_name='Người thu'
    )
    SoTienThu = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"Phiếu thu #{self.MaPhieuThu} - {self.MaKH.HoTen}"
    
class ThamSo(models.Model):
    id = models.AutoField(primary_key=True)  # Django requires a primary key
    SLNhapTT = models.IntegerField()  # Minimum import quantity
    TonTD = models.IntegerField()    # Maximum inventory
    NoTD = models.DecimalField(max_digits=15, decimal_places=2)  # Maximum customer debt
    TonTT = models.IntegerField()    # Minimum inventory before restocking
    TiLe = models.DecimalField(max_digits=5, decimal_places=2)  # Ratio/Rate
    SDQD4 = models.BooleanField() # Decision number reference
    
class HoaDon(models.Model):
    MaHD = models.AutoField(primary_key=True)
    MaKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    NgayLap = models.DateField()
    NguoiLapHD = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='NguoiLapHD',
        verbose_name='Người lập Hóa Đơn'
    )
    TongTien = models.DecimalField(max_digits=15, decimal_places=2)
    SoTienTra = models.DecimalField(max_digits=15, decimal_places=2)
    ConLai = models.DecimalField(max_digits=15, decimal_places=2)
    MaSach = models.ManyToManyField(Sach, through='CT_HoaDon', related_name='HoaDon')

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

class BaoCaoTon(models.Model):
    MaBCTon = models.AutoField(primary_key=True)
    Thang = models.IntegerField()
    Nam = models.IntegerField()
    MaSach = models.ManyToManyField(Sach, through='CT_BCTon', related_name='BaoCaoTon')
    
    def __str__(self):
        return f"Báo cáo tồn - Tháng {self.Thang}/{self.Nam}"
    
class CT_BCTon(models.Model):
    MaBCTon = models.ForeignKey(BaoCaoTon, on_delete=models.CASCADE)
    MaSach = models.ForeignKey(Sach, on_delete=models.CASCADE)
    TonDau = models.IntegerField()
    PhatSinh = models.IntegerField()
    TonCuoi = models.IntegerField(editable=False)  # Make it non-editable
    
    class Meta:
        unique_together = ('MaBCTon', 'MaSach')

    def __str__(self):
        return f"Chi tiết báo cáo tồn - {self.MaBCTon} - {self.MaSach}"

class BaoCaoCongNo(models.Model):
    MaBCCN = models.AutoField(primary_key=True)
    Thang = models.IntegerField()
    Nam = models.IntegerField()
    MaKH = models.ManyToManyField(KhachHang, through='CT_BCCongNo', related_name='BaoCaoCongNo')

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