# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import TacGiaSerializer

tacgia_data = [
  { "TenTG": "Nguyễn Nhật Ánh" },
  { "TenTG": "J.K. Rowling" },
  { "TenTG": "Dan Brown" },
  { "TenTG": "Haruki Murakami" },
  { "TenTG": "Paulo Coelho" },
  { "TenTG": "Stephen King" },
  { "TenTG": "George R.R. Martin" },
  { "TenTG": "Nguyễn Huy Thiệp" },
  { "TenTG": "Ernest Hemingway" },
  { "TenTG": "F. Scott Fitzgerald" },
  { "TenTG": "Jane Austen" },
  { "TenTG": "Nguyễn Minh Châu" },
  { "TenTG": "Isaac Asimov" },
  { "TenTG": "Truman Capote" },
  { "TenTG": "Lỗ Tấn" },
  { "TenTG": "Victor Hugo" },
  { "TenTG": "Franz Kafka" },
  { "TenTG": "Fyodor Dostoevsky" },
  { "TenTG": "Nguyễn Quang Sáng" },
  { "TenTG": "Margaret Atwood" },
  { "TenTG": "Gabriel García Márquez" },
  { "TenTG": "Leo Tolstoy" },
  { "TenTG": "Charles Dickens" },
  { "TenTG": "Ngô Tất Tố" },
  { "TenTG": "Kazuo Ishiguro" },
  { "TenTG": "Nguyễn Tuân" },
  { "TenTG": "Antoine de Saint-Exupéry" },
  { "TenTG": "Albert Camus" },
  { "TenTG": "J.R.R. Tolkien" },
  { "TenTG": "Nguyễn Đình Thi" },
  { "TenTG": "Trịnh Công Sơn" },
  { "TenTG": "Nguyễn Du" },
  { "TenTG": "Xuân Diệu" },
  { "TenTG": "Nam Cao" },
  { "TenTG": "Tô Hoài" },
  { "TenTG": "Vũ Trọng Phụng" },
  { "TenTG": "Nguyễn Khải" },
  { "TenTG": "Nguyễn Ngọc Tư" },
  { "TenTG": "Nguyễn Thị Thu Huệ" },
  { "TenTG": "Minh Nhật" },
  { "TenTG": "Lê Minh Khuê" },
  { "TenTG": "Bùi Anh Tuấn" },
  { "TenTG": "Nguyễn Phan Hách" },
  { "TenTG": "Lê Anh Hoài" },
  { "TenTG": "Nguyễn Thị Hoàng" },
  { "TenTG": "Nguyễn Đông Thức" },
  { "TenTG": "Dương Thụ" },
  { "TenTG": "Nguyễn Nhật Duy" },
  { "TenTG": "Nguyễn Trí Huân" },
  { "TenTG": "Nguyễn Thành Long" }
]

success, failed = 0, 0

for item in tacgia_data:
    serializer = TacGiaSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")