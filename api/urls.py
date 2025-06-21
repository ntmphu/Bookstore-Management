from rest_framework import routers
from django.urls import path, include
from .views import (
    KhachHangViewSet, SachViewSet, HoaDonViewSet, CTHoaDonViewSet, PhieuThuTienViewSet,
    DauSachViewSet, TacGiaViewSet, TheLoaiViewSet, NXBViewSet,
    PhieuNhapSachViewSet, CTNhapSachViewSet,
    BaoCaoTonViewSet, CTBCTonViewSet, BaoCaoCongNoViewSet, CTBCCongNoViewSet, ThamSoViewSet,
    UserManagementViewSet, bcton_excel, bccno_excel, GroupViewSet
)

router = routers.DefaultRouter()
router.register(r'khachhang', KhachHangViewSet)
router.register(r'sach', SachViewSet)
router.register(r'hoadon', HoaDonViewSet)
router.register(r'cthoadon', CTHoaDonViewSet)
router.register(r'phieuthutien', PhieuThuTienViewSet)
router.register(r'dausach', DauSachViewSet)
router.register(r'tacgia', TacGiaViewSet)
router.register(r'theloai', TheLoaiViewSet)
router.register(r'phieunhapsach', PhieuNhapSachViewSet)
router.register(r'ctnhapsach', CTNhapSachViewSet)
router.register(r'baocaoton', BaoCaoTonViewSet)
router.register(r'ctbcton', CTBCTonViewSet)
router.register(r'baocaocongno', BaoCaoCongNoViewSet)
router.register(r'ctbccongno', CTBCCongNoViewSet)
router.register(r'thamso', ThamSoViewSet)
router.register(r'nxb', NXBViewSet)
router.register(r'user', UserManagementViewSet, basename='user')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),  # include all ViewSet routes
    path('baocaoton/<int:bcton_id>/excel/', bcton_excel, name='baocaoton-excel'),
    path('baocaocongno/<int:bccno_id>/excel/', bccno_excel, name='baocaocongno-excel'),
]