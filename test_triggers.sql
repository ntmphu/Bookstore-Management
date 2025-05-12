INSERT INTO api_thamso (SLNhapTT, TonTD, NoTD, TonTT, TiLe, SDQD4) VALUES (150, 300, 1000000, 20, 1.05, 1);

INSERT INTO api_theloai (tentheloai) VALUES 
('Khoa học viễn tưởng'),
('Lịch sử'),
('Văn học Việt Nam'),
('Kinh doanh'),
('Tâm lý học'),
('Thiếu nhi'),
('Công nghệ thông tin'),
('Triết học'),
('Nghệ thuật'),
('Du ký');

INSERT INTO api_tacgia (TenTG) VALUES
('Nguyễn Nhật Ánh'),
('Dan Brown'),
('Yuval Noah Harari'),
('Stephen Hawking'),
('J.K. Rowling'),
('Ngô Bảo Châu');

INSERT INTO api_dausach (TenSach, MaTheLoai_id) VALUES
('Mắt Biếc', 3),
('The Da Vinci Code', 1),
('Sapiens: A Brief History of Humankind', 2),
('A Brief History of Time', 1),
('Harry Potter and the Sorcerer''s Stone', 6),
('Từ Điển Toán Học Hiện Đại', 7);

INSERT INTO api_dausach_MaTG (dausach_id, tacgia_id) VALUES
(1, 1),  -- Mắt Biếc by Nguyễn Nhật Ánh
(2, 2),  -- The Da Vinci Code by Dan Brown
(3, 3),  -- Sapiens by Yuval Noah Harari
(4, 4),  -- A Brief History of Time by Stephen Hawking
(5, 5),  -- Harry Potter by J.K. Rowling
(6, 6);  -- Từ Điển Toán Học by Ngô Bảo Châu

-- SELECT ds.TenSach, tg.TenTG, tl.TenTheLoai
-- FROM api_dausach ds
-- JOIN api_dausach_MaTG dstg ON ds.MaDauSach = dstg.dausach_id
-- JOIN api_tacgia tg ON dstg.tacgia_id = tg.MaTG
-- JOIN api_theloai tl ON ds.MaTheLoai_id = tl.MaTheLoai;

INSERT INTO api_sach (NXB, NamXB, MaDauSach_id) VALUES
('NXB Trẻ', 2020, 1),     -- Mắt Biếc
('NXB Random House', 2018, 2),   -- The Da Vinci Code
('NXB Omega Plus', 2019, 3),     -- Sapiens
('NXB Bantam Books', 2015, 4),   -- A Brief History of Time
('NXB Bloomsbury', 2010, 5),    -- Harry Potter
('NXB Giáo Dục', 2021, 6);       -- Từ Điển Toán Học

INSERT INTO api_phieunhapsach (NgayNhap, NguoiNhap_id) VALUES
('2025-05-01', 1),
('2025-05-03', 1),
('2025-05-06', 1);

-- Chi tiết cho Phiếu Nhập 1
INSERT INTO api_ct_nhapsach (SLNhap, GiaNhap, MaPhieuNhap_id, MaSach_id) VALUES
(150, 50000, 1, 1),
(200,  120000, 1, 2),
(300,  150000, 1, 3);

-- Chi tiết cho Phiếu Nhập 2
INSERT INTO api_ct_nhapsach (SLNhap, GiaNhap, MaPhieuNhap_id, MaSach_id) VALUES
(300,  200000, 2, 4),
(200,   95000, 2, 5);

-- Chi tiết cho Phiếu Nhập 3
-- INSERT INTO api_ct_nhapsach (SLNhap, GiaNhap, MaPhieuNhap_id, MaSach_id) VALUES
-- (150, 175000, 3, 6),
-- (2, 50000, 3, 1); -- will raise error

INSERT INTO api_ct_nhapsach (SLNhap, GiaNhap, MaPhieuNhap_id, MaSach_id) VALUES
(150, 175000, 3, 6),
(200, 50000, 3, 1);

INSERT INTO api_khachhang (HoTen, DiaChi, DienThoai, Email) VALUES
('Nguyễn Văn A', '123 Lý Thường Kiệt, Q.10, TP.HCM', '0909123456', 'nguyenvana@gmail.com'),
('Trần Thị B', '45 Nguyễn Trãi, Q.5, TP.HCM', '0912345678', 'tranthib@yahoo.com'),
('Lê Văn C', 'Số 8 Trần Hưng Đạo, Hà Nội', '0988765432', 'levanc@gmail.com'),
('Phạm Thị D', '222 Hai Bà Trưng, Đà Nẵng', '0933456789', 'phamthid@hotmail.com'),
('Đỗ Minh E', '99 Nguyễn Huệ, Huế', '0977654321', 'dminhe@outlook.com');
INSERT INTO api_khachhang (HoTen, DiaChi, DienThoai, Email) VALUES
('Võ Hữu Long', '12 Nguyễn Văn Cừ, Quận 1, TP.HCM', '0909988776', 'longvo@example.com');

INSERT INTO api_hoadon (NgayLap, SoTienTra, NguoiLapHD_id, MaKH_id) VALUES
('2025-05-01', 150000, 1, 1),   -- Khách 1 thanh toán đủ
('2025-05-02', 150000, 1, 2), -- Khách 2 còn nợ
('2025-05-03', 180000, 1, 3), -- Khách 3 còn nợ nhiều
('2025-05-04', 100000, 1, 4),   -- Khách 4 thanh toán đủ
('2025-05-05', 100000, 1, 5); -- Khách 5 còn nợ nhẹ

-- Hóa đơn 1: Khách 1 mua 3 cuốn Mắt Biếc, 2 cuốn Da Vinci Code
INSERT INTO api_ct_hoadon (SLBan, MaHD_id, MaSach_id) VALUES
(3, 1, 1),
(2, 1, 2);

-- Hóa đơn 2: Khách 2 mua 1 cuốn Sapiens, 2 cuốn Harry Potter
INSERT INTO api_ct_hoadon (SLBan, MaHD_id, MaSach_id) VALUES
(1, 2, 3),
(2, 2, 5);

-- Hóa đơn 3: Khách 3 mua 2 cuốn A Brief History, 2 cuốn Từ Điển Toán
INSERT INTO api_ct_hoadon (SLBan, MaHD_id, MaSach_id) VALUES
(2, 3, 4),
(2, 3, 6);

-- Hóa đơn 4: Khách 4 mua 2 cuốn Harry Potter
INSERT INTO api_ct_hoadon (SLBan, MaHD_id, MaSach_id) VALUES
(2, 4, 5);

-- Hóa đơn 5: Khách 5 mua 1 cuốn Mắt Biếc, 1 cuốn Từ Điển Toán
INSERT INTO api_ct_hoadon (SLBan, MaHD_id, MaSach_id) VALUES
(1, 5, 1),
(1, 5, 6);


INSERT INTO api_hoadon (NgayLap, SoTienTra, NguoiLapHD_id, MaKH_id) VALUES
('2025-05-06', 250000, 1, 6);

-- Khách này mua số lượng lớn các sách khác nhau
INSERT INTO api_ct_hoadon (SLBan, MaHD_id, MaSach_id) VALUES
(5, 6, 1),  -- Mắt Biếc
(4, 6, 3), -- Sapiens
(3, 6, 4), -- A Brief History of Time
(5, 6, 6); -- Từ Điển Toán Học

-- Khách 2 trả 20.000 (nợ trước 50.000)
INSERT INTO api_phieuthutien (NgayThu, SoTienThu, MaKH_id, NguoiThu_id) VALUES
('2025-05-07', 20000, 2, 1);

-- Khách 2 trả 20.000 (nợ trước 50.000)
INSERT INTO api_phieuthutien (NgayThu, SoTienThu, MaKH_id, NguoiThu_id) VALUES
('2025-05-07', 20000, 2, 1);

-- Khách 3 trả 100.000 (nợ trước 120.000)
INSERT INTO api_phieuthutien (NgayThu, SoTienThu, MaKH_id, NguoiThu_id) VALUES
('2025-05-08', 100000, 3, 1);

-- Khách 5 trả 20.000 (nợ trước 20.000 → trả hết)
INSERT INTO api_phieuthutien (NgayThu, SoTienThu, MaKH_id, NguoiThu_id) VALUES
('2025-05-08', 30000, 5, 1);

-- Khách 5 trả 20.000 (nợ trước 20.000 → trả hết)
INSERT INTO api_phieuthutien (NgayThu, SoTienThu, MaKH_id, NguoiThu_id) VALUES
('2025-05-08', 20000, 5, 1);

-- Khách 6 (Võ Hữu Long) trả 500.000 (nợ trước 1.250.000)
INSERT INTO api_phieuthutien (NgayThu, SoTienThu, MaKH_id, NguoiThu_id) VALUES
('2025-05-09', 500000, 6, 1);

-- Báo cáo tồn kho tháng 5 năm 2025
INSERT INTO api_baocaoton (Thang, Nam) VALUES
(5, 2025);

-- Chi tiết báo cáo tồn kho tháng 5 năm 2025 cho các sách
INSERT INTO api_ct_bcton (MaBCTon_id, MaSach_id) VALUES
(1, 1),  -- Mắt Biếc: Tồn đầu 10, phát sinh 5, tồn cuối 15
(1, 2),   -- The Da Vinci Code: Tồn đầu 8, phát sinh 2, tồn cuối 10
(1, 3),    -- Sapiens: Tồn đầu 5, phát sinh 3, tồn cuối 8
(1, 4),    -- A Brief History of Time: Tồn đầu 3, phát sinh 2, tồn cuối 5
(1, 5),  -- Harry Potter: Tồn đầu 12, phát sinh 1, tồn cuối 13
(1, 6);    -- Từ Điển Toán Học: Tồn đầu 6, phát sinh 2, tồn cuối 8

-- Báo cáo công nợ tháng 5 năm 2025
INSERT INTO api_baocaocongno (Thang, Nam)
VALUES (5, 2025);

-- Chi tiết báo cáo công nợ cho 6 khách hàng
INSERT INTO api_ct_bccongno (MaBCCN_id, MaKH_id) VALUES
(1, 1),  -- Khách 1: nợ phát sinh 50k, đã trả 20k
(1, 2),  -- Khách 2: nợ mới
(1, 3),  -- Khách 3: nợ cũ trả bớt
(1, 4),  -- Khách 4: không phát sinh
(1, 5),  -- Khách 5: phát sinh và trả hết
(1, 6);  -- Khách 6: nợ lớn, trả một phần