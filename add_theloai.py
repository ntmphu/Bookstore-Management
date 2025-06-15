# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import TheLoaiSerializer

theloai_data = [
  { "TenTheLoai": "Khoa học viễn tưởng" },
  { "TenTheLoai": "Trinh thám" },
  { "TenTheLoai": "Kinh dị" },
  { "TenTheLoai": "Lịch sử" },
  { "TenTheLoai": "Tâm lý học" },
  { "TenTheLoai": "Kinh tế" },
  { "TenTheLoai": "Giáo dục" },
  { "TenTheLoai": "Văn học Việt Nam" },
  { "TenTheLoai": "Văn học nước ngoài" },
  { "TenTheLoai": "Kỹ năng sống" },
  { "TenTheLoai": "Thiếu nhi" },
  { "TenTheLoai": "Tình cảm" },
  { "TenTheLoai": "Triết học" },
  { "TenTheLoai": "Nghệ thuật" },
  { "TenTheLoai": "Âm nhạc" },
  { "TenTheLoai": "Công nghệ thông tin" },
  { "TenTheLoai": "Y học" },
  { "TenTheLoai": "Du ký" },
  { "TenTheLoai": "Ẩm thực" },
  { "TenTheLoai": "Hài hước" }
]

success, failed = 0, 0

for item in theloai_data:
    serializer = TheLoaiSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")