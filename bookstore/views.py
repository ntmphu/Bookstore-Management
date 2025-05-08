from rest_framework import viewsets, permissions
from .models import (
    KhachHang, Sach, HoaDon, CT_HoaDon, PhieuThuTien,
    DauSach, TacGia, TheLoai, DauSach_TacGia,
    PhieuNhapSach, CT_NhapSach,
    BaoCaoTon, CT_BCTon, BaoCaoCongNo, CT_BCCongNo, ThamSo
)
from .serializers import (
    KhachHangSerializer, SachSerializer, HoaDonSerializer, CTHoaDonSerializer, PhieuThuTienSerializer,
    DauSachSerializer, TacGiaSerializer, TheLoaiSerializer, DauSachTacGiaSerializer,
    PhieuNhapSachSerializer, CTNhapSachSerializer,
    BaoCaoTonSerializer, CTBCTonSerializer, BaoCaoCongNoSerializer, CTBCCongNoSerializer, ThamSoSerializer
)



class IsInGroups(permissions.BasePermission):
    """
    Allow access if user is in any of the allowed groups.
    """
    def __init__(self, groups):
        self.groups = groups

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name__in=self.groups).exists()


# Permission classes
class IsQuanLi(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='quanli').exists()

class IsNguoiLapHD(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='NguoiLapHD').exists()

class IsNguoiNhap(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='NguoiNhap').exists()

class IsNguoiThu(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='NguoiThu').exists()

class QuanLiOrGroupPermission(permissions.BasePermission):
    """
    Allow Quanli all, otherwise check group-specific permission.
    """
    group_perm = None  # override in subclass

    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Quanli').exists():
            return True
        if self.group_perm:
            return request.user and request.user.groups.filter(name=self.group_perm).exists()
        return False

# ViewSets

# KhachHang: Nguoilaphd (full), Nguoithu (view), Quanli (all)
class KhachHangViewSet(viewsets.ModelViewSet):
    queryset = KhachHang.objects.all()
    serializer_class = KhachHangSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [IsInGroups(['quanli', 'NguoiLapHD', 'NguoiThu'])]
        return [IsInGroups(['quanli', 'NguoiLapHD'])]

# Sach: Nguoilaphd (view), Nguoi nhap (full), Quanli (all)
class SachViewSet(viewsets.ModelViewSet):
    queryset = Sach.objects.all()
    serializer_class = SachSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [IsInGroups(["quanli" , "NguoiLapHD" , "NguoiNhap"])]
        return [IsInGroups(["quanli" , "NguoiNhap"])]

# HoaDon: Nguoilaphd (full), Nguoithu (view), Quanli (all)
class HoaDonViewSet(viewsets.ModelViewSet):
    queryset = HoaDon.objects.all()
    serializer_class = HoaDonSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [IsInGroups(['quanli', 'NguoiLapHD', 'NguoiThu'])]
        return [IsInGroups(['quanli', 'NguoiLapHD'])]

# CT_HoaDon: Nguoilaphd (full), Quanli (all)
class CTHoaDonViewSet(viewsets.ModelViewSet):
    queryset = CT_HoaDon.objects.all()
    serializer_class = CTHoaDonSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiLapHD"])]

# PhieuThuTien: Nguoithu (full), Quanli (all)
class PhieuThuTienViewSet(viewsets.ModelViewSet):
    queryset = PhieuThuTien.objects.all()
    serializer_class = PhieuThuTienSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiThu"])]

# DauSach: Nguoi nhap (full), Quanli (all)
class DauSachViewSet(viewsets.ModelViewSet):
    queryset = DauSach.objects.all()
    serializer_class = DauSachSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiNhap"])]

# TacGia: Nguoi nhap (full), Quanli (all)
class TacGiaViewSet(viewsets.ModelViewSet):
    queryset = TacGia.objects.all()
    serializer_class = TacGiaSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiNhap"])]

# TheLoai: Nguoi nhap (full), Quanli (all)
class TheLoaiViewSet(viewsets.ModelViewSet):
    queryset = TheLoai.objects.all()
    serializer_class = TheLoaiSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiNhap"])]

# DauSach_TacGia: Nguoi nhap (full), Quanli (all)
class DauSachTacGiaViewSet(viewsets.ModelViewSet):
    queryset = DauSach_TacGia.objects.all()
    serializer_class = DauSachTacGiaSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiNhap"])]

# PhieuNhapSach: Nguoi nhap (full), Quanli (all)
class PhieuNhapSachViewSet(viewsets.ModelViewSet):
    queryset = PhieuNhapSach.objects.all()
    serializer_class = PhieuNhapSachSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiNhap"])]

# CT_NhapSach: Nguoi nhap (full), Quanli (all)
class CTNhapSachViewSet(viewsets.ModelViewSet):
    queryset = CT_NhapSach.objects.all()
    serializer_class = CTNhapSachSerializer

    def get_permissions(self):
        return [IsInGroups(["quanli" , "NguoiNhap"])]

class BaoCaoTonViewSet(viewsets.ModelViewSet):
    queryset = BaoCaoTon.objects.all()
    serializer_class = BaoCaoTonSerializer
    permission_classes = [IsQuanLi]

class CTBCTonViewSet(viewsets.ModelViewSet):
    queryset = CT_BCTon.objects.all()
    serializer_class = CTBCTonSerializer
    permission_classes = [IsQuanLi]

class BaoCaoCongNoViewSet(viewsets.ModelViewSet):
    queryset = BaoCaoCongNo.objects.all()
    serializer_class = BaoCaoCongNoSerializer
    permission_classes = [IsQuanLi]

class CTBCCongNoViewSet(viewsets.ModelViewSet):
    queryset = CT_BCCongNo.objects.all()
    serializer_class = CTBCCongNoSerializer
    permission_classes = [IsQuanLi]

class ThamSoViewSet(viewsets.ModelViewSet):
    queryset = ThamSo.objects.all()
    serializer_class = ThamSoSerializer
    permission_classes = [IsQuanLi]