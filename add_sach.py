# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import SachSerializer

sach_data = [
#   {
#     "TenDauSach_input": "Cho Tôi Xin Một Vé Đi Tuổi Thơ",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2008"
#   },
#   {
#     "TenDauSach_input": "Cho Tôi Xin Một Vé Đi Tuổi Thơ",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Harry Potter và Hòn Đá Phù Thủy",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2003"
#   },
#   {
#     "TenDauSach_input": "Harry Potter và Hòn Đá Phù Thủy",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Mật Mã Da Vinci",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2005"
#   },
#   {
#     "TenDauSach_input": "Mật Mã Da Vinci",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Rừng Na Uy",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2006"
#   },
#   {
#     "TenDauSach_input": "Rừng Na Uy",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Nhà Giả Kim",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2013"
#   },
#   {
#     "TenDauSach_input": "Nhà Giả Kim",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Gã Hề Ma Quái (It)",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Gã Hề Ma Quái (It)",
#     "TenNXB_input": "NXB Thanh Niên",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Chí Phèo",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2002"
#   },
#   {
#     "TenDauSach_input": "Chí Phèo",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Dế Mèn Phiêu Lưu Ký",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "1999"
#   },
#   {
#     "TenDauSach_input": "Dế Mèn Phiêu Lưu Ký",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2014"
#   },
#   {
#     "TenDauSach_input": "Số Đỏ",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2005"
#   },
#   {
#     "TenDauSach_input": "Số Đỏ",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Hoàng Tử Bé",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2013"
#   },
#   {
#     "TenDauSach_input": "Hoàng Tử Bé",
#     "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Truyện Kiều",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2000"
#   },
#   {
#     "TenDauSach_input": "Truyện Kiều",
#     "TenNXB_input": "NXB Chính Trị Quốc Gia Sự Thật",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Lặng Lẽ Sa Pa",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2008"
#   },
#   {
#     "TenDauSach_input": "Lặng Lẽ Sa Pa",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Những Người Khốn Khổ",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2007"
#   },
#   {
#     "TenDauSach_input": "Những Người Khốn Khổ",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Tôi, Robot",
#     "TenNXB_input": "NXB Khoa Học và Kỹ Thuật",
#     "NamXB": "2011"
#   },
#   {
#     "TenDauSach_input": "Tôi, Robot",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Cánh Đồng Bất Tận",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2005"
#   },
#   {
#     "TenDauSach_input": "Cánh Đồng Bất Tận",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Tắt Đèn",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2004"
#   },
#   {
#     "TenDauSach_input": "Tắt Đèn",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Tâm Lý Học Đám Đông",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Tâm Lý Học Đám Đông",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Nhập Môn Lập Trình",
#     "TenNXB_input": "NXB Khoa Học và Kỹ Thuật",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Nhập Môn Lập Trình",
#     "TenNXB_input": "NXB Đại Học Quốc Gia TP.HCM",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Hành Trình Ẩm Thực Việt",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Hành Trình Ẩm Thực Việt",
#     "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Để Gió Cuốn Đi",
#     "TenNXB_input": "NXB Văn Nghệ TP.HCM",
#     "NamXB": "2001"
#   },
#   {
#     "TenDauSach_input": "Để Gió Cuốn Đi",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Trò Chơi Vương Quyền",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2012"
#   },
#   {
#     "TenDauSach_input": "Trò Chơi Vương Quyền",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Ông Già Và Biển Cả",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2003"
#   },
#   {
#     "TenDauSach_input": "Ông Già Và Biển Cả",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Gatsby Vĩ Đại",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2011"
#   },
#   {
#     "TenDauSach_input": "Gatsby Vĩ Đại",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Kiêu Hãnh và Định Kiến",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2009"
#   },
#   {
#     "TenDauSach_input": "Kiêu Hãnh và Định Kiến",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Chiến Tranh Và Hòa Bình",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2001"
#   },
#   {
#     "TenDauSach_input": "Chiến Tranh Và Hòa Bình",
#     "TenNXB_input": "NXB Chính Trị Quốc Gia Sự Thật",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Tội Ác và Hình Phạt",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2006"
#   },
#   {
#     "TenDauSach_input": "Tội Ác và Hình Phạt",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Chuyện Người Tùy Nữ",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Chuyện Người Tùy Nữ",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Trăm Năm Cô Đơn",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2002"
#   },
#   {
#     "TenDauSach_input": "Trăm Năm Cô Đơn",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Người Xa Lạ (Kẻ Ngoại Cuộc)",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2010"
#   },
#   {
#     "TenDauSach_input": "Người Xa Lạ (Kẻ Ngoại Cuộc)",
#     "TenNXB_input": "NXB Tri Thức",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Chúa Tể Của Những Chiếc Nhẫn",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2004"
#   },
#   {
#     "TenDauSach_input": "Chúa Tể Của Những Chiếc Nhẫn",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2014"
#   },
#   {
#     "TenDauSach_input": "Vang Bóng Một Thời",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "1999"
#   },
#   {
#     "TenDauSach_input": "Vang Bóng Một Thời",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Tướng Về Hưu",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "1995"
#   },
#   {
#     "TenDauSach_input": "Tướng Về Hưu",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2012"
#   },
#   {
#     "TenDauSach_input": "AQ Chính Truyện",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2005"
#   },
#   {
#     "TenDauSach_input": "AQ Chính Truyện",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Hóa Thân",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2011"
#   },
#   {
#     "TenDauSach_input": "Hóa Thân",
#     "TenNXB_input": "NXB Tri Thức",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Mảnh Trăng Cuối Rừng",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2009"
#   },
#   {
#     "TenDauSach_input": "Mảnh Trăng Cuối Rừng",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Bí Quyết Đầu Tư Thông Minh",
#     "TenNXB_input": "NXB Kinh Tế TP.HCM",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Bí Quyết Đầu Tư Thông Minh",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Phương Pháp Dạy Học Tích Cực",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Phương Pháp Dạy Học Tích Cực",
#     "TenNXB_input": "NXB Đại Học Quốc Gia TP.HCM",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Nghệ Thuật Giao Tiếp Hiệu Quả",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Nghệ Thuật Giao Tiếp Hiệu Quả",
#     "TenNXB_input": "NXB Thanh Niên",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Sổ Tay Chăm Sóc Sức Khỏe Gia Đình",
#     "TenNXB_input": "NXB Y Học",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Sổ Tay Chăm Sóc Sức Khỏe Gia Đình",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Giai Điệu Thời Gian",
#     "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
#     "NamXB": "2010"
#   },
#   {
#     "TenDauSach_input": "Giai Điệu Thời Gian",
#     "TenNXB_input": "NXB Âm Nhạc",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Bước Chân Trên Miền Đất Lạ",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2013"
#   },
#   {
#     "TenDauSach_input": "Bước Chân Trên Miền Đất Lạ",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Cái Đẹp Trong Mỹ Thuật Đương Đại",
#     "TenNXB_input": "NXB Mỹ Thuật",
#     "NamXB": "2014"
#   },
#   {
#     "TenDauSach_input": "Cái Đẹp Trong Mỹ Thuật Đương Đại",
#     "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Tiếng Cười Dân Gian",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2007"
#   },
#   {
#     "TenDauSach_input": "Tiếng Cười Dân Gian",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Mãi Mãi Là Bao Xa",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Mãi Mãi Là Bao Xa",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Lịch Sử Các Học Thuyết Kinh Tế",
#     "TenNXB_input": "NXB Chính Trị Quốc Gia Sự Thật",
#     "NamXB": "2012"
#   },
#   {
#     "TenDauSach_input": "Lịch Sử Các Học Thuyết Kinh Tế",
#     "TenNXB_input": "NXB Kinh Tế TP.HCM",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Chiếc Thuyền Ngoài Xa",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2006"
#   },
#   {
#     "TenDauSach_input": "Chiếc Thuyền Ngoài Xa",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Lập Trình Hướng Đối Tượng",
#     "TenNXB_input": "NXB Khoa Học và Kỹ Thuật",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Lập Trình Hướng Đối Tượng",
#     "TenNXB_input": "NXB Thông Tin và Truyền Thông",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Mùa Lạc",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "1998"
#   },
#   {
#     "TenDauSach_input": "Mùa Lạc",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Tuyển Tập Thơ Tình Xuân Diệu",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2003"
#   },
#   {
#     "TenDauSach_input": "Tuyển Tập Thơ Tình Xuân Diệu",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Oliver Twist",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2008"
#   },
#   {
#     "TenDauSach_input": "Oliver Twist",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Mắt Biếc",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "1990"
#   },
#   {
#     "TenDauSach_input": "Mắt Biếc",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2013"
#   },
#   {
#     "TenDauSach_input": "Thiên Thần và Ác Quỷ",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2006"
#   },
#   {
#     "TenDauSach_input": "Thiên Thần và Ác Quỷ",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Ngôi Nhà Ma Ám (The Shining)",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Ngôi Nhà Ma Ám (The Shining)",
#     "TenNXB_input": "NXB Thanh Niên",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Lão Hạc",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2002"
#   },
#   {
#     "TenDauSach_input": "Lão Hạc",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Bí Mật Dinh Dưỡng Cho Sức Khỏe Toàn Diện",
#     "TenNXB_input": "NXB Y Học",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Bí Mật Dinh Dưỡng Cho Sức Khỏe Toàn Diện",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Tư Duy Phản Biện",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Tư Duy Phản Biện",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Lịch Sử Việt Nam Toàn Tập",
#     "TenNXB_input": "NXB Chính Trị Quốc Gia Sự Thật",
#     "NamXB": "2010"
#   },
#   {
#     "TenDauSach_input": "Lịch Sử Việt Nam Toàn Tập",
#     "TenNXB_input": "NXB Khoa Học Xã Hội",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Harry Potter và Tên Tù Nhân Ngục Azkaban",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2004"
#   },
#   {
#     "TenDauSach_input": "Harry Potter và Tên Tù Nhân Ngục Azkaban",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Hà Nội Băm Sáu Phố Phường",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2000"
#   },
#   {
#     "TenDauSach_input": "Hà Nội Băm Sáu Phố Phường",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Tâm Lý Học Tội Phạm",
#     "TenNXB_input": "NXB Tư Pháp",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Tâm Lý Học Tội Phạm",
#     "TenNXB_input": "NXB Công An Nhân Dân",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Nền Tảng Kinh Tế Vĩ Mô",
#     "TenNXB_input": "NXB Kinh Tế TP.HCM",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Nền Tảng Kinh Tế Vĩ Mô",
#     "TenNXB_input": "NXB Đại Học Quốc Gia TP.HCM",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Giông Tố",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2007"
#   },
#   {
#     "TenDauSach_input": "Giông Tố",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Nghệ Thuật Tối Giản",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Nghệ Thuật Tối Giản",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Phát Triển Tư Duy Cho Trẻ",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Phát Triển Tư Duy Cho Trẻ",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Những Giai Điệu Bất Hủ",
#     "TenNXB_input": "NXB Âm Nhạc",
#     "NamXB": "2008"
#   },
#   {
#     "TenDauSach_input": "Những Giai Điệu Bất Hủ",
#     "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "An Ninh Mạng Cơ Bản",
#     "TenNXB_input": "NXB Thông Tin và Truyền Thông",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "An Ninh Mạng Cơ Bản",
#     "TenNXB_input": "NXB Khoa Học và Kỹ Thuật",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Hương Vị Quê Nhà",
#     "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Hương Vị Quê Nhà",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Chuyện Làng Nho",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2009"
#   },
#   {
#     "TenDauSach_input": "Chuyện Làng Nho",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Thế Giới Phẳng",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2007"
#   },
#   {
#     "TenDauSach_input": "Thế Giới Phẳng",
#     "TenNXB_input": "NXB Kinh Tế TP.HCM",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Những vì sao xa xôi",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2001"
#   },
#   {
#     "TenDauSach_input": "Những vì sao xa xôi",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Bức Tranh",
#     "TenNXB_input": "NXB Mỹ Thuật",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Bức Tranh",
#     "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Bản Giao Hưởng Định Mệnh",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Bản Giao Hưởng Định Mệnh",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Vũ Trụ Trong Vỏ Hạt Dẻ",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2003"
#   },
#   {
#     "TenDauSach_input": "Vũ Trụ Trong Vỏ Hạt Dẻ",
#     "TenNXB_input": "NXB Khoa Học và Kỹ Thuật",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Anna Karenina",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2008"
#   },
#   {
#     "TenDauSach_input": "Anna Karenina",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Khi Lỗi Thuộc Về Những Vì Sao",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2014"
#   },
#   {
#     "TenDauSach_input": "Khi Lỗi Thuộc Về Những Vì Sao",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Triết Lý Sống",
#     "TenNXB_input": "NXB Tri Thức",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Triết Lý Sống",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Bến Quê",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2005"
#   },
#   {
#     "TenDauSach_input": "Bến Quê",
#     "TenNXB_input": "NXB Giáo Dục Việt Nam",
#     "NamXB": "2015"
#   },
#   {
#     "TenDauSach_input": "Kỹ Năng Quản Lý Thời Gian",
#     "TenNXB_input": "NXB Lao Động",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Kỹ Năng Quản Lý Thời Gian",
#     "TenNXB_input": "NXB Thanh Niên",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "David Copperfield",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2010"
#   },
#   {
#     "TenDauSach_input": "David Copperfield",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Gia Đình",
#     "TenNXB_input": "NXB Phụ Nữ",
#     "NamXB": "2012"
#   },
#   {
#     "TenDauSach_input": "Gia Đình",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2021"
#   },
#   {
#     "TenDauSach_input": "Vòng Quanh Thế Giới",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2011"
#   },
#   {
#     "TenDauSach_input": "Vòng Quanh Thế Giới",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2019"
#   },
#   {
#     "TenDauSach_input": "Tuyển Tập Truyện Ngắn Nguyễn Huy Thiệp",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2009"
#   },
#   {
#     "TenDauSach_input": "Tuyển Tập Truyện Ngắn Nguyễn Huy Thiệp",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Cấu Trúc Dữ Liệu và Giải Thuật",
#     "TenNXB_input": "NXB Khoa Học và Kỹ Thuật",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Cấu Trúc Dữ Liệu và Giải Thuật",
#     "TenNXB_input": "NXB Đại Học Quốc Gia TP.HCM",
#     "NamXB": "2023"
#   },
#   {
#     "TenDauSach_input": "Thơ Tình Gửi Một Người",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2004"
#   },
#   {
#     "TenDauSach_input": "Thơ Tình Gửi Một Người",
#     "TenNXB_input": "NXB Hội Nhà Văn",
#     "NamXB": "2017"
#   },
#   {
#     "TenDauSach_input": "Vụ Án",
#     "TenNXB_input": "NXB Văn Học",
#     "NamXB": "2013"
#   },
#   {
#     "TenDauSach_input": "Vụ Án",
#     "TenNXB_input": "NXB Tư Pháp",
#     "NamXB": "2022"
#   },
#   {
#     "TenDauSach_input": "Chuyện Cũ Hà Nội",
#     "TenNXB_input": "NXB Hà Nội",
#     "NamXB": "2008"
#   },
#   {
#     "TenDauSach_input": "Chuyện Cũ Hà Nội",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2018"
#   },
#   {
#     "TenDauSach_input": "Đắc Nhân Tâm",
#     "TenNXB_input": "NXB Tổng Hợp TP.HCM",
#     "NamXB": "2005"
#   },
#   {
#     "TenDauSach_input": "Đắc Nhân Tâm",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "2016"
#   },
#   {
#     "TenDauSach_input": "Hồi Ký Chiến Tranh",
#     "TenNXB_input": "NXB Quân Đội Nhân Dân",
#     "NamXB": "2010"
#   },
#   {
#     "TenDauSach_input": "Hồi Ký Chiến Tranh",
#     "TenNXB_input": "NXB Chính Trị Quốc Gia Sự Thật",
#     "NamXB": "2020"
#   },
#   {
#     "TenDauSach_input": "Cô Gái Đến Từ Hôm Qua",
#     "TenNXB_input": "NXB Trẻ",
#     "NamXB": "1995"
#   },
#   {
#     "TenDauSach_input": "Cô Gái Đến Từ Hôm Qua",
#     "TenNXB_input": "NXB Kim Đồng",
#     "NamXB": "2014"
#   },
  {
    "TenDauSach_input": "Nghệ Thuật Sân Khấu",
    "TenNXB_input": "NXB Sân Khấu",
    "NamXB": "2012"
  },
  {
    "TenDauSach_input": "Nghệ Thuật Sân Khấu",
    "TenNXB_input": "NXB Văn Hóa - Văn Nghệ",
    "NamXB": "2021"
  },
  {
    "TenDauSach_input": "Bí Ẩn Về Cái Chết Của Marilyn Monroe",
    "TenNXB_input": "NXB Lao Động",
    "NamXB": "2019"
  },
  {
    "TenDauSach_input": "Bí Ẩn Về Cái Chết Của Marilyn Monroe",
    "TenNXB_input": "NXB Thanh Niên",
    "NamXB": "2023"
  },
  {
    "TenDauSach_input": "Anh Em Nhà Karamazov",
    "TenNXB_input": "NXB Văn Học",
    "NamXB": "2011"
  },
  {
    "TenDauSach_input": "Anh Em Nhà Karamazov",
    "TenNXB_input": "NXB Hội Nhà Văn",
    "NamXB": "2022"
  },
  {
    "TenDauSach_input": "Những Bài Học Giáo Dục Sớm",
    "TenNXB_input": "NXB Phụ Nữ",
    "NamXB": "2017"
  },
  {
    "TenDauSach_input": "Những Bài Học Giáo Dục Sớm",
    "TenNXB_input": "NXB Giáo Dục Việt Nam",
    "NamXB": "2023"
  },
  {
    "TenDauSach_input": "Lý Thuyết Trò Chơi và Ứng Dụng Kinh Tế",
    "TenNXB_input": "NXB Kinh Tế TP.HCM",
    "NamXB": "2018"
  },
  {
    "TenDauSach_input": "Lý Thuyết Trò Chơi và Ứng Dụng Kinh Tế",
    "TenNXB_input": "NXB Đại Học Quốc Gia TP.HCM",
    "NamXB": "2022"
  },
  {
    "TenDauSach_input": "Cẩm Nang Phòng Bệnh Tim Mạch",
    "TenNXB_input": "NXB Y Học",
    "NamXB": "2019"
  },
  {
    "TenDauSach_input": "Cẩm Nang Phòng Bệnh Tim Mạch",
    "TenNXB_input": "NXB Tổng Hợp TP.HCM",
    "NamXB": "2023"
  },
  {
    "TenDauSach_input": "Truyện Cười Hiện Đại",
    "TenNXB_input": "NXB Thanh Niên",
    "NamXB": "2015"
  },
  {
    "TenDauSach_input": "Truyện Cười Hiện Đại",
    "TenNXB_input": "NXB Lao Động",
    "NamXB": "2021"
  },
  {
    "TenDauSach_input": "Khởi Nghiệp Trong Thời Đại 4.0",
    "TenNXB_input": "NXB Trẻ",
    "NamXB": "2020"
  },
  {
    "TenDauSach_input": "Khởi Nghiệp Trong Thời Đại 4.0",
    "TenNXB_input": "NXB Thông Tin và Truyền Thông",
    "NamXB": "2024"
  },
  {
    "TenDauSach_input": "Đất Rừng Phương Nam",
    "TenNXB_input": "NXB Kim Đồng",
    "NamXB": "1997"
  },
  {
    "TenDauSach_input": "Đất Rừng Phương Nam",
    "TenNXB_input": "NXB Văn Học",
    "NamXB": "2014"
  },
  {
    "TenDauSach_input": "Xứ Đẹp",
    "TenNXB_input": "NXB Hội Nhà Văn",
    "NamXB": "2006"
  },
  {
    "TenDauSach_input": "Xứ Đẹp",
    "TenNXB_input": "NXB Trẻ",
    "NamXB": "2017"
  },
  {
    "TenDauSach_input": "Dạy Con Làm Giàu",
    "TenNXB_input": "NXB Trẻ",
    "NamXB": "2005"
  },
  {
    "TenDauSach_input": "Dạy Con Làm Giàu",
    "TenNXB_input": "NXB Phụ Nữ",
    "NamXB": "2018"
  }
]

success, failed = 0, 0

for item in sach_data:
    serializer = SachSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")