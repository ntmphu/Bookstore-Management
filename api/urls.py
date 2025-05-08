from rest_framework import routers
from .views import (
    KhachHangViewSet, SachViewSet, HoaDonViewSet, CTHoaDonViewSet, PhieuThuTienViewSet,
    DauSachViewSet, TacGiaViewSet, TheLoaiViewSet,
    PhieuNhapSachViewSet, CTNhapSachViewSet,
    BaoCaoTonViewSet, CTBCTonViewSet, BaoCaoCongNoViewSet, CTBCCongNoViewSet, ThamSoViewSet,
    UserManagementViewSet, GroupModelPermissionViewSet,
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
router.register(r'user', UserManagementViewSet, basename='user')
router.register(r'groupmodelpermission', GroupModelPermissionViewSet)
urlpatterns = router.urls