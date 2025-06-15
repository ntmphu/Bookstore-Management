# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import DauSachSerializer

dausach_data = [
  {
    "TenSach": "Cho Tôi Xin Một Vé Đi Tuổi Thơ",
    "TenTheLoai_input": "Thiếu nhi",
    "TenTacGia_input": ["Nguyễn Nhật Ánh"]
  },
  {
    "TenSach": "Harry Potter và Hòn Đá Phù Thủy",
    "TenTheLoai_input": "Khoa học viễn tưởng",
    "TenTacGia_input": ["J.K. Rowling"]
  },
  {
    "TenSach": "Mật Mã Da Vinci",
    "TenTheLoai_input": "Trinh thám",
    "TenTacGia_input": ["Dan Brown"]
  },
  {
    "TenSach": "Rừng Na Uy",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Haruki Murakami"]
  },
  {
    "TenSach": "Nhà Giả Kim",
    "TenTheLoai_input": "Triết học",
    "TenTacGia_input": ["Paulo Coelho"]
  },
  {
    "TenSach": "Gã Hề Ma Quái (It)",
    "TenTheLoai_input": "Kinh dị",
    "TenTacGia_input": ["Stephen King"]
  },
  {
    "TenSach": "Chí Phèo",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nam Cao"]
  },
  {
    "TenSach": "Dế Mèn Phiêu Lưu Ký",
    "TenTheLoai_input": "Thiếu nhi",
    "TenTacGia_input": ["Tô Hoài"]
  },
  {
    "TenSach": "Số Đỏ",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Vũ Trọng Phụng"]
  },
  {
    "TenSach": "Hoàng Tử Bé",
    "TenTheLoai_input": "Triết học",
    "TenTacGia_input": ["Antoine de Saint-Exupéry"]
  },
  {
    "TenSach": "Truyện Kiều",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Du"]
  },
  {
    "TenSach": "Lặng Lẽ Sa Pa",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Thành Long"]
  },
  {
    "TenSach": "Những Người Khốn Khổ",
    "TenTheLoai_input": "Lịch sử",
    "TenTacGia_input": ["Victor Hugo"]
  },
  {
    "TenSach": "Tôi, Robot",
    "TenTheLoai_input": "Khoa học viễn tưởng",
    "TenTacGia_input": ["Isaac Asimov"]
  },
  {
    "TenSach": "Cánh Đồng Bất Tận",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Ngọc Tư"]
  },
  {
    "TenSach": "Tắt Đèn",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Ngô Tất Tố"]
  },
  {
    "TenSach": "Tâm Lý Học Đám Đông",
    "TenTheLoai_input": "Tâm lý học",
    "TenTacGia_input": ["Nguyễn Trí Huân", "Lê Anh Hoài"]
  },
  {
    "TenSach": "Nhập Môn Lập Trình",
    "TenTheLoai_input": "Công nghệ thông tin",
    "TenTacGia_input": ["Bùi Anh Tuấn", "Nguyễn Nhật Duy"]
  },
  {
    "TenSach": "Hành Trình Ẩm Thực Việt",
    "TenTheLoai_input": "Ẩm thực",
    "TenTacGia_input": ["Nguyễn Thị Thu Huệ"]
  },
  {
    "TenSach": "Để Gió Cuốn Đi",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Trịnh Công Sơn", "Dương Thụ"]
  },
  {
    "TenSach": "Trò Chơi Vương Quyền",
    "TenTheLoai_input": "Khoa học viễn tưởng",
    "TenTacGia_input": ["George R.R. Martin"]
  },
  {
    "TenSach": "Ông Già Và Biển Cả",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Ernest Hemingway"]
  },
  {
    "TenSach": "Gatsby Vĩ Đại",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["F. Scott Fitzgerald"]
  },
  {
    "TenSach": "Kiêu Hãnh và Định Kiến",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Jane Austen"]
  },
  {
    "TenSach": "Chiến Tranh Và Hòa Bình",
    "TenTheLoai_input": "Lịch sử",
    "TenTacGia_input": ["Leo Tolstoy"]
  },
  {
    "TenSach": "Tội Ác và Hình Phạt",
    "TenTheLoai_input": "Tâm lý học",
    "TenTacGia_input": ["Fyodor Dostoevsky"]
  },
  {
    "TenSach": "Chuyện Người Tùy Nữ",
    "TenTheLoai_input": "Khoa học viễn tưởng",
    "TenTacGia_input": ["Margaret Atwood"]
  },
  {
    "TenSach": "Trăm Năm Cô Đơn",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Gabriel García Márquez"]
  },
  {
    "TenSach": "Người Xa Lạ (Kẻ Ngoại Cuộc)",
    "TenTheLoai_input": "Triết học",
    "TenTacGia_input": ["Albert Camus"]
  },
  {
    "TenSach": "Chúa Tể Của Những Chiếc Nhẫn",
    "TenTheLoai_input": "Khoa học viễn tưởng",
    "TenTacGia_input": ["J.R.R. Tolkien"]
  },
  {
    "TenSach": "Vang Bóng Một Thời",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Tuân"]
  },
  {
    "TenSach": "Tướng Về Hưu",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Huy Thiệp"]
  },
  {
    "TenSach": "AQ Chính Truyện",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Lỗ Tấn"]
  },
  {
    "TenSach": "Hóa Thân",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Franz Kafka"]
  },
  {
    "TenSach": "Mảnh Trăng Cuối Rừng",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Minh Châu"]
  },
  {
    "TenSach": "Bí Quyết Đầu Tư Thông Minh",
    "TenTheLoai_input": "Kinh tế",
    "TenTacGia_input": ["Minh Nhật"]
  },
  {
    "TenSach": "Phương Pháp Dạy Học Tích Cực",
    "TenTheLoai_input": "Giáo dục",
    "TenTacGia_input": ["Nguyễn Thị Hoàng", "Lê Anh Hoài"]
  },
  {
    "TenSach": "Nghệ Thuật Giao Tiếp Hiệu Quả",
    "TenTheLoai_input": "Kỹ năng sống",
    "TenTacGia_input": ["Nguyễn Đông Thức"]
  },
  {
    "TenSach": "Sổ Tay Chăm Sóc Sức Khỏe Gia Đình",
    "TenTheLoai_input": "Y học",
    "TenTacGia_input": ["Lê Minh Khuê"]
  },
  {
    "TenSach": "Giai Điệu Thời Gian",
    "TenTheLoai_input": "Âm nhạc",
    "TenTacGia_input": ["Trịnh Công Sơn", "Dương Thụ"]
  },
  {
    "TenSach": "Bước Chân Trên Miền Đất Lạ",
    "TenTheLoai_input": "Du ký",
    "TenTacGia_input": ["Nguyễn Phan Hách"]
  },
  {
    "TenSach": "Cái Đẹp Trong Mỹ Thuật Đương Đại",
    "TenTheLoai_input": "Nghệ thuật",
    "TenTacGia_input": ["Nguyễn Đình Thi"]
  },
  {
    "TenSach": "Tiếng Cười Dân Gian",
    "TenTheLoai_input": "Hài hước",
    "TenTacGia_input": ["Nguyễn Quang Sáng"]
  },
  {
    "TenSach": "Mãi Mãi Là Bao Xa",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Kazuo Ishiguro"]
  },
  {
    "TenSach": "Lịch Sử Các Học Thuyết Kinh Tế",
    "TenTheLoai_input": "Kinh tế",
    "TenTacGia_input": ["Bùi Anh Tuấn", "Nguyễn Trí Huân"]
  },
  {
    "TenSach": "Chiếc Thuyền Ngoài Xa",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Minh Châu"]
  },
  {
    "TenSach": "Lập Trình Hướng Đối Tượng",
    "TenTheLoai_input": "Công nghệ thông tin",
    "TenTacGia_input": ["Nguyễn Nhật Duy"]
  },
  {
    "TenSach": "Mùa Lạc",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Khải"]
  },
  {
    "TenSach": "Tuyển Tập Thơ Tình Xuân Diệu",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Xuân Diệu"]
  },
  {
    "TenSach": "Oliver Twist",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Charles Dickens"]
  },
  {
    "TenSach": "Mắt Biếc",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Nguyễn Nhật Ánh"]
  },
  {
    "TenSach": "Thiên Thần và Ác Quỷ",
    "TenTheLoai_input": "Trinh thám",
    "TenTacGia_input": ["Dan Brown"]
  },
  {
    "TenSach": "Ngôi Nhà Ma Ám (The Shining)",
    "TenTheLoai_input": "Kinh dị",
    "TenTacGia_input": ["Stephen King"]
  },
  {
    "TenSach": "Lão Hạc",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nam Cao"]
  },
  {
    "TenSach": "Bí Mật Dinh Dưỡng Cho Sức Khỏe Toàn Diện",
    "TenTheLoai_input": "Y học",
    "TenTacGia_input": ["Lê Minh Khuê", "Nguyễn Thị Thu Huệ"]
  },
  {
    "TenSach": "Tư Duy Phản Biện",
    "TenTheLoai_input": "Kỹ năng sống",
    "TenTacGia_input": ["Paulo Coelho"]
  },
  {
    "TenSach": "Lịch Sử Việt Nam Toàn Tập",
    "TenTheLoai_input": "Lịch sử",
    "TenTacGia_input": ["Nguyễn Khải", "Ngô Tất Tố"]
  },
  {
    "TenSach": "Harry Potter và Tên Tù Nhân Ngục Azkaban",
    "TenTheLoai_input": "Khoa học viễn tưởng",
    "TenTacGia_input": ["J.K. Rowling"]
  },
  {
    "TenSach": "Hà Nội Băm Sáu Phố Phường",
    "TenTheLoai_input": "Du ký",
    "TenTacGia_input": ["Nguyễn Tuân", "Tô Hoài"]
  },
  {
    "TenSach": "Tâm Lý Học Tội Phạm",
    "TenTheLoai_input": "Tâm lý học",
    "TenTacGia_input": ["Truman Capote"]
  },
  {
    "TenSach": "Nền Tảng Kinh Tế Vĩ Mô",
    "TenTheLoai_input": "Kinh tế",
    "TenTacGia_input": ["Bùi Anh Tuấn"]
  },
  {
    "TenSach": "Giông Tố",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Vũ Trọng Phụng"]
  },
  {
    "TenSach": "Nghệ Thuật Tối Giản",
    "TenTheLoai_input": "Kỹ năng sống",
    "TenTacGia_input": ["Haruki Murakami"]
  },
  {
    "TenSach": "Phát Triển Tư Duy Cho Trẻ",
    "TenTheLoai_input": "Giáo dục",
    "TenTacGia_input": ["Nguyễn Thị Hoàng"]
  },
  {
    "TenSach": "Những Giai Điệu Bất Hủ",
    "TenTheLoai_input": "Âm nhạc",
    "TenTacGia_input": ["Trịnh Công Sơn"]
  },
  {
    "TenSach": "An Ninh Mạng Cơ Bản",
    "TenTheLoai_input": "Công nghệ thông tin",
    "TenTacGia_input": ["Nguyễn Nhật Duy"]
  },
  {
    "TenSach": "Hương Vị Quê Nhà",
    "TenTheLoai_input": "Ẩm thực",
    "TenTacGia_input": ["Nguyễn Ngọc Tư"]
  },
  {
    "TenSach": "Chuyện Làng Nho",
    "TenTheLoai_input": "Hài hước",
    "TenTacGia_input": ["Ngô Tất Tố"]
  },
  {
    "TenSach": "Thế Giới Phẳng",
    "TenTheLoai_input": "Kinh tế",
    "TenTacGia_input": ["Minh Nhật"]
  },
  {
    "TenSach": "Những vì sao xa xôi",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Lê Minh Khuê"]
  },
  {
    "TenSach": "Bức Tranh",
    "TenTheLoai_input": "Nghệ thuật",
    "TenTacGia_input": ["Victor Hugo"]
  },
  {
    "TenSach": "Bản Giao Hưởng Định Mệnh",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Kazuo Ishiguro"]
  },
  {
    "TenSach": "Vũ Trụ Trong Vỏ Hạt Dẻ",
    "TenTheLoai_input": "Khoa học viễn tưởng",
    "TenTacGia_input": ["Isaac Asimov"]
  },
  {
    "TenSach": "Anna Karenina",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Leo Tolstoy"]
  },
  {
    "TenSach": "Khi Lỗi Thuộc Về Những Vì Sao",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Nguyễn Thị Hoàng"]
  },
  {
    "TenSach": "Triết Lý Sống",
    "TenTheLoai_input": "Triết học",
    "TenTacGia_input": ["Albert Camus", "Lỗ Tấn"]
  },
  {
    "TenSach": "Bến Quê",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Minh Châu"]
  },
  {
    "TenSach": "Kỹ Năng Quản Lý Thời Gian",
    "TenTheLoai_input": "Kỹ năng sống",
    "TenTacGia_input": ["Lê Anh Hoài"]
  },
  {
    "TenSach": "David Copperfield",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Charles Dickens"]
  },
  {
    "TenSach": "Gia Đình",
    "TenTheLoai_input": "Tâm lý học",
    "TenTacGia_input": ["Nguyễn Thị Thu Huệ"]
  },
  {
    "TenSach": "Vòng Quanh Thế Giới",
    "TenTheLoai_input": "Du ký",
    "TenTacGia_input": ["Nguyễn Phan Hách"]
  },
  {
    "TenSach": "Tuyển Tập Truyện Ngắn Nguyễn Huy Thiệp",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Huy Thiệp"]
  },
  {
    "TenSach": "Cấu Trúc Dữ Liệu và Giải Thuật",
    "TenTheLoai_input": "Công nghệ thông tin",
    "TenTacGia_input": ["Bùi Anh Tuấn"]
  },
  {
    "TenSach": "Thơ Tình Gửi Một Người",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Xuân Diệu"]
  },
  {
    "TenSach": "Vụ Án",
    "TenTheLoai_input": "Trinh thám",
    "TenTacGia_input": ["Franz Kafka"]
  },
  {
    "TenSach": "Chuyện Cũ Hà Nội",
    "TenTheLoai_input": "Lịch sử",
    "TenTacGia_input": ["Tô Hoài"]
  },
  {
    "TenSach": "Đắc Nhân Tâm",
    "TenTheLoai_input": "Kỹ năng sống",
    "TenTacGia_input": ["Nguyễn Trí Huân"]
  },
  {
    "TenSach": "Hồi Ký Chiến Tranh",
    "TenTheLoai_input": "Lịch sử",
    "TenTacGia_input": ["Nguyễn Đình Thi", "Nguyễn Quang Sáng"]
  },
  {
    "TenSach": "Cô Gái Đến Từ Hôm Qua",
    "TenTheLoai_input": "Tình cảm",
    "TenTacGia_input": ["Nguyễn Nhật Ánh"]
  },
  {
    "TenSach": "Nghệ Thuật Sân Khấu",
    "TenTheLoai_input": "Nghệ thuật",
    "TenTacGia_input": ["Dương Thụ"]
  },
  {
    "TenSach": "Bí Ẩn Về Cái Chết Của Marilyn Monroe",
    "TenTheLoai_input": "Trinh thám",
    "TenTacGia_input": ["Truman Capote"]
  },
  {
    "TenSach": "Anh Em Nhà Karamazov",
    "TenTheLoai_input": "Văn học nước ngoài",
    "TenTacGia_input": ["Fyodor Dostoevsky"]
  },
  {
    "TenSach": "Những Bài Học Giáo Dục Sớm",
    "TenTheLoai_input": "Giáo dục",
    "TenTacGia_input": ["Nguyễn Thị Hoàng"]
  },
  {
    "TenSach": "Lý Thuyết Trò Chơi và Ứng Dụng Kinh Tế",
    "TenTheLoai_input": "Kinh tế",
    "TenTacGia_input": ["Minh Nhật", "Bùi Anh Tuấn"]
  },
  {
    "TenSach": "Cẩm Nang Phòng Bệnh Tim Mạch",
    "TenTheLoai_input": "Y học",
    "TenTacGia_input": ["Lê Minh Khuê"]
  },
  {
    "TenSach": "Truyện Cười Hiện Đại",
    "TenTheLoai_input": "Hài hước",
    "TenTacGia_input": ["Nguyễn Đông Thức"]
  },
  {
    "TenSach": "Khởi Nghiệp Trong Thời Đại 4.0",
    "TenTheLoai_input": "Kinh tế",
    "TenTacGia_input": ["Nguyễn Trí Huân"]
  },
  {
    "TenSach": "Đất Rừng Phương Nam",
    "TenTheLoai_input": "Văn học Việt Nam",
    "TenTacGia_input": ["Nguyễn Quang Sáng"]
  },
  {
    "TenSach": "Xứ Đẹp",
    "TenTheLoai_input": "Du ký",
    "TenTacGia_input": ["Nguyễn Tuân"]
  },
  {
    "TenSach": "Dạy Con Làm Giàu",
    "TenTheLoai_input": "Giáo dục",
    "TenTacGia_input": ["Lê Anh Hoài"]
  }
]

success, failed = 0, 0

for item in dausach_data:
    serializer = DauSachSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")