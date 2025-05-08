from rest_framework import viewsets, permissions
from .models import (
    KhachHang, Sach, HoaDon, CT_HoaDon, PhieuThuTien,
    DauSach, TacGia, TheLoai, 
    PhieuNhapSach, CT_NhapSach,
    BaoCaoTon, CT_BCTon, BaoCaoCongNo, CT_BCCongNo, ThamSo, GroupModelPermission 
)
from .serializers import (
    KhachHangSerializer, SachSerializer, HoaDonSerializer, CTHoaDonSerializer, PhieuThuTienSerializer,
    DauSachSerializer, TacGiaSerializer, TheLoaiSerializer, 
    PhieuNhapSachSerializer, CTNhapSachSerializer,
    BaoCaoTonSerializer, CTBCTonSerializer, BaoCaoCongNoSerializer, CTBCCongNoSerializer, ThamSoSerializer,
    GroupModelPermissionSerializer
)

from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, CreateUserSerializer
VALID_GROUPS = ['NguoiNhap', 'ThuNgan']
class DynamicModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        model_name = view.queryset.model._meta.model_name
        user_groups = request.user.groups.all()
        
        group_perms = GroupModelPermission.objects.filter(
            group__in=user_groups,
            model_name=model_name
        )

        if request.method in permissions.SAFE_METHODS:
            return group_perms.filter(can_view=True).exists()
        elif request.method == 'POST':
            return group_perms.filter(can_add=True).exists()
        elif request.method in ['PUT', 'PATCH']:
            return group_perms.filter(can_change=True).exists()
        elif request.method == 'DELETE':
            return group_perms.filter(can_delete=True).exists()


class UserManagementViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DynamicModelPermission]

    @action(detail=False, methods=['post'])
    def create_staff(self, request):
        if not request.user.groups.filter(name='quanli').exists():
            return Response(
                {"error": "Only managers can create staff accounts"}, 
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            group_name = request.data.get('role')
            if group_name in VALID_GROUPS:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        if user != request.user and not request.user.groups.filter(name='quanli').exists():
            return Response(
                {"error": "You don't have permission to change this password"},
                status=status.HTTP_403_FORBIDDEN
            )
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
        if user != request.user and not request.user.groups.filter(name='quanli').exists():
            return Response(
                {"error": "You can only update your own profile"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        if not request.user.groups.filter(name='quanli').exists():
            return Response(
                {"error": "Only managers can deactivate users"}, 
                status=status.HTTP_403_FORBIDDEN
            )
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({"status": "user deactivated"})
class GroupModelPermissionViewSet(viewsets.ModelViewSet):
    queryset = GroupModelPermission.objects.all()
    serializer_class = GroupModelPermissionSerializer
    permission_classes = [permissions.IsAdminUser]  # Only allow admin/Quanli to manage
# Use in viewsets
class KhachHangViewSet(viewsets.ModelViewSet):
    queryset = KhachHang.objects.all()
    serializer_class = KhachHangSerializer
    permission_classes = [DynamicModelPermission]


# Sach: Nguoilaphd (view), Nguoi nhap (full), Quanli (all)
class SachViewSet(viewsets.ModelViewSet):
    queryset = Sach.objects.all()
    serializer_class = SachSerializer
    permission_classes = [DynamicModelPermission]

# HoaDon: Nguoilaphd (full), Nguoithu (view), Quanli (all)
class HoaDonViewSet(viewsets.ModelViewSet):
    queryset = HoaDon.objects.all()
    serializer_class = HoaDonSerializer

    permission_classes = [DynamicModelPermission]

# CT_HoaDon: Nguoilaphd (full), Quanli (all)
class CTHoaDonViewSet(viewsets.ModelViewSet):
    queryset = CT_HoaDon.objects.all()
    serializer_class = CTHoaDonSerializer

    permission_classes = [DynamicModelPermission]

# PhieuThuTien: Nguoithu (full), Quanli (all)
class PhieuThuTienViewSet(viewsets.ModelViewSet):
    queryset = PhieuThuTien.objects.all()
    serializer_class = PhieuThuTienSerializer

    permission_classes = [DynamicModelPermission]
# DauSach: Nguoi nhap (full), Quanli (all)
class DauSachViewSet(viewsets.ModelViewSet):
    queryset = DauSach.objects.all()
    serializer_class = DauSachSerializer
    permission_classes = [DynamicModelPermission]

# TacGia: Nguoi nhap (full), Quanli (all)
class TacGiaViewSet(viewsets.ModelViewSet):
    queryset = TacGia.objects.all()
    serializer_class = TacGiaSerializer
    permission_classes = [DynamicModelPermission]

# TheLoai: Nguoi nhap (full), Quanli (all)
class TheLoaiViewSet(viewsets.ModelViewSet):
    queryset = TheLoai.objects.all()
    serializer_class = TheLoaiSerializer
    permission_classes = [DynamicModelPermission]


# PhieuNhapSach: Nguoi nhap (full), Quanli (all)
class PhieuNhapSachViewSet(viewsets.ModelViewSet):
    queryset = PhieuNhapSach.objects.all()
    serializer_class = PhieuNhapSachSerializer

    permission_classes = [DynamicModelPermission]

# CT_NhapSach: Nguoi nhap (full), Quanli (all)
class CTNhapSachViewSet(viewsets.ModelViewSet):
    queryset = CT_NhapSach.objects.all()
    serializer_class = CTNhapSachSerializer

    permission_classes = [DynamicModelPermission]
class BaoCaoTonViewSet(viewsets.ModelViewSet):
    queryset = BaoCaoTon.objects.all()
    serializer_class = BaoCaoTonSerializer
    permission_classes = [DynamicModelPermission]

class CTBCTonViewSet(viewsets.ModelViewSet):
    queryset = CT_BCTon.objects.all()
    serializer_class = CTBCTonSerializer
    permission_classes = [DynamicModelPermission]

class BaoCaoCongNoViewSet(viewsets.ModelViewSet):
    queryset = BaoCaoCongNo.objects.all()
    serializer_class = BaoCaoCongNoSerializer
    permission_classes = [DynamicModelPermission]

class CTBCCongNoViewSet(viewsets.ModelViewSet):
    queryset = CT_BCCongNo.objects.all()
    serializer_class = CTBCCongNoSerializer
    permission_classes = [DynamicModelPermission]

class ThamSoViewSet(viewsets.ModelViewSet):
    queryset = ThamSo.objects.all()
    serializer_class = ThamSoSerializer
    permission_classes = [DynamicModelPermission]