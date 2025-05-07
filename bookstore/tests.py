from django.test import TestCase
from .models import *
from datetime import date

class SignalTests(TestCase):
    def setUp(self):
        # Create a ThamSo object
        ThamSo.objects.create(SLNhapTT=10, TonTD=100, NoTD=500000, TonTT=5, TiLe=120, SDQD4=True)

        # Create a TheLoai object
        the_loai = TheLoai.objects.create(TenTheLoai="Fiction")

        # Create a TacGia object
        tac_gia = TacGia.objects.create(TenTG="Author A")

        # Create a DauSach object
        dau_sach = DauSach.objects.create(TenSach="Sample Book", MaTheLoai=the_loai)

        # Link DauSach with TacGia
        DauSach_TacGia.objects.create(MaDauSach=dau_sach, MaTG=tac_gia)

        # Create a Sach object
        self.sach = Sach.objects.create(MaDauSach=dau_sach, NXB="NXB Kim Dong", NamXB=2023, SLTon=50)

        # Create a KhachHang object
        self.khachhang = KhachHang.objects.create(HoTen="Nguyen Van A", SoTienNo=0)

        # Create a NguoiDung object
        nguoi_nhap = NguoiDung.objects.create(username="admin", password="password")

        # Create a PhieuNhapSach object
        self.phieu_nhap = PhieuNhapSach.objects.create(NgayNhap=date.today(), NguoiNhap=nguoi_nhap)

        # Create a CT_NhapSach object
        CT_NhapSach.objects.create(MaPhieuNhap=self.phieu_nhap, MaSach=self.sach, SLNhap=20, GiaNhap=80000)

        # Create a BaoCaoTon and BaoCaoCongNo for the current month
        self.baocaoton = BaoCaoTon.objects.create(Thang=date.today().month, Nam=date.today().year)
        self.baocaocongno = BaoCaoCongNo.objects.create(Thang=date.today().month, Nam=date.today().year)

        # Create a CT_BCTon object
        CT_BCTon.objects.create(MaBCTon=self.baocaoton, MaSach=self.sach, TonDau=50, PhatSinh=20)

        # Create a CT_BCCongNo object
        CT_BCCongNo.objects.create(MaBCCN=self.baocaocongno, MaKH=self.khachhang, NoDau=0, PhatSinh=0, NoCuoi=0)
    def test_ct_hoadon_signal(self):
        # Create a HoaDon object
        hoadon = HoaDon.objects.create(MaKH=self.khachhang, NgayLap=date.today(), TongTien=0, SoTienTra=0, ConLai=0, NguoiLapHD_id=1)

        # Create a CT_HoaDon object
        ct_hoadon = CT_HoaDon.objects.create(MaHD=hoadon, MaSach=self.sach, SLBan=5)

        # Verify that GiaBan is calculated correctly
        self.assertEqual(ct_hoadon.GiaBan, 80000 * 1.2)  # GiaNhap * TiLe

        # Verify that ThanhTien is calculated correctly
        self.assertEqual(ct_hoadon.ThanhTien, ct_hoadon.SLBan * ct_hoadon.GiaBan)

        # Verify that Sach.SLTon is updated
        self.sach.refresh_from_db()
        self.assertEqual(self.sach.SLTon, 45)

        # Verify that CT_BCTon is updated
        ct_bcton = CT_BCTon.objects.get(MaBCTon=self.baocaoton, MaSach=self.sach)
        self.assertEqual(ct_bcton.TonCuoi, ct_bcton.TonDau + ct_bcton.PhatSinh - 5)

    def test_ct_nhapsach_signal(self):
        # Create a new PhieuNhapSach for this test
        new_phieu_nhap = PhieuNhapSach.objects.create(
            NgayNhap=date.today(), 
            NguoiNhap_id=1
        )
        
        # Create a CT_NhapSach object with the new PhieuNhapSach
        CT_NhapSach.objects.create(
            MaPhieuNhap=new_phieu_nhap, 
            MaSach=self.sach, 
            SLNhap=20, 
            GiaNhap=80000
        )
    def test_phieuthutien_signal(self):
        # First create debt through HoaDon
        hoadon = HoaDon.objects.create(MaKH=self.khachhang, NgayLap=date.today(), TongTien=0, SoTienTra=0, ConLai=0, NguoiLapHD_id=1)

        # Create a CT_HoaDon object
        ct_hoadon = CT_HoaDon.objects.create(MaHD=hoadon, MaSach=self.sach, SLBan=5)

        
        # Now create PhieuThuTien
        phieuthutien = PhieuThuTien.objects.create(
            MaKH=self.khachhang,
            NgayThu=date.today(),
            SoTienThu=200000,
            NguoiThu_id=1
        )
    def test_hoadon_signal(self):
        # Create a HoaDon object
        hoadon = HoaDon.objects.create(MaKH=self.khachhang, NgayLap=date.today(), TongTien=100000, SoTienTra=50000, ConLai=50000, NguoiLapHD_id=1)

        # Verify that KhachHang.SoTienNo is updated
        self.khachhang.refresh_from_db()
        self.assertEqual(self.khachhang.SoTienNo, 50000)

        # Verify that CT_BCCongNo.PhatSinh is updated
        ct_bccongno = CT_BCCongNo.objects.get(MaBCCN=self.baocaocongno, MaKH=self.khachhang)
        self.assertEqual(ct_bccongno.PhatSinh, 50000)

    def test_thamso_constraints(self):
        # Verify that only one ThamSo object exists
        with self.assertRaises(ValueError):
            ThamSo.objects.create(SLNhapTT=5, TonTD=50, NoTD=100000, TonTT=2, TiLe=50, SDQD4=False)

        # Verify edge case validation
        thamso = ThamSo.objects.first()
        thamso.TiLe = 0
        with self.assertRaises(ValueError):
            thamso.save()