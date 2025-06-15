# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import NXBSerializer

nxb_data = [
  { "TenNXB": "NXB Sân Khấu" },
  { "TenNXB": "NXB Quân Đội Nhân Dân" },
  { "TenNXB": "NXB Hà Nội" },
  { "TenNXB": "NXB Công An Nhân Dân" },
  { "TenNXB": "NXB Khoa Học Xã Hội" },
  { "TenNXB": "NXB Mỹ Thuật" },
  { "TenNXB": "NXB Âm Nhạc" },
  { "TenNXB": "NXB Y Học" },
  { "TenNXB": "NXB Kinh Tế TP.HCM" },
  { "TenNXB": "NXB Tri Thức" },
  { "TenNXB": "NXB Văn Nghệ TP.HCM" },
  { "TenNXB": "NXB Kim Đồng" },
  { "TenNXB": "NXB Trẻ" },
  { "TenNXB": "NXB Giáo Dục Việt Nam" },
  { "TenNXB": "NXB Văn Học" },
  { "TenNXB": "NXB Tổng Hợp TP.HCM" },
  { "TenNXB": "NXB Phụ Nữ" },
  { "TenNXB": "NXB Hội Nhà Văn" },
  { "TenNXB": "NXB Lao Động" },
  { "TenNXB": "NXB Chính Trị Quốc Gia Sự Thật" },
  { "TenNXB": "NXB Thông Tin và Truyền Thông" },
  { "TenNXB": "NXB Khoa Học và Kỹ Thuật" },
  { "TenNXB": "NXB Tư Pháp" },
  { "TenNXB": "NXB Văn Hóa - Văn Nghệ" },
  { "TenNXB": "NXB Đại Học Quốc Gia TP.HCM" },
  { "TenNXB": "NXB Thanh Niên" }
]

success, failed = 0, 0

for item in nxb_data:
    serializer = NXBSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")