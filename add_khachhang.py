# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import KhachHangSerializer

khachhang_data = [
#   {
#     "HoTen": "Nguyễn Văn An",
#     "DiaChi": "123 Lê Lợi, Quận 1, TP.HCM",
#     "DienThoai": "0905123456",
#     "Email": "an.nguyen@example.com"
#   },
#   {
#     "HoTen": "Trần Thị Bích Ngọc",
#     "DiaChi": "456 Trần Hưng Đạo, Quận 5, TP.HCM",
#     "DienThoai": "0934556677",
#     "Email": "ngoc.tran@example.com"
#   },
#   {
#     "HoTen": "Lê Minh Tuấn",
#     "DiaChi": "789 Nguyễn Trãi, Quận 3, TP.HCM",
#     "DienThoai": "0912345678",
#     "Email": "tuan.le@example.com"
#   },
#   {
#     "HoTen": "Phạm Thu Hà",
#     "DiaChi": "321 Hai Bà Trưng, Quận 1, TP.HCM",
#     "DienThoai": "0908555123",
#     "Email": "ha.pham@example.com"
#   },
#   {
#     "HoTen": "Đặng Quốc Huy",
#     "DiaChi": "22 Phan Đăng Lưu, Phú Nhuận, TP.HCM",
#     "DienThoai": "0967888999",
#     "Email": "huy.dang@example.com"
#   },
#   {
#     "HoTen": "Võ Ngọc Anh",
#     "DiaChi": "88 Cách Mạng Tháng 8, Quận 10, TP.HCM",
#     "DienThoai": "0911999888",
#     "Email": "anh.vo@example.com"
#   },
#   {
#     "HoTen": "Bùi Thị Mai",
#     "DiaChi": "56 Nguyễn Văn Cừ, Quận 1, TP.HCM",
#     "DienThoai": "0909777666",
#     "Email": "mai.bui@example.com"
#   },
#   {
#     "HoTen": "Hoàng Văn Long",
#     "DiaChi": "17 Lý Tự Trọng, Quận 1, TP.HCM",
#     "DienThoai": "0977888666",
#     "Email": "long.hoang@example.com"
#   },
#   {
#     "HoTen": "Trịnh Thảo Nhi",
#     "DiaChi": "14 Trường Chinh, Tân Bình, TP.HCM",
#     "DienThoai": "0933331122",
#     "Email": "nhi.trinh@example.com"
#   },
#   {
#     "HoTen": "Ngô Đức Kiên",
#     "DiaChi": "67 Võ Thị Sáu, Quận 3, TP.HCM",
#     "DienThoai": "0908000111",
#     "Email": "kien.ngo@example.com"
#   },
    {
    "HoTen": "Nguyễn Văn An",
    "DiaChi": "123 Lý Thường Kiệt, Q.10, TP.HCM",
    "DienThoai": "0901234567",
    "Email": "an.nguyen@example.com"
  },
  {
    "HoTen": "Trần Thị Bích",
    "DiaChi": "45 Nguyễn Trãi, Q.5, TP.HCM",
    "DienThoai": "0913345678",
    "Email": "bich.tran@example.com"
  },
  {
    "HoTen": "Phạm Quốc Cường",
    "DiaChi": "678 Điện Biên Phủ, Q.3, TP.HCM",
    "DienThoai": "0923456789",
    "Email": "cuong.pham@example.com"
  },
  {
    "HoTen": "Lê Mỹ Duyên",
    "DiaChi": "89 Cách Mạng Tháng 8, Q.1, TP.HCM",
    "DienThoai": "0934567890",
    "Email": "duyen.le@example.com"
  },
  {
    "HoTen": "Đỗ Văn Em",
    "DiaChi": "12 Trường Chinh, Tân Bình, TP.HCM",
    "DienThoai": "0945678901",
    "Email": "em.do@example.com"
  },
  {
    "HoTen": "Vũ Hà Giang",
    "DiaChi": "9A Pasteur, Q.3, TP.HCM",
    "DienThoai": "0956789012",
    "Email": "giang.vu@example.com"
  },
  {
    "HoTen": "Lý Minh Hiếu",
    "DiaChi": "234 Nguyễn Văn Cừ, Q.5, TP.HCM",
    "DienThoai": "0967890123",
    "Email": "hieu.ly@example.com"
  },
  {
    "HoTen": "Ngô Thị Ích",
    "DiaChi": "567 Trần Hưng Đạo, Q.1, TP.HCM",
    "DienThoai": "0978901234",
    "Email": "ich.ngo@example.com"
  },
  {
    "HoTen": "Hoàng Văn Khoa",
    "DiaChi": "21 Huỳnh Tấn Phát, Q.7, TP.HCM",
    "DienThoai": "0989012345",
    "Email": "khoa.hoang@example.com"
  },
  {
    "HoTen": "Mai Thị Lan",
    "DiaChi": "33 Phan Xích Long, Q. Phú Nhuận, TP.HCM",
    "DienThoai": "0990123456",
    "Email": "lan.mai@example.com"
  }
]


success, failed = 0, 0

for item in khachhang_data:
    serializer = KhachHangSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")