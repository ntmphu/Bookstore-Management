# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import KhachHangSerializer

khachhang_data = [
  # {
  #   "HoTen": "Nguyễn Văn An",
  #   "DiaChi": "123 Lê Lợi, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0901234567",
  #   "Email": "an.nguyenvan@gmail.com"
  # },
  # {
  #   "HoTen": "Trần Thị Bích",
  #   "DiaChi": "45 Hai Bà Trưng, Phường Tràng Tiền, Quận Hoàn Kiếm, Hà Nội",
  #   "DienThoai": "0987654321",
  #   "Email": "bich.tran@yahoo.com"
  # },
  # {
  #   "HoTen": "Lê Minh Cường",
  #   "DiaChi": "21A Nguyễn Văn Cừ, Phường An Hòa, Quận Ninh Kiều, Cần Thơ",
  #   "DienThoai": "0912345678",
  #   "Email": "cuong.le.minh@outlook.com"
  # },
  # {
  #   "HoTen": "Phạm Thị Dung",
  #   "DiaChi": "K10/2 Ngô Quyền, Phường An Hải Bắc, Quận Sơn Trà, Đà Nẵng",
  #   "DienThoai": "0355112233",
  #   "Email": "dungpham.88@gmail.com"
  # },
  # {
  #   "HoTen": "Hoàng Văn Em",
  #   "DiaChi": "Số 5, Ngõ 15, Đường Cầu Giấy, Quận Cầu Giấy, Hà Nội",
  #   "DienThoai": "0778990011",
  #   "Email": "em.hoangvan@email.com"
  # },
  # {
  #   "HoTen": "Võ Ngọc Giang",
  #   "DiaChi": "30/4B Phan Chu Trinh, Phường 2, Quận Bình Thạnh, TP. Hồ Chí Minh",
  #   "DienThoai": "0868123456",
  #   "Email": "giangvo.ngoc95@gmail.com"
  # },
  # {
  #   "HoTen": "Đỗ Thuý Hằng",
  #   "DiaChi": "78 Trần Phú, Phường Hải Châu 1, Quận Hải Châu, Đà Nẵng",
  #   "DienThoai": "0935678901",
  #   "Email": "hang.dothuy@hotmail.com"
  # },
  # {
  #   "HoTen": "Bùi Quang Huy",
  #   "DiaChi": "101 Pasteur, Phường 6, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0944556677",
  #   "Email": "huybui.quang@yahoo.com"
  # },
  # {
  #   "HoTen": "Ngô Thanh Lan",
  #   "DiaChi": "190 Lạch Tray, Quận Ngô Quyền, Hải Phòng",
  #   "DienThoai": "0399887766",
  #   "Email": "lanngo.thanh@gmail.com"
  # },
  # {
  #   "HoTen": "Lý Thành Long",
  #   "DiaChi": "202 Nguyễn Thị Minh Khai, Phường Võ Thị Sáu, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0909112233",
  #   "Email": "long.lythanh@email.com"
  # },
  # {
  #   "HoTen": "Trịnh Thị Kim Oanh",
  #   "DiaChi": "Số 15, Đường 3/2, Phường 11, Quận 10, TP. Hồ Chí Minh",
  #   "DienThoai": "0918776655",
  #   "Email": "oanhtrinh.kim@gmail.com"
  # },
  # {
  #   "HoTen": "Dương Minh Phát",
  #   "DiaChi": "55 Nguyễn Trãi, Phường Bến Thành, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0977889900",
  #   "Email": "phat.duongminh@yahoo.com"
  # },
  # {
  #   "HoTen": "Huỳnh Tấn Sang",
  #   "DiaChi": "189 Điện Biên Phủ, Phường Đa Kao, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0367123789",
  #   "Email": "sang.huynh.tan@outlook.com"
  # },
  # {
  #   "HoTen": "Phan Thị Mỹ Tâm",
  #   "DiaChi": "222 Lý Thường Kiệt, Phường 14, Quận 11, TP. Hồ Chí Minh",
  #   "DienThoai": "0908334455",
  #   "Email": "tamphan.my@gmail.com"
  # },
  # {
  #   "HoTen": "Vũ Anh Tuấn",
  #   "DiaChi": "333 Xô Viết Nghệ Tĩnh, Phường 25, Quận Bình Thạnh, TP. Hồ Chí Minh",
  #   "DienThoai": "0988990011",
  #   "Email": "tuanvu.anh90@email.com"
  # },
  # {
  #   "HoTen": "Nguyễn Thị Kim Chi",
  #   "DiaChi": "444 Hoàng Diệu, Phường 5, Quận 4, TP. Hồ Chí Minh",
  #   "DienThoai": "0913445566",
  #   "Email": "chi.nguyen.kim@gmail.com"
  # },
  # {
  #   "HoTen": "Trần Đức Bình",
  #   "DiaChi": "555 Cách Mạng Tháng Tám, Phường 15, Quận 10, TP. Hồ Chí Minh",
  #   "DienThoai": "0903556677",
  #   "Email": "binhtran.duc@yahoo.com"
  # },
  # {
  #   "HoTen": "Lê Ngọc Diệp",
  #   "DiaChi": "66 Bà Huyện Thanh Quan, Phường 6, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0933667788",
  #   "Email": "diep.le.ngoc@hotmail.com"
  # },
  # {
  #   "HoTen": "Phạm Văn Đồng",
  #   "DiaChi": "77 Sư Vạn Hạnh, Phường 12, Quận 10, TP. Hồ Chí Minh",
  #   "DienThoai": "0976778899",
  #   "Email": "dongpham.van@gmail.com"
  # },
  # {
  #   "HoTen": "Hoàng Minh Hải",
  #   "DiaChi": "88 Võ Văn Tần, Phường 6, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0902889900",
  #   "Email": "hai.hoang.minh@email.com"
  # },
  # {
  #   "HoTen": "Võ Thị Thu Hà",
  #   "DiaChi": "99 Nguyễn Du, Phường Bến Thành, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0911990011",
  #   "Email": "havothu@gmail.com"
  # },
  # {
  #   "HoTen": "Đặng Quốc Hùng",
  #   "DiaChi": "111 Đinh Tiên Hoàng, Phường Đa Kao, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0945001122",
  #   "Email": "hung.dangquoc@yahoo.com"
  # },
  # {
  #   "HoTen": "Bùi Thị Lan Hương",
  #   "DiaChi": "135 Nam Kỳ Khởi Nghĩa, Phường Bến Thành, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0966112233",
  #   "Email": "huongbui.lan@outlook.com"
  # },
  # {
  #   "HoTen": "Ngô Gia Khiêm",
  #   "DiaChi": "147 Lê Thánh Tôn, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0989223344",
  #   "Email": "khiem.ngo.gia@gmail.com"
  # },
  # {
  #   "HoTen": "Lý Mỹ Lệ",
  #   "DiaChi": "159 Đồng Khởi, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0907334455",
  #   "Email": "lely.my92@email.com"
  # },
  # {
  #   "HoTen": "Trịnh Hoài Nam",
  #   "DiaChi": "171 Hàm Nghi, Phường Nguyễn Thái Bình, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0917445566",
  #   "Email": "nam.trinh.hoai@gmail.com"
  # },
  # {
  #   "HoTen": "Dương Tuyết Nhung",
  #   "DiaChi": "183 Trần Hưng Đạo, Phường Cầu Ông Lãnh, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0938556677",
  #   "Email": "nhungduong.tuyet@yahoo.com"
  # },
  # {
  #   "HoTen": "Huỳnh Thanh Phong",
  #   "DiaChi": "205 An Dương Vương, Phường 8, Quận 5, TP. Hồ Chí Minh",
  #   "DienThoai": "0949667788",
  #   "Email": "phong.huynhthanh@hotmail.com"
  # },
  # {
  #   "HoTen": "Phan Minh Quân",
  #   "DiaChi": "217 Nguyễn Văn Cừ, Phường 2, Quận 5, TP. Hồ Chí Minh",
  #   "DienThoai": "0968778899",
  #   "Email": "quanphan.minh@gmail.com"
  # },
  # {
  #   "HoTen": "Vũ Diễm Quỳnh",
  #   "DiaChi": "229 Trần Bình Trọng, Phường 4, Quận 5, TP. Hồ Chí Minh",
  #   "DienThoai": "0982889900",
  #   "Email": "quynhvu.diem@email.com"
  # },
  # {
  #   "HoTen": "Nguyễn Hoàng Sơn",
  #   "DiaChi": "241 Hùng Vương, Phường 9, Quận 5, TP. Hồ Chí Minh",
  #   "DienThoai": "0906990011",
  #   "Email": "son.nguyen.hoang@gmail.com"
  # },
  # {
  #   "HoTen": "Trần Ngọc Thảo",
  #   "DiaChi": "253 Lý Thái Tổ, Phường 9, Quận 10, TP. Hồ Chí Minh",
  #   "DienThoai": "0916001122",
  #   "Email": "thaotran.ngoc@yahoo.com"
  # },
  # {
  #   "HoTen": "Lê Anh Tú",
  #   "DiaChi": "265 Điện Biên Phủ, Phường 7, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0937112233",
  #   "Email": "tule.anh@outlook.com"
  # },
  # {
  #   "HoTen": "Phạm Thanh Tùng",
  #   "DiaChi": "277 Hai Bà Trưng, Phường 8, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0978223344",
  #   "Email": "tungpham.thanh@gmail.com"
  # },
  # {
  #   "HoTen": "Hoàng Thị Uyên",
  #   "DiaChi": "289 Phan Đình Phùng, Phường 15, Quận Phú Nhuận, TP. Hồ Chí Minh",
  #   "DienThoai": "0901334455",
  #   "Email": "uyen.hoang.thi@email.com"
  # },
  # {
  #   "HoTen": "Võ Minh Vương",
  #   "DiaChi": "301 Hoàng Văn Thụ, Phường 2, Quận Tân Bình, TP. Hồ Chí Minh",
  #   "DienThoai": "0912445566",
  #   "Email": "vuongvo.minh@gmail.com"
  # },
  # {
  #   "HoTen": "Đỗ Hoàng Yến",
  #   "DiaChi": "313 Trường Chinh, Phường 14, Quận Tân Bình, TP. Hồ Chí Minh",
  #   "DienThoai": "0932556677",
  #   "Email": "yen.do.hoang@yahoo.com"
  # },
  # {
  #   "HoTen": "Bùi Xuân An",
  #   "DiaChi": "325 Cộng Hòa, Phường 13, Quận Tân Bình, TP. Hồ Chí Minh",
  #   "DienThoai": "0946667788",
  #   "Email": "an.bui.xuan@hotmail.com"
  # },
  # {
  #   "HoTen": "Ngô Văn Bảo",
  #   "DiaChi": "337 Âu Cơ, Phường Phú Trung, Quận Tân Phú, TP. Hồ Chí Minh",
  #   "DienThoai": "0967778899",
  #   "Email": "baongo.van@gmail.com"
  # },
  # {
  #   "HoTen": "Lý Thị Cẩm",
  #   "DiaChi": "349 Lũy Bán Bích, Phường Hiệp Tân, Quận Tân Phú, TP. Hồ Chí Minh",
  #   "DienThoai": "0981889900",
  #   "Email": "cam.ly.thi@email.com"
  # },
  # {
  #   "HoTen": "Trịnh Minh Đức",
  #   "DiaChi": "361 Kinh Dương Vương, Phường An Lạc, Quận Bình Tân, TP. Hồ Chí Minh",
  #   "DienThoai": "0905990011",
  #   "Email": "duc.trinh.minh@gmail.com"
  # },
  # {
  #   "HoTen": "Dương Thị Hồng Gấm",
  #   "DiaChi": "373 Tên Lửa, Phường Bình Trị Đông B, Quận Bình Tân, TP. Hồ Chí Minh",
  #   "DienThoai": "0915001122",
  #   "Email": "gamduong.hong@yahoo.com"
  # },
  # {
  #   "HoTen": "Huỳnh Quốc Hiệp",
  #   "DiaChi": "385 Võ Văn Kiệt, Phường Cô Giang, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0936112233",
  #   "Email": "hiep.huynh.quoc@outlook.com"
  # },
  # {
  #   "HoTen": "Phan Thị Thanh Huyền",
  #   "DiaChi": "397 Nguyễn Tri Phương, Phường 5, Quận 10, TP. Hồ Chí Minh",
  #   "DienThoai": "0971223344",
  #   "Email": "huyenphan.thanh@gmail.com"
  # },
  # {
  #   "HoTen": "Vũ Đức Kiên",
  #   "DiaChi": "409 Ba Tháng Hai, Phường 10, Quận 10, TP. Hồ Chí Minh",
  #   "DienThoai": "0904334455",
  #   "Email": "kienvu.duc@email.com"
  # },
  # {
  #   "HoTen": "Nguyễn Thùy Linh",
  #   "DiaChi": "25 Ngô Thời Nhiệm, Phường 6, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0914445566",
  #   "Email": "linh.nguyen.thuy@gmail.com"
  # },
  # {
  #   "HoTen": "Trần Văn Mạnh",
  #   "DiaChi": "37 Tôn Đức Thắng, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0934556677",
  #   "Email": "manhtran.van@yahoo.com"
  # },
  # {
  #   "HoTen": "Lê Thị Nga",
  #   "DiaChi": "48 Nguyễn Bỉnh Khiêm, Phường Đa Kao, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0948667788",
  #   "Email": "ngale.thi@hotmail.com"
  # },
  # {
  #   "HoTen": "Phạm Quang Ninh",
  #   "DiaChi": "52 Thạch Thị Thanh, Phường Tân Định, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0969778899",
  #   "Email": "ninhpham.quang@gmail.com"
  # },
  # {
  #   "HoTen": "Hoàng Kim Phượng",
  #   "DiaChi": "63 Mạc Đĩnh Chi, Phường Đa Kao, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0983889900",
  #   "Email": "phuong.hoang.kim@email.com"
  # },
  # {
  #   "HoTen": "Võ Tấn Phát",
  #   "DiaChi": "75 Hai Bà Trưng, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0908990011",
  #   "Email": "phat.vo.tan@gmail.com"
  # },
  # {
  #   "HoTen": "Đỗ Minh Quân",
  #   "DiaChi": "86 Lê Quý Đôn, Phường 6, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0918001122",
  #   "Email": "quando.minh@yahoo.com"
  # },
  # {
  #   "HoTen": "Bùi Thanh Thủy",
  #   "DiaChi": "97 Trương Định, Phường 6, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0939112233",
  #   "Email": "thuybui.thanh@outlook.com"
  # },
  # {
  #   "HoTen": "Ngô Bích Trâm",
  #   "DiaChi": "108 Bà Huyện Thanh Quan, Phường 9, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0972223344",
  #   "Email": "tramngo.bich@gmail.com"
  # },
  # {
  #   "HoTen": "Lý Gia Huy",
  #   "DiaChi": "119 Tú Xương, Phường 7, Quận 3, TP. Hồ Chí Minh",
  #   "DienThoai": "0902334455",
  #   "Email": "huy.ly.gia@email.com"
  # },
  # {
  #   "HoTen": "Trịnh Ngọc Anh",
  #   "DiaChi": "130 Điện Biên Phủ, Phường 17, Quận Bình Thạnh, TP. Hồ Chí Minh",
  #   "DienThoai": "0913245546",
  #   "Email": "anh.trinh.ngoc@gmail.com"
  # },
  # {
  #   "HoTen": "Dương Văn Toàn",
  #   "DiaChi": "141 D5, Phường 25, Quận Bình Thạnh, TP. Hồ Chí Minh",
  #   "DienThoai": "0931556677",
  #   "Email": "toan.duongvan@yahoo.com"
  # },
  # {
  #   "HoTen": "Huỳnh Thị Thu",
  #   "DiaChi": "152 Ung Văn Khiêm, Phường 25, Quận Bình Thạnh, TP. Hồ Chí Minh",
  #   "DienThoai": "0941667788",
  #   "Email": "thuhuynh.thi@hotmail.com"
  # },
  # {
  #   "HoTen": "Phan Văn Tài",
  #   "DiaChi": "163 Nguyễn Hữu Cảnh, Phường 22, Quận Bình Thạnh, TP. Hồ Chí Minh",
  #   "DienThoai": "0961778899",
  #   "Email": "taiphan.van@gmail.com"
  # },
  # {
  #   "HoTen": "Vũ Thị Vân",
  #   "DiaChi": "174 Phan Xích Long, Phường 2, Quận Phú Nhuận, TP. Hồ Chí Minh",
  #   "DienThoai": "0321880910",
  #   "Email": "vanvu.thi@email.com"
  # },
  # {
  #   "HoTen": "Nguyễn Minh Việt",
  #   "DiaChi": "185 Hoa Lan, Phường 2, Quận Phú Nhuận, TP. Hồ Chí Minh",
  #   "DienThoai": "0901990011",
  #   "Email": "viet.nguyen.minh@gmail.com"
  # },
  # {
  #   "HoTen": "Trần Quốc Tuấn",
  #   "DiaChi": "20 Ngô Đức Kế, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0911001122",
  #   "Email": "tuantran.quoc@yahoo.com"
  # },
  # {
  #   "HoTen": "Lê Thị Thúy",
  #   "DiaChi": "31 Tôn Thất Thiệp, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0931112233",
  #   "Email": "thuyle.thi@outlook.com"
  # },
  # {
  #   "HoTen": "Phạm Hồng Phúc",
  #   "DiaChi": "42 Hồ Tùng Mậu, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0971621445",
  #   "Email": "phucpham.hong@gmail.com"
  # },
  # {
  #   "HoTen": "Hoàng Văn Trung",
  #   "DiaChi": "53 Hải Triều, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0921343456",
  #   "Email": "trung.hoang.van@email.com"
  # },
  # {
  #   "HoTen": "Võ Thị Xuân",
  #   "DiaChi": "64 Tôn Thất Đạm, Phường Nguyễn Thái Bình, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0911445566",
  #   "Email": "xuanvo.thi@gmail.com"
  # },
  # {
  #   "HoTen": "Đỗ Gia Bảo",
  #   "DiaChi": "75 Calmette, Phường Nguyễn Thái Bình, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0921576579",
  #   "Email": "bao.do.gia@yahoo.com"
  # },
  # {
  #   "HoTen": "Bùi Mai Anh",
  #   "DiaChi": "86 Ký Con, Phường Nguyễn Thái Bình, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0941658781",
  #   "Email": "anhbui.mai@hotmail.com"
  # },
  # {
  #   "HoTen": "Ngô Đình Trọng",
  #   "DiaChi": "97 Yersin, Phường Cầu Ông Lãnh, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0961778819",
  #   "Email": "trong.ngo.dinh@gmail.com"
  # },
  # {
  #   "HoTen": "Lý Thanh Trúc",
  #   "DiaChi": "108 Nguyễn Công Trứ, Phường Nguyễn Thái Bình, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0981885900",
  #   "Email": "truc.ly.thanh@email.com"
  # },
  # {
  #   "HoTen": "Trịnh Văn Quyết",
  #   "DiaChi": "119 Phó Đức Chính, Phường Nguyễn Thái Bình, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0901990012",
  #   "Email": "quyet.trinh.van@gmail.com"
  # },
  # {
  #   "HoTen": "Dương Thùy Dương",
  #   "DiaChi": "130 Pasteur, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
  #   "DienThoai": "0919001122",
  #   "Email": "duongduong.thuy@yahoo.com"
  # }
  {
    "HoTen": "Nguyễn Thắng Lợi",
    "DiaChi": "Landmark 81, Quận Bình Thạnh, TP. Hồ Chí Minh",
    "DienThoai": "0375551352",
    "Email": "loi27652023@gmail.com"
  },
  {
    "HoTen": "Dương Tấn Lộc",
    "DiaChi": "Ký túc xá khu B, TP. Thủ Đức",
    "DienThoai": "0489384094",
    "Email": "loc@gmail.com"
  },
  {
    "HoTen": "Võ Anh Kiệt",
    "DiaChi": "Vũng Tàu",
    "DienThoai": "0438290741",
    "Email": "kiet@gmail.com"
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