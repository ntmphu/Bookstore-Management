from rest_framework import serializers
from .models import (
    TheLoai, DauSach, TacGia, DauSach_TacGia, Sach, KhachHang,
    PhieuNhapSach, CT_NhapSach, HoaDon, CT_HoaDon, PhieuThuTien,
    BaoCaoTon, CT_BCTon, BaoCaoCongNo, CT_BCCongNo, ThamSo
)

class TheLoaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheLoai
        fields = '__all__'

class DauSachSerializer(serializers.ModelSerializer):
    class Meta:
        model = DauSach
        fields = '__all__'

class TacGiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacGia
        fields = '__all__'

class DauSachTacGiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DauSach_TacGia
        fields = '__all__'

class SachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sach
        fields = '__all__'

class KhachHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhachHang
        fields = '__all__'

class PhieuNhapSachSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhieuNhapSach
        fields = '__all__'

class CTNhapSachSerializer(serializers.ModelSerializer):
    class Meta:
        model = CT_NhapSach
        fields = '__all__'

class HoaDonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoaDon
        fields = '__all__'

class CTHoaDonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CT_HoaDon
        fields = '__all__'

class PhieuThuTienSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhieuThuTien
        fields = '__all__'

class BaoCaoTonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaoCaoTon
        fields = '__all__'

class CTBCTonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CT_BCTon
        fields = '__all__'

class BaoCaoCongNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaoCaoCongNo
        fields = '__all__'

class CTBCCongNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CT_BCCongNo
        fields = '__all__'

class ThamSoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThamSo
        fields = '__all__'