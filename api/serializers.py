from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    TheLoai, DauSach, TacGia, Sach, KhachHang,
    PhieuNhapSach, CT_NhapSach, HoaDon, CT_HoaDon, PhieuThuTien,
    BaoCaoTon, CT_BCTon, BaoCaoCongNo, CT_BCCongNo, ThamSo,
    GroupModelPermission, UserProfile
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

class CTBCTonSerializer(serializers.ModelSerializer):
    MaSach = SachSerializer()  # Nested serializer for Sach details
    
    class Meta:
        model = CT_BCTon
        fields = ['MaSach', 'TonDau', 'PhatSinh', 'TonCuoi']

class BaoCaoTonSerializer(serializers.ModelSerializer):
    chitiet = serializers.SerializerMethodField()

    class Meta:
        model = BaoCaoTon
        fields = ['MaBCTon', 'Thang', 'Nam', 'chitiet']

    def get_chitiet(self, obj):
        ct_bcton = CT_BCTon.objects.filter(MaBCTon=obj)
        return CTBCTonSerializer(ct_bcton, many=True).data
    
class CTBCCongNoSerializer(serializers.ModelSerializer):
    MaKH = KhachHangSerializer()  # Nested serializer for KhachHang details
    
    class Meta:
        model = CT_BCCongNo
        fields = ['MaKH', 'NoDau', 'PhatSinh', 'NoCuoi']

class BaoCaoCongNoSerializer(serializers.ModelSerializer):
    chitiet = serializers.SerializerMethodField()

    class Meta:
        model = BaoCaoCongNo
        fields = ['MaBCCN', 'Thang', 'Nam', 'chitiet']

    def get_chitiet(self, obj):
        ct_bccongno = CT_BCCongNo.objects.filter(MaBCCN=obj)
        return CTBCCongNoSerializer(ct_bccongno, many=True).data
    
class ThamSoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThamSo
        fields = '__all__'
    
VALID_GROUPS = ['NguoiNhap', 'ThuNgan']
class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['gioiTinh']

class UserSerializer(serializers.ModelSerializer):
    gioiTinh = serializers.CharField(source='profile.gioiTinh', required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'gioiTinh']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        if profile_data and 'gioiTinh' in profile_data:
            instance.profile.gioiTinh = profile_data['gioiTinh']
            instance.profile.save()
        return super().update(instance, validated_data)

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=VALID_GROUPS, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class GroupModelPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModelPermission
        fields = '__all__'