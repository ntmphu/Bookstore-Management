from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.db import IntegrityError

from .models import (
    KhachHang, Sach, HoaDon, CT_HoaDon, PhieuThuTien,
    DauSach, TacGia, TheLoai, NXB,
    PhieuNhapSach, CT_NhapSach,
    BaoCaoTon, CT_BCTon, BaoCaoCongNo, CT_BCCongNo, ThamSo
)

from .serializers import (
    KhachHangSerializer, SachSerializer, HoaDonSerializer, CTHoaDonSerializer, PhieuThuTienSerializer,
    DauSachSerializer, TacGiaSerializer, TheLoaiSerializer, NXBSerializer,
    PhieuNhapSachSerializer, CTNhapSachSerializer,
    BaoCaoTonSerializer, CT_BCTonSerializer, BaoCaoCongNoSerializer, CT_BCCNSerializer, ThamSoSerializer,
    
)

from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter, CharFilter, DateFilter
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, CreateUserSerializer


def get_valid_groups():
    """Get all group names from the database"""
    return list(Group.objects.values_list('name', flat=True))
# class IsAuthenticated(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if not request.user or not request.user.is_authenticated:
#             return False

#         if request.user.is_superuser:
#             return True

#         model_name = view.queryset.model._meta.model_name
#         user_groups = request.user.groups.all()
        
#         group_perms = GroupModelPermission.objects.filter(
#             group__in=user_groups,
#             model_name=model_name
#         )

#         if request.method in permissions.SAFE_METHODS:
#             return group_perms.filter(can_view=True).exists()
#         elif request.method == 'POST':
#             return group_perms.filter(can_add=True).exists()
#         elif request.method in ['PUT', 'PATCH']:
#             return group_perms.filter(can_change=True).exists()
#         elif request.method == 'DELETE':
#             return group_perms.filter(can_delete=True).exists()

class UserManagementViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Any authenticated user can access

    @action(detail=False, methods=['post'])
    def create_staff(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This will handle role assignment
            # Set gender if provided
            if 'gioiTinh' in request.data:
                user.profile.gioiTinh = request.data['gioiTinh']
                user.profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('new_password')
        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({"status": "password changed"})
        return Response(
            {"error": "No password provided"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['put'])
    def update_profile(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({"status": "user deactivated"})
    @action(detail=True, methods=['post'])
    def reactivate(self, request, pk=None):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({"status": "user reactivated"})

# CT_HoaDon: Nguoilaphd (full), Quanli (all)
class CTHoaDonViewSet(viewsets.ModelViewSet):
    queryset = CT_HoaDon.objects.all()
    serializer_class = CTHoaDonSerializer

    permission_classes = [IsAuthenticated]

# PhieuThuTien: Nguoithu (full), Quanli (all)
class PhieuThuTienViewSet(viewsets.ModelViewSet):
    queryset = PhieuThuTien.objects.all()
    serializer_class = PhieuThuTienSerializer

    permission_classes = [IsAuthenticated]

# DauSach: Nguoi nhap (full), Quanli (all)
class DauSachViewSet(viewsets.ModelViewSet):
    queryset = DauSach.objects.all()
    serializer_class = DauSachSerializer
    permission_classes = [IsAuthenticated]

# TacGia: Nguoi nhap (full), Quanli (all)
class TacGiaViewSet(viewsets.ModelViewSet):
    queryset = TacGia.objects.all()
    serializer_class = TacGiaSerializer
    permission_classes = [IsAuthenticated]

class NXBViewSet(viewsets.ModelViewSet):
    queryset = NXB.objects.all()
    serializer_class = NXBSerializer
    permission_classes = [IsAuthenticated]

# TheLoai: Nguoi nhap (full), Quanli (all)
class TheLoaiViewSet(viewsets.ModelViewSet):
    queryset = TheLoai.objects.all()
    serializer_class = TheLoaiSerializer
    permission_classes = [IsAuthenticated]

# CT_NhapSach: Nguoi nhap (full), Quanli (all)
class CTNhapSachViewSet(viewsets.ModelViewSet):
    queryset = CT_NhapSach.objects.all()
    serializer_class = CTNhapSachSerializer

    permission_classes = [IsAuthenticated]

class CTBCTonViewSet(viewsets.ModelViewSet):
    queryset = CT_BCTon.objects.all()
    serializer_class = CT_BCTonSerializer
    permission_classes = [IsAuthenticated]

class CTBCCongNoViewSet(viewsets.ModelViewSet):
    queryset = CT_BCCongNo.objects.all()
    serializer_class = CT_BCCNSerializer
    permission_classes = [IsAuthenticated]

class ThamSoViewSet(viewsets.ModelViewSet):
    queryset = ThamSo.objects.all()
    serializer_class = ThamSoSerializer
    permission_classes = [IsAuthenticated]

# Custom filter for Sach
class SachFilter(FilterSet):
    # Filter by book name (DauSach.TenSach)
    ten_sach = CharFilter(field_name='MaDauSach__TenSach', lookup_expr='icontains')
    # Filter by author name (TacGia.TenTG, many-to-many)
    tac_gia = CharFilter(method='filter_tac_gia')
    # Filter by genre name (TheLoai.TenTheLoai)
    the_loai = CharFilter(field_name='MaDauSach__MaTheLoai__TenTheLoai', lookup_expr='icontains')
    # Filter by publisher (Sach.NXB)
    nxb = CharFilter(field_name='NXB__TenNXB', lookup_expr='icontains')
    # Filter by year (Sach.NamXB)
    nam_xb = NumberFilter(field_name='NamXB')
    nam_xb_min = NumberFilter(field_name='NamXB', lookup_expr='gte')
    nam_xb_max = NumberFilter(field_name='NamXB', lookup_expr='lte')
    # Filter by stock (Sach.SLTon)
    slton_min = NumberFilter(field_name='SLTon', lookup_expr='gte')
    slton_max = NumberFilter(field_name='SLTon', lookup_expr='lte')

    def filter_tac_gia(self, queryset, name, value):
        # MaDauSach is FK to DauSach, MaTG is M2M in DauSach
        return queryset.filter(MaDauSach__MaTG__TenTG__icontains=value)

    class Meta:
        model = Sach
        fields = [
            'ten_sach', 'tac_gia', 'the_loai', 'nxb',
            'nam_xb', 'nam_xb_min', 'nam_xb_max',
            'slton_min', 'slton_max'
        ]

class SachViewSet(viewsets.ModelViewSet):
    queryset = Sach.objects.all()
    serializer_class = SachSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SachFilter

class KhachHangFilter(FilterSet):
    id = NumberFilter(field_name='MaKhachHang')
    name = CharFilter(field_name='HoTen', lookup_expr='icontains')
    phone = CharFilter(field_name='DienThoai', lookup_expr='icontains')
    invoiceId = CharFilter(field_name='hoadon__MaHD', lookup_expr='icontains')  # Ensure 'hoadon' is the related_name for HoaDon in KhachHang

    class Meta:
        model = KhachHang
        fields = ['MaKhachHang', 'HoTen', 'DienThoai', 'hoadon__MaHD']

class KhachHangViewSet(viewsets.ModelViewSet):
    queryset = KhachHang.objects.all()
    serializer_class = KhachHangSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = KhachHangFilter

# PhieuNhapSach filterset
class PhieuNhapSachFilter(FilterSet):
    maNhap = NumberFilter(field_name='MaPhieuNhap')
    ngayNhap = DateFilter(field_name='NgayNhap')
    # maSach and tenSach are not direct fields, but you can filter by related Sach
    maSach = NumberFilter(field_name='MaSach')
    tenSach = CharFilter(field_name='MaSach__MaDauSach__TenSach', lookup_expr='icontains')

    class Meta:
        model = PhieuNhapSach
        fields = ['MaPhieuNhap', 'NgayNhap', 'MaSach', 'MaSach__MaDauSach__TenSach']

# PhieuNhapSach: Nguoi nhap (full), Quanli (all)
class PhieuNhapSachViewSet(viewsets.ModelViewSet):
    queryset = PhieuNhapSach.objects.all()
    serializer_class = PhieuNhapSachSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PhieuNhapSachFilter

# BaoCaoTon filterset
class BaoCaoTonFilter(FilterSet):
    thang = DateFilter(field_name='Thang', lookup_expr='month')
    # book/stock: filter by related CT_BCTon
    maSach = NumberFilter(field_name='ct_bcton__MaSach__MaSach')
    tenSach = CharFilter(field_name='ct_bcton__MaSach__MaDauSach__TenSach', lookup_expr='icontains')
    tonDau = NumberFilter(field_name='ct_bcton__TonDau')
    tonCuoi = NumberFilter(field_name='ct_bcton__TonCuoi')

    class Meta:
        model = BaoCaoTon
        fields = ['Thang', 'ct_bcton__MaSach__MaSach', 'ct_bcton__MaSach__MaDauSach__TenSach', 'ct_bcton__TonDau', 'ct_bcton__TonCuoi']

class BaoCaoTonViewSet(viewsets.ModelViewSet):
    queryset = BaoCaoTon.objects.all()
    serializer_class = BaoCaoTonSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BaoCaoTonFilter

# BaoCaoCongNo filterset
class BaoCaoCongNoFilter(FilterSet):
    thang = DateFilter(field_name='Thang', lookup_expr='month')
    maKH = NumberFilter(field_name='ct_bccongno__MaKH__MaKhachHang')
    tenKH = CharFilter(field_name='ct_bccongno__MaKH__HoTen', lookup_expr='icontains')
    noDau = NumberFilter(field_name='ct_bccongno__NoDau')
    noCuoi = NumberFilter(field_name='ct_bccongno__NoCuoi')

    class Meta:
        model = BaoCaoCongNo
        fields = ['Thang', 'ct_bccongno__MaKH__MaKhachHang', 'ct_bccongno__MaKH__HoTen', 'ct_bccongno__NoDau', 'ct_bccongno__NoCuoi']
        
class BaoCaoCongNoViewSet(viewsets.ModelViewSet):
    queryset = BaoCaoCongNo.objects.all()
    serializer_class = BaoCaoCongNoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BaoCaoCongNoFilter    

# HoaDon filterset
class HoaDonFilter(FilterSet):
    maHD = NumberFilter(field_name='MaHD')
    ngayLap = DateFilter(field_name='NgayLap')
    maKH = NumberFilter(field_name='MaKH__MaKhachHang')
    tenKH = CharFilter(field_name='MaKH__HoTen', lookup_expr='icontains')
    # status is not a field in HoaDon, so skip it

    class Meta:
        model = HoaDon
        fields = ['MaHD', 'NgayLap', 'MaKH__MaKhachHang', 'MaKH__HoTen']
# HoaDon: Nguoilaphd (full), Nguoithu (view), Quanli (all)
class HoaDonViewSet(viewsets.ModelViewSet):
    queryset = HoaDon.objects.all()
    serializer_class = HoaDonSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = HoaDonFilter