from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import (
    TheLoai, DauSach, TacGia, Sach, KhachHang,
    PhieuNhapSach, CT_NhapSach, HoaDon, CT_HoaDon, PhieuThuTien,
    BaoCaoTon, CT_BCTon, BaoCaoCongNo, CT_BCCongNo, ThamSo, NXB, 
    UserProfile
)
from datetime import date
class UserProfile():
    serializers.ModelSerializer

class TheLoaiSerializer(serializers.ModelSerializer):
    MaTheLoai = serializers.SerializerMethodField()

    class Meta:
        model = TheLoai
        fields = ['MaTheLoai', 'TenTheLoai']

    def get_MaTheLoai(self, obj):
        return f"TL{obj.MaTheLoai:03d}"

class DauSachSerializer(serializers.ModelSerializer):
    MaDauSach = serializers.SerializerMethodField()

    # Write-only fields for input
    TenTheLoai_input = serializers.CharField(write_only=True, required=False)
    TenTacGia_input = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )

    # Read-only display fields
    TenTheLoai = serializers.SerializerMethodField()
    TenTacGia = serializers.SerializerMethodField()

    class Meta:
        model = DauSach
        fields = [
            'MaDauSach',
            'TenSach',
            'TenTheLoai_input',
            'TenTacGia_input',
            'TenTheLoai',
            'TenTacGia',
        ]

    def get_MaDauSach(self, obj):
        return f"DS{obj.MaDauSach:03d}"

    def get_TenTheLoai(self, obj):
        return obj.MaTheLoai.TenTheLoai if obj.MaTheLoai else None

    def get_TenTacGia(self, obj):
        return [tg.TenTG for tg in obj.MaTG.all()]

    def validate(self, data):
        ten_theloai = data.get("TenTheLoai_input", None)
        ten_tacgia_list = data.get("TenTacGia_input", [])
        try:
            theloai_obj = TheLoai.objects.get(TenTheLoai=ten_theloai)
        except TheLoai.DoesNotExist:
            raise serializers.ValidationError({
                'TenTheLoai_input': f"Không tồn tại tên thể loại '{ten_theloai}'. Vui lòng thêm mới thể loại."
            })
        
        tacgia_objs = []
        missing_tacgia = []
        for ten_tg in ten_tacgia_list:
            try:
                tg_obj = TacGia.objects.get(TenTG=ten_tg)
                tacgia_objs.append(tg_obj)
            except TacGia.DoesNotExist:
                missing_tacgia.append(ten_tg)

        if missing_tacgia:
            raise serializers.ValidationError({
                'TenTacGia_input': f"Không tồn tại tác giả: {[name for name in missing_tacgia]}. Vui lòng thêm mới tác giả."
            })

        data["_resolved_theloai"] = theloai_obj
        data["_resolved_tacgia"] = tacgia_objs
        return data

    def create(self, validated_data):
        theloai_obj = validated_data.pop("_resolved_theloai")
        tacgia_objs = validated_data.pop("_resolved_tacgia")

        # Remove input fields
        validated_data.pop("TenTheLoai_input", None)
        validated_data.pop("TenTacGia_input", [])

        dausach = DauSach.objects.create(
            MaTheLoai=theloai_obj,
            **validated_data
        )
        dausach.MaTG.set(tacgia_objs)
        return dausach
    
    def update(self, instance, validated_data):
        theloai_obj = validated_data.pop("_resolved_theloai")
        tacgia_objs = validated_data.pop("_resolved_tacgia")
        validated_data.pop("TenTheLoai_input", None)
        validated_data.pop("TenTacGia_input", [])
        tensach = validated_data.get("TenSach")
        instance.TenSach = tensach
        instance.MaTheLoai = theloai_obj
        instance.MaTG.set(tacgia_objs)
        instance.save()
        return instance

class TacGiaSerializer(serializers.ModelSerializer):
    MaTG = serializers.SerializerMethodField()

    class Meta:
        model = TacGia
        fields = ['MaTG', 'TenTG']

    def get_MaTG(self, obj):
        return f"TL{obj.MaTG:03d}"

class NXBSerializer(serializers.ModelSerializer):
    MaNXB = serializers.SerializerMethodField()

    class Meta:
        model = NXB
        fields = ['MaNXB', 'TenNXB']

    def get_MaNXB(self, obj):
        return f"NXB{obj.MaNXB:03d}"

class SachSerializer(serializers.ModelSerializer):
    MaSach = serializers.SerializerMethodField()
    TenDauSach_input = serializers.CharField(write_only=True, required=False)  # Changed to not required for updates
    TenDauSach = serializers.SerializerMethodField()
    TenNXB_input = serializers.CharField(write_only=True, required=False)  # Changed to not required for updates
    TenNXB = serializers.SerializerMethodField()
    MaDauSach = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Sach
        fields = ['MaSach', 'MaDauSach', 'TenDauSach_input', 'TenDauSach', 'TenNXB', 'TenNXB_input', 'NamXB', 'SLTon']
        read_only_fields = ['SLTon']

    def get_MaSach(self, obj):
        return f"S{obj.MaSach:03d}"

    def get_MaDauSach(self, obj):
        return f"DS{obj.MaDauSach.MaDauSach:03d}"

    def get_TenDauSach(self, obj):
        return obj.MaDauSach.TenSach

    def get_TenNXB(self, obj):
        return obj.NXB.TenNXB

    def create(self, validated_data):
        ten_dausach = validated_data.pop('TenDauSach_input', None)
        ten_nxb = validated_data.pop('TenNXB_input', None)

        if not ten_dausach:
            raise serializers.ValidationError({"TenDauSach_input": "Phải nhập tên đầu sách."})
        
        if not ten_nxb:
            raise serializers.ValidationError({"TenNXB_input": "Phải nhập tên nhà xuất bản."})

        # Validate existence of DauSach
        try:
            dausach = DauSach.objects.get(TenSach=ten_dausach)
        except DauSach.DoesNotExist:
            raise serializers.ValidationError({
                'TenDauSach_input': f"Không tồn tại đầu sách '{ten_dausach}'. Vui lòng thêm mới đầu sách."
            })
        
        try:
            nxb = NXB.objects.get(TenNXB=ten_nxb)
        except NXB.DoesNotExist:
            raise serializers.ValidationError({
                'TenNXB_input': f"Không tồn tại tên NXB '{ten_nxb}'. Vui lòng thêm mới nhà xuất bản."
            })

        # Create the Sach object
        sach = Sach.objects.create(MaDauSach=dausach, NXB=nxb, **validated_data)
        return sach

    def update(self, instance, validated_data):
        ten_nxb = validated_data.pop('TenNXB_input', None)
        nam_xb = validated_data.get('NamXB', instance.NamXB)

        # Validate NamXB
        from datetime import datetime
        current_year = datetime.now().year
        if nam_xb < 1900 or nam_xb > current_year:
            raise serializers.ValidationError({
                'NamXB': f"Năm xuất bản phải từ 1900 đến {current_year}"
            })

        # Update NXB if provided
        if ten_nxb:
            try:
                nxb = NXB.objects.get(TenNXB=ten_nxb)
                instance.NXB = nxb
            except NXB.DoesNotExist:
                raise serializers.ValidationError({
                    'TenNXB_input': f"Không tồn tại nhà xuất bản '{ten_nxb}'. Vui lòng thêm mới nhà xuất bản."
                })

        # Update NamXB
        instance.NamXB = nam_xb
        instance.save()
        return instance

class KhachHangSerializer(serializers.ModelSerializer):
    MaKhachHang = serializers.SerializerMethodField()

    class Meta:
        model = KhachHang
        fields = ['MaKhachHang', 'HoTen', 'DiaChi', 'DienThoai', 'Email', 'SoTienNo']
        read_only_fields = ['SoTienNo']

    def get_MaKhachHang(self, obj):
        return f"KH{obj.MaKhachHang:03d}"
    
    def create(self, validated_data):
        # Validate unique DienThoai
        if KhachHang.objects.filter(DienThoai=validated_data['DienThoai']).exists():
            raise serializers.ValidationError({
                'DienThoai': f"Số điện thoại '{validated_data['DienThoai']}' đã tồn tại. Vui lòng nhập số điện thoại khác."
            })

        # Create the KhachHang object
        khachhang = KhachHang.objects.create(**validated_data)
        return khachhang

class PhieuNhapSachSerializer(serializers.ModelSerializer):
    MaPhieuNhap = serializers.SerializerMethodField()
    NguoiNhap = serializers.SerializerMethodField()
    # username = serializers.CharField(write_only=True, required=True)
    NguoiNhap_input = serializers.CharField(write_only=True, required=True)
    NgayNhap = serializers.DateField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"], required=True)
    
    class Meta:
        model = PhieuNhapSach
        fields = ['MaPhieuNhap', 'NgayNhap', 'NguoiNhap', 'NguoiNhap_input']    

    def get_MaPhieuNhap(self, obj):
        return f"PN{obj.MaPhieuNhap:03d}"
    
    def get_NguoiNhap(self, obj):
        return f'{obj.NguoiNhap.last_name} {obj.NguoiNhap.first_name}'
    
    def create(self, validated_data):
        # username = validated_data.pop('username', None)
        manv = validated_data.pop('NguoiNhap_input', None)
        
        if not manv:
            raise serializers.ValidationError({"manv": "Phải nhập tên người dùng."})

        # Validate existence of User
        try:
            manv = int(manv.replace('NV', ''))
            user = User.objects.get(id=manv)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'NguoiNhap_input': f"Không tồn tại mã người dùng '{manv}'. Vui lòng nhập đúng tên người dùng."
            })

        # Create the PhieuNhapSach object
        phieunhapsach = PhieuNhapSach.objects.create(NguoiNhap=user, **validated_data)
        return phieunhapsach

class CTNhapSachSerializer(serializers.ModelSerializer):
    MaPhieuNhap_input = serializers.CharField(write_only=True, required=True)
    MaSach_input = serializers.CharField(write_only=True, required=True)
    SLNhap = serializers.IntegerField(required=True)
    GiaNhap = serializers.DecimalField(max_digits=15, decimal_places=0, required=True)
    
    MaCT_NhapSach = serializers.SerializerMethodField()
    MaPhieuNhap = serializers.SerializerMethodField()
    MaSach = serializers.SerializerMethodField()
    TenSach = serializers.CharField(source='MaSach.MaDauSach.TenSach', read_only=True)

    class Meta:
        model = CT_NhapSach
        fields = ['MaCT_NhapSach', 'MaPhieuNhap_input', 'MaSach_input', 'MaPhieuNhap', 'MaSach', 'TenSach', 'SLNhap', 'GiaNhap']

    def validate_SLNhap(self, value):
        if value <= 0:
            raise serializers.ValidationError("SLNhap: Số lượng nhập phải lớn hơn 0.")
        return value

    def validate(self, data):
        thamso = ThamSo.objects.first()
        if not thamso:
            raise serializers.ValidationError("Tham số hệ thống chưa được cấu hình.")

        sl_nhap = data.get("SLNhap")
        ma_sach_input = data.get("MaSach_input")
        ma_phieu_nhap_input = data.get("MaPhieuNhap_input")
        
        # Validate required fields
        if not ma_phieu_nhap_input:
            raise serializers.ValidationError({"MaPhieuNhap_input": "Phải nhập mã phiếu nhập."})
        
        if not ma_sach_input:
            raise serializers.ValidationError({"MaSach_input": "Phải nhập mã sách."})
        
        if not sl_nhap:
            raise serializers.ValidationError({"SLNhap": "Phải nhập số lượng nhập."})

        if not ma_phieu_nhap_input:
            raise serializers.ValidationError({"MaPhieuNhap_input": "Phải nhập mã phiếu nhập."})
        
        try:    
            ma_phieu_nhap = int(ma_phieu_nhap_input.replace('PN', ''))
            phieunhapsach = PhieuNhapSach.objects.get(MaPhieuNhap=ma_phieu_nhap)
        except (ValueError, PhieuNhapSach.DoesNotExist):
            raise serializers.ValidationError({
                'MaPhieuNhap_input': f"Không tồn tại mã phiếu nhập '{ma_phieu_nhap_input}'. Vui lòng nhập đúng mã phiếu nhập."
            })

        try:
            ma_sach = int(ma_sach_input.replace('S', ''))
            sach = Sach.objects.get(MaSach=ma_sach)
        except (ValueError, Sach.DoesNotExist):
            raise serializers.ValidationError({
                'MaSach_input': f"Không tồn tại mã sách '{ma_sach_input}'. Vui lòng nhập đúng mã sách."
            })

        if sl_nhap < thamso.SLNhapTT:
            raise serializers.ValidationError({
                "SLNhap": f"Số lượng nhập phải ≥ {thamso.SLNhapTT}."
            })

        current_slton = sach.SLTon
        # update case
        if self.instance:
            old_sln = self.instance.SLNhap
            diff = sl_nhap - old_sln
            if diff > 0:
                if current_slton > thamso.TonTD:
                    raise serializers.ValidationError({
                        "MaSach_input, SLNhap": f"Tồn của sách {sach.MaSach}: {sach.MaDauSach.TenSach}, vượt quá tồn tối đa ({thamso.TonTD})."
                    })
            else: 
                new_slton = current_slton + diff
                if new_slton < 0:
                    raise serializers.ValidationError({
                        "MaSach_input, SLNhap": f"Tồn của sách {sach.MaSach}: {sach.MaDauSach.TenSach} phải là số dương."
                    })
        # create case
        else:
            current_slton = sach.SLTon
            if current_slton > thamso.TonTD:
                raise serializers.ValidationError({
                    "MaSach_input, SLNhap": f"Tồn của sách {sach.MaSach}: {sach.MaDauSach.TenSach}, vượt quá tồn tối đa ({thamso.TonTD})."
                })

        # Temporarily attach sach for use in create()
        data['MaPhieuNhap'] = phieunhapsach
        data['MaSach'] = sach
        return data

    def get_MaCT_NhapSach(self, obj):
        return f"CTNS{obj.id:03d}"

    def get_MaPhieuNhap(self, obj):
        return f"PN{obj.MaPhieuNhap.MaPhieuNhap:03d}"
    
    def get_MaSach(self, obj):
        return f"S{obj.MaSach.MaSach:03d}"
    
    def create(self, validated_data):
        # These fields were added during validation
        validated_data.pop('MaPhieuNhap_input', None)
        validated_data.pop('MaSach_input', None)

        return CT_NhapSach.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.SLNhap = validated_data.get('SLNhap', instance.SLNhap)
        instance.GiaNhap = validated_data.get('GiaNhap', instance.GiaNhap)
        # Update any other fields that exist in the CT_NhapSach model
        instance.save()
        return instance

class CTHoaDonSerializer(serializers.ModelSerializer):
    MaHD_input = serializers.CharField(write_only=True, required=True)
    MaSach_input = serializers.CharField(write_only=True, required=True)
    TenSach = serializers.CharField(source='MaSach.MaDauSach.TenSach', read_only=True)

    id = serializers.SerializerMethodField()
    MaHD = serializers.SerializerMethodField()
    MaSach = serializers.SerializerMethodField()
    GiaBan = serializers.DecimalField(max_digits=15, decimal_places=0, read_only=True)
    ThanhTien = serializers.DecimalField(max_digits=15, decimal_places=0, read_only=True)
    SLBan = serializers.IntegerField(required=True)

    class Meta:
        model = CT_HoaDon
        fields = ['id', 'MaHD', 'MaHD_input', 'MaSach', 'MaSach_input', 'TenSach', 'SLBan', 'GiaBan', 'ThanhTien']
        read_only_fields = ['GiaBan', 'ThanhTien']

    def get_id(self, obj):
        return f"CTHD{obj.id:03d}"

    def get_MaHD(self, obj):
        return f"HD{obj.MaHD.MaHD:03d}"
    
    def get_MaSach(self, obj):
        return f"S{obj.MaSach.MaSach:03d}"

    def validate_SLBan(self, value):
        if value <= 0:
            raise serializers.ValidationError("Số lượng bán phải lớn hơn 0.")
        return value

    def validate(self, data):
        ma_hd_input = data.get('MaHD_input')
        
        if not ma_hd_input:
            raise serializers.ValidationError({"MaHD_input": "Mã hóa đơn là bắt buộc."})
        
        ma_sach_input = data.get('MaSach_input')
        if not ma_sach_input:
            raise serializers.ValidationError({"MaSach_input": "Mã sách là bắt buộc."})

        try:
            ma_hd = int(ma_hd_input.replace('HD', ''))
            hoadon = HoaDon.objects.get(MaHD=ma_hd)
        except (ValueError, HoaDon.DoesNotExist):
            raise serializers.ValidationError({"MaHD_input": f"Mã hóa đơn HD{ma_hd:03d} không tồn tại."})

        try:
            ma_sach = int(ma_sach_input.replace('S', ''))
            sach = Sach.objects.get(MaSach=ma_sach)
        except (ValueError, Sach.DoesNotExist):
            raise serializers.ValidationError({"MaSach_input": f"Mã sách S{ma_sach:03d} không tồn tại."})

        thamso = ThamSo.objects.first()
        if not thamso:
            raise serializers.ValidationError("Tham số hệ thống chưa được cấu hình.")

        latest_pn = PhieuNhapSach.objects.filter(MaSach=sach).order_by('-NgayNhap').first()

        if not latest_pn:
            raise serializers.ValidationError("Không tìm thấy giá nhập cho sách này.")

        slban = data.get('SLBan')

        # update case
        if self.instance:
            old_slban = self.instance.SLBan
            diff = slban - old_slban
        # create case
        else:
            diff = slban

        new_slton = sach.SLTon - diff

        if new_slton < thamso.TonTT:
            raise serializers.ValidationError({
                "MaSach_input, SLBan": f"Số lượng tồn sau khi bán ({new_slton}) nhỏ hơn số lượng tồn tối thiểu ({thamso.TonTT})."
            })
        
        if new_slton < 0:
            raise serializers.ValidationError({
                "MaSach_input, SLBan": f"Số lượng sách không đủ để bán (số lượng hiện tại: {sach.SLTon})."
            })

        gianhap = (
            CT_NhapSach.objects
            .filter(MaSach=sach)
            .order_by('-MaPhieuNhap__NgayNhap')
            .first()
        )

        giaban = int(gianhap.GiaNhap * thamso.TiLe)
        data['MaHD'] = hoadon
        data['MaSach'] = sach
        data['GiaBan'] = giaban
        data['ThanhTien'] = giaban * slban
        return data

    def create(self, validated_data):
        validated_data.pop('MaHD_input', None)
        validated_data.pop('MaSach_input', None)
        return CT_HoaDon.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     # Update fields
    #     instance.SLBan = validated_data.get('SLBan', instance.SLBan)
    #     thamso = ThamSo.objects.first()
        
    #     gianhap = (
    #         CT_NhapSach.objects
    #         .filter(MaSach=instance.MaSach)
    #         .order_by('-MaPhieuNhap__NgayNhap')
    #         .first()
    #     )

    #     instance.GiaBan = gianhap.GiaNhap * thamso.TiLe
    #     instance.ThanhTien = instance.GiaBan * instance.SLBan
    #     instance.save()

    #     # Cập nhật hóa đơn
    #     return instance
    
class HoaDonSerializer(serializers.ModelSerializer):
    NgayLap = serializers.DateField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"], required=True)
    NguoiLapHD_input = serializers.CharField(write_only=True, required=True)
    MaKH_input = serializers.CharField(write_only=True, required=True)
    SoTienTra = serializers.DecimalField(max_digits=15, decimal_places=0, required=False)
    MaHD = serializers.SerializerMethodField()
    MaKH = serializers.SerializerMethodField()
    HoTen = serializers.CharField(source='MaKH.HoTen', read_only=True)
    NguoiLapHD = serializers.SerializerMethodField()
    # TongTien = serializers.SerializerMethodField()
    # ConLai = serializers.SerializerMethodField()

    class Meta:
        model = HoaDon
        fields = [
            'MaHD', 'MaKH', 'MaKH_input', 'HoTen', 'NgayLap', 'NguoiLapHD_input', 'NguoiLapHD',
            'SoTienTra', 'TongTien', 'ConLai'
        ]
        read_only_fields = ['TongTien', 'ConLai']

    def get_MaHD(self, obj):
        return f"HD{obj.MaHD:03d}"

    def get_MaKH(self, obj):
        return f"KH{obj.MaKH.MaKhachHang:03d}"
    
    def get_NguoiLapHD(self, obj):
        return f'NV{obj.NguoiLapHD.id:03d}'
    
    # def get_TongTien(self, obj):
    #     return obj.TongTien
    
    # def get_ConLai(self, obj):
    #     return obj.ConLai

    def validate_SoTienTra(self, value):
        if value < 0:
            raise serializers.ValidationError("Số tiền trả không được âm.")
        return value
    
    def update(self, instance, validated_data):
        validated_data.pop('MaKH_input', None)
        validated_data.pop('NguoiLapHD_input', None)
        sotientra = validated_data.get("SoTienTra", None)
        # 
        if sotientra is None:
            for field in ['MaKH', 'NguoiLapHD']:
                setattr(instance, field, validated_data.get(field))
        # update new sotientra
        else:
            if sotientra > instance.TongTien:
                raise serializers.ValidationError({
                    'SoTienTra': f"Số tiền trả ({sotientra}) không được vượt quá tổng tiền ({instance.TongTien})."
                })
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
        instance.save()
        return instance
    
    def validate(self, data):
        ma_kh_input = data.get('MaKH_input')
        manv = data.get('NguoiLapHD_input')
        # Validate required fields       
        if not ma_kh_input:
            raise serializers.ValidationError({"MaKH_input": "Phải nhập mã khách hàng."})
        
        if not manv:
            raise serializers.ValidationError({"NguoiLapHD_input": "Phải nhập người lập hóa đơn."})

        try:
            ma_kh = int(ma_kh_input.replace('KH', ''))
            khachhang = KhachHang.objects.get(MaKhachHang=ma_kh)
        except (ValueError, KhachHang.DoesNotExist):
            raise serializers.ValidationError({
                'MaKH_input': f"Không tồn tại mã khách hàng '{ma_kh_input}'. Vui lòng nhập đúng mã khách hàng."
            })

        try:
            manv = int(manv.replace('NV', ''))
            user = User.objects.get(id=manv)
        except User.DoesNotExist:
            raise serializers.ValidationError({"NguoiLapHD_input": f"Không tồn tại người dùng '{manv}'."})

        data['NguoiLapHD'] = user
        data['MaKH'] = khachhang
        return data
    
    def create(self, validated_data):
        # These fields were added during validation
        validated_data.pop('MaKH_input', None)
        validated_data.pop('NguoiLapHD_input', None)

        thamso = ThamSo.objects.first()
        khachhang = validated_data.get('MaKH')
        sotienno = khachhang.SoTienNo
        
        if sotienno > thamso.NoTD:
            raise serializers.ValidationError({
                'MaKH_input': f"Khách hàng KH{khachhang.MaKhachHang:03d}: {khachhang.HoTen} nợ quá số tiền nợ tối đa ({thamso.NoTD}). Nợ hiện tại: {khachhang.SoTienNo}."
            })

        return HoaDon.objects.create(**validated_data)
    
class PhieuThuTienSerializer(serializers.ModelSerializer):
    NguoiThu_input = serializers.CharField(write_only=True, required=True)
    NgayThu = serializers.DateField(format="%d/%m/%Y", input_formats=["%d/%m/%Y"], required=True)
    MaKH_input = serializers.CharField(write_only=True, required=True)
    SoTienThu = serializers.DecimalField(max_digits=15, decimal_places=0, required=True)

    MaKH = serializers.SerializerMethodField()
    MaPhieuThu = serializers.SerializerMethodField()
    TenKH = serializers.CharField(source='MaKH.HoTen', read_only=True)
    NguoiThu = serializers.SerializerMethodField()

    class Meta:
        model = PhieuThuTien
        fields = ['MaPhieuThu', 'MaKH', 'TenKH', 'SoTienThu', 'NguoiThu', 'NgayThu', 'MaKH_input', 'NguoiThu_input']

    def get_MaPhieuThu(self, obj):
        return f"PT{obj.MaPhieuThu:03d}"
    
    def get_NguoiThu(self, obj):
        return f'NV{obj.NguoiThu.id:03d}'
    
    def get_MaKH(self, obj):
        return f"KH{obj.MaKH.MaKhachHang:03d}"

    def validate_SoTienThu(self, value):
        if value <= 0:
            raise serializers.ValidationError("Số tiền thu phải lớn hơn 0.")
        return value    

    def validate(self, data):
        manv = data.get('NguoiThu_input')
        ma_kh_input = data.get('MaKH_input')
        sotienthu = data.get('SoTienThu')

        # Validate required fields
        if not ma_kh_input:
            raise serializers.ValidationError({"MaKH_input": "Phải nhập mã khách hàng."})
        
        if not manv:
            raise serializers.ValidationError({"manv": "Phải nhập tên người dùng."})
        
        try:
            manv = int(manv.replace('NV', ''))
            user = User.objects.get(id=manv)
        except User.DoesNotExist:
            raise serializers.ValidationError({"manv": f"Không tồn tại mã nhân viên '{manv}'."})
        
        try:
            ma_kh = int(ma_kh_input.replace('KH', ''))
            khachhang = KhachHang.objects.get(MaKhachHang=ma_kh)
        except (ValueError, KhachHang.DoesNotExist):
            raise serializers.ValidationError({
                'MaKH_input': f"Không tồn tại mã khách hàng '{ma_kh_input}'. Vui lòng nhập đúng mã khách hàng."
            })

        # Validate SoTienThu
        # create case
        if not self.instance:
            if sotienthu > khachhang.SoTienNo:
                raise serializers.ValidationError({
                    'SoTienThu': f"Số tiền thu ({sotienthu}) không được vượt quá số tiền nợ của khách hàng ({khachhang.SoTienNo})."
                })
        # update case:
        else:
            diff = sotienthu - self.SoTienThu
            new_no = khachhang.SoTienNo - diff
            if new_no < 0:
                raise serializers.ValidationError({
                    'SoTienThu': f"Số tiền thu ({sotienthu}) không được vượt quá số tiền nợ của khách hàng ({khachhang.SoTienNo})."
                })

        data['NguoiThu'] = user
        data['MaKH'] = khachhang
        return data
    
    def create(self, validated_data):
        # These fields were added during validation
        validated_data.pop('MaKH_input', None)
        validated_data.pop('NguoiThu_input', None)

        return PhieuThuTien.objects.create(**validated_data)

class CT_BCTonSerializer(serializers.ModelSerializer):
    TenSach = serializers.CharField(source='MaSach.MaDauSach.TenSach', read_only=True)
    MaSach = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    MaBCTon = serializers.SerializerMethodField()
    Thang = serializers.SerializerMethodField()
    Nam = serializers.SerializerMethodField()

    class Meta:
        model = CT_BCTon
        fields = ['id', 'MaBCTon', 'Thang', 'Nam', 'MaSach', 'TenSach', 'TonDau', 'PhatSinh', 'TonCuoi']
        read_only_fields = fields  # All fields are read-only

    def get_id(self, obj):
        return f"CTBCT{obj.id:03d}"

    def get_MaSach(self, obj):
        return f"S{obj.MaSach.MaSach:03d}"
    
    def get_MaBCTon(self, obj):
        return f"BCT{obj.MaBCTon.MaBCTon:03d}"

    def get_Thang(self, obj):
        return f"{obj.MaBCTon.Thang.month}"
    
    def get_Nam(self, obj):
        return f"{obj.MaBCTon.Thang.year}"
    
class BaoCaoTonSerializer(serializers.ModelSerializer):
    Thang_input = serializers.IntegerField(required=True, write_only=True)
    Nam_input = serializers.IntegerField(required=True, write_only=True)
    # chi_tiet_ton = CT_BCTonSerializer(many=True, read_only=True)
    MaBCTon = serializers.SerializerMethodField()
    Thang = serializers.DateField(format="%m/%Y", read_only=True)

    class Meta:
        model = BaoCaoTon
        fields = ['MaBCTon', 'Thang_input', 'Nam_input', 'Thang']
    
    def get_MaBCTon(self, obj):
        return f"BCT{obj.MaBCTon:03d}"

    def get_Thang(self, obj):
        return f"{obj.Thang}"

    def validate(self, data):
        first_date = PhieuNhapSach.objects.order_by('NgayNhap').values_list('NgayNhap', flat=True).first()
        if not first_date:
            raise serializers.ValidationError({
                'Error': f"Không có dữ liệu nhập/bán sách trong cơ sở dữ liệu."
            })
        last_date = PhieuNhapSach.objects.order_by('NgayNhap').values_list('NgayNhap', flat=True).last()
        month = data.get("Thang_input")
        year = data.get("Nam_input")
        request_date = date(year, month, 1)
        
        if request_date > last_date or request_date < first_date:
            raise serializers.ValidationError({
                'Error': f"Không có dữ liệu nhập/mua vào tháng {month}/{year}."
            })

        data['Thang'] = request_date
        return data
    
    def create(self, validated_data):
        thang = validated_data.pop("Thang")
        BaoCaoTon().generate_all_reports()
        return BaoCaoTon.objects.get(Thang=thang)
    
    def update(self, instance, validated_data):
        thang = validated_data.pop("Thang")
        BaoCaoTon().generate_all_reports()
        return BaoCaoTon.objects.get(Thang=thang)

class CT_BCCNSerializer(serializers.ModelSerializer):
    TenKH = serializers.CharField(source='MaKH.HoTen', read_only=True)
    MaKH = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    MaBCCN = serializers.SerializerMethodField()
    Thang = serializers.SerializerMethodField()
    Nam = serializers.SerializerMethodField()

    class Meta:
        model = CT_BCCongNo
        fields = ['id', 'MaBCCN', 'Thang', 'Nam', 'MaKH', 'TenKH', 'NoDau', 'PhatSinh', 'NoCuoi']
        read_only_fields = fields

    def get_MaKH(self, obj):
        return f"KH{obj.MaKH.MaKhachHang:03d}"
    
    def get_id(self, obj):
        return f"CTBCN{obj.id:03d}"
    
    def get_MaBCCN(self, obj):
        return f"BCCN{obj.MaBCCN.MaBCCN:03d}"
    
    def get_Thang(self, obj):
        return f"{obj.MaBCCN.Thang.month}"
    
    def get_Nam(self, obj):
        return f"{obj.MaBCCN.Thang.year}"

class BaoCaoCongNoSerializer(serializers.ModelSerializer):
    Thang_input = serializers.IntegerField(required=True, write_only=True)
    Nam_input = serializers.IntegerField(required=True, write_only=True)
    # chi_tiet_no = CT_BCCNSerializer(many=True, read_only=True)
    MaBCCN = serializers.SerializerMethodField()
    Thang = serializers.DateField(format="%m/%Y", read_only=True)

    class Meta:
        model = BaoCaoCongNo
        fields = ['MaBCCN', 'Thang_input', 'Nam_input', 'Thang']

    def get_MaBCCN(self, obj):
        return f"BCCN{obj.MaBCCN:03d}"
    
    def get_Thang(self, obj):
        return f"{obj.Thang}"

    def validate(self, data):
        m = data.get("Thang_input")
        y = data.get("Nam_input")

        first_date = HoaDon.objects.order_by('NgayLap').values_list('NgayLap', flat=True).first()
        if not first_date:
            raise serializers.ValidationError({
                'Error': f"Không có dữ liệu nợ/thu trong cơ sở dữ liệu."
            })
        last_date = HoaDon.objects.order_by('NgayLap').values_list('NgayLap', flat=True).last()

        request_date = date(y, m, 1)
        
        if request_date > last_date or request_date < first_date:
            raise serializers.ValidationError({
                'Error': f"Không có dữ liệu nợ/thu vào tháng {m}/{y}."
            })

        data['Thang'] = request_date
        return data

    def create(self, validated_data):
        thang = validated_data.pop("Thang")
        BaoCaoCongNo().generate_all_reports()
        return BaoCaoCongNo.objects.get(Thang=thang)
    
    def update(self, instance, validated_data):
        thang = validated_data.pop("Thang")
        BaoCaoCongNo().generate_all_reports()
        return BaoCaoCongNo.objects.get(Thang=thang)

    
class ThamSoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThamSo
        fields = '__all__'

    def validate_SLNhapTT(self, value):
        try:
            int(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Số lượng nhập tối thiểu phải là số nguyên dương.")
        
        if value <= 0:
            raise serializers.ValidationError("Số lượng nhập tối thiểu phải là số nguyên dương.")
        
        return value

    
    def validate_TonTD(self, value):
        try:
            int(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Tồn tối đa phải là số nguyên dương.")
        
        if value <= 0:
            raise serializers.ValidationError("Tồn tối đa phải là số nguyên dương.")
        
        return value

    def validate_NoTD(self, value):
        try:
            int(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Nợ tối đa phải là số nguyên dương.")
        
        if value <= 0:
            raise serializers.ValidationError("Nợ tối đa phải là số nguyên dương.")
        
        return value
    
    def validate_TonTT(self, value):
        try:
            int(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Tồn tối thiểu phải là số nguyên dương.")
        
        if value <= 0:
            raise serializers.ValidationError("Tồn tối thiểu phải là số nguyên dương.")
        
        return value
    
    def validate_TiLe(self, value):
        try:
            float(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError("Tỉ lệ phải là số thực duơng.")
        
        if value <= 0:
            raise serializers.ValidationError("Tỉ lệ phải là số thực duơng.")
        
        return value
    
    def validate_SDQD4(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Sử dụng quy định 4 phải là '0' hoặc '1'.")
        return value
    
def get_valid_groups():
    """Get all group names from the database"""
    return list(Group.objects.values_list('name', flat=True))

class UserSerializer(serializers.ModelSerializer):
    gioiTinh = serializers.CharField(source='profile.gioiTinh', required=False)
    role = serializers.CharField(required=False)  # Replace ChoiceField with CharField

    is_active = serializers.BooleanField(read_only=True)  # Add this field
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update choices dynamically
        self.valid_roles = [group.name for group in Group.objects.all()]


    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'gioiTinh', 'role', 'is_active']

    def validate_role(self, value):
        """Custom validation for the role field."""
        if value not in self.valid_roles:
            raise serializers.ValidationError(
                f"Nhóm người dùng '{value}' không tồn tại trong hệ thống. Vui lòng chọn một trong các nhóm: {', '.join(self.valid_roles)}"
            )
        return value
    
    def get_role(self, obj):
        return obj.groups.first().name if obj.groups.exists() else None
    
    def to_representation(self, instance):
        # This ensures we still return the role name in responses
        ret = super().to_representation(instance)
        ret['role'] = self.get_role(instance)
        return ret
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        role = validated_data.pop('role', None)
        
        if profile_data and 'gioiTinh' in profile_data:
            instance.profile.gioiTinh = profile_data['gioiTinh']
            instance.profile.save()
            
        if role:
            try:
                # Remove from current groups
                instance.groups.clear()
                # Add to new group
                group = Group.objects.get(name=role)
                instance.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError({
                    'role': f"Nhóm người dùng '{role}' không tồn tại trong hệ thống. Vui lòng chọn một trong các nhóm: {', '.join(self.valid_roles)}"
                })
            
        return super().update(instance, validated_data)

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True, required=True)  # Change ChoiceField to CharField
    group = serializers.SerializerMethodField(read_only=True)  # Add this for reading group

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.valid_roles = [group.name for group in Group.objects.all()]  # Fetch valid roles dynamically

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'role', 'group']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_role(self, value):
        """Custom validation for the role field."""
        if value not in self.valid_roles:
            raise serializers.ValidationError(
                f"Nhóm người dùng '{value}' không tồn tại trong hệ thống. Vui lòng chọn một trong các nhóm: {', '.join(self.valid_roles)}"
            )
        return value

    def get_group(self, obj):
        """Return the user's group name"""
        return obj.groups.first().name if obj.groups.exists() else None

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.is_active = True
        # Add user to the role group
        try:
            group = Group.objects.get(name=role)
            user.groups.add(group)
            user.save()
        except Group.DoesNotExist:
            user.delete()  # Cleanup if group assignment fails
            raise serializers.ValidationError({
                'role': f"Nhóm người dùng '{role}' không tồn tại trong hệ thống. Vui lòng chọn một trong các nhóm: {', '.join(self.valid_roles)}"
            })
        return user

    def to_representation(self, instance):
        """Custom representation that includes the group name"""
        ret = super().to_representation(instance)
        ret['role'] = self.get_group(instance)  # Replace 'group' with 'role' in output
        ret.pop('group', None)  # Remove the temporary 'group' field
        return ret
    


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']