from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TheLoai)
admin.site.register(DauSach)
admin.site.register(TacGia)
admin.site.register(Sach)
admin.site.register(KhachHang)
admin.site.register(PhieuNhapSach)
admin.site.register(CT_NhapSach)
admin.site.register(HoaDon)
admin.site.register(CT_HoaDon)
admin.site.register(PhieuThuTien)
admin.site.register(BaoCaoTon)
admin.site.register(CT_BCTon)
admin.site.register(BaoCaoCongNo)
admin.site.register(CT_BCCongNo)
admin.site.register(ThamSo)
admin.site.register(UserProfile)

@admin.register(GroupModelPermission)
class GroupModelPermissionAdmin(admin.ModelAdmin):
    list_display = ('group', 'model_name', 'can_view', 'can_add', 'can_change', 'can_delete')
    list_filter = ('group', 'model_name')