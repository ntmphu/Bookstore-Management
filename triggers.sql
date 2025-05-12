ALTER TABLE api_sach RENAME COLUMN SLTon TO SLTon_OLD;
ALTER TABLE api_sach ADD SLTon INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_sach DROP COLUMN SLTon_OLD;

ALTER TABLE api_khachhang RENAME COLUMN SoTienNo TO SoTienNo_OLD;
ALTER TABLE api_khachhang ADD SoTienNo INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_khachhang DROP COLUMN SoTienNo_OLD;

ALTER TABLE api_hoadon RENAME COLUMN TongTien TO TongTien_OLD;
ALTER TABLE api_hoadon ADD TongTien INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_hoadon DROP COLUMN TongTien_OLD;

ALTER TABLE api_hoadon RENAME COLUMN ConLai TO ConLai_OLD;
ALTER TABLE api_hoadon ADD ConLai INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_hoadon DROP COLUMN ConLai_OLD;

ALTER TABLE api_ct_hoadon RENAME COLUMN GiaBan TO GiaBan_OLD;
ALTER TABLE api_ct_hoadon ADD GiaBan INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_hoadon DROP COLUMN GiaBan_OLD;

ALTER TABLE api_ct_hoadon RENAME COLUMN ThanhTien TO ThanhTien_OLD;
ALTER TABLE api_ct_hoadon ADD ThanhTien INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_hoadon DROP COLUMN ThanhTien_OLD;

ALTER TABLE api_ct_bcton RENAME COLUMN TonDau TO TonDau_OLD;
ALTER TABLE api_ct_bcton ADD TonDau INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_bcton DROP COLUMN TonDau_OLD;

ALTER TABLE api_ct_bcton RENAME COLUMN PhatSinh TO PhatSinh_OLD;
ALTER TABLE api_ct_bcton ADD PhatSinh INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_bcton DROP COLUMN PhatSinh_OLD;

ALTER TABLE api_ct_bcton RENAME COLUMN TonCuoi TO TonCuoi_OLD;
ALTER TABLE api_ct_bcton ADD TonCuoi INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_bcton DROP COLUMN TonCuoi_OLD;

ALTER TABLE api_ct_bccongno RENAME COLUMN NoDau TO NoDau_OLD;
ALTER TABLE api_ct_bccongno ADD NoDau INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_bccongno DROP COLUMN NoDau_OLD;

ALTER TABLE api_ct_bccongno RENAME COLUMN PhatSinh TO PhatSinh_OLD;
ALTER TABLE api_ct_bccongno ADD PhatSinh INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_bccongno DROP COLUMN PhatSinh_OLD;

ALTER TABLE api_ct_bccongno RENAME COLUMN NoCuoi TO NoCuoi_OLD;
ALTER TABLE api_ct_bccongno ADD NoCuoi INTEGER DEFAULT 0 NOT NULL;
ALTER TABLE api_ct_bccongno DROP COLUMN NoCuoi_OLD;

CREATE TRIGGER KT_QD1_INSERT
BEFORE INSERT ON api_CT_NhapSach
FOR EACH ROW
BEGIN
    SELECT CASE 
        WHEN NEW.SLNhap < (SELECT SLNhapTT FROM api_thamso WHERE id = 1)
        THEN RAISE(ABORT, 'Quy định 1: Số lượng nhập nhỏ hơn số lượng nhập tối thiểu')
        WHEN (SELECT SLTon FROM api_Sach WHERE MaSach = NEW.MaSach_id) >= (SELECT TonTD FROM api_thamso WHERE id = 1)
        THEN RAISE(ABORT, 'Quy định 1: Số lượng tồn của sách vượt quá mức tồn tối đa')
        WHEN NEW.SLNhap < 0
        THEN RAISE(ABORT, 'Số lượng nhập không được nhỏ hơn 0')
    END;
END;

CREATE TRIGGER KT_QD1_UPDATE
BEFORE UPDATE ON api_CT_NhapSach
FOR EACH ROW
BEGIN
    SELECT CASE 
        WHEN NEW.SLNhap < (SELECT SLNhapTT FROM api_thamso WHERE id = 1)
        THEN RAISE(ABORT, 'Quy định 1: Số lượng nhập nhỏ hơn số lượng nhập tối thiểu')
        WHEN (SELECT SLTon FROM api_Sach WHERE MaSach = NEW.MaSach_id) >= (SELECT TonTD FROM api_thamso WHERE id = 1)
        THEN RAISE(ABORT, 'Quy định 1: Số lượng tồn của sách lớn hơn mức tồn tối đa')
        WHEN NEW.SLNhap < 0
        THEN RAISE(ABORT, 'Số lượng nhập không được nhỏ hơn 0')
    END;
END;

CREATE TRIGGER KT_QD2_INSERT_HOADON
BEFORE INSERT ON api_HoaDon
FOR EACH ROW
BEGIN
    SELECT CASE 
        WHEN (SELECT SoTienNo FROM api_KhachHang WHERE MaKhachHang = NEW.MaKH_id) > (SELECT NoTD FROM api_thamso WHERE id = 1)
        THEN RAISE(ABORT, 'Quy định 2: Không được bán cho khách hàng có số tiền nợ lớn hơn số tiền nợ tối đa')
    END;
END;

CREATE TRIGGER KT_QD2_INSERT_CT_HOADON
BEFORE INSERT ON api_CT_HoaDon
FOR EACH ROW
BEGIN
    SELECT CASE 
        WHEN (
            SELECT SUM(S.SLTon) 
            FROM api_Sach S 
            WHERE S.MaDauSach_id = (SELECT MaDauSach_id FROM api_sach WHERE api_sach.MaSach = NEW.MaSach_id)
        ) - NEW.SLBan < (SELECT TonTT FROM api_thamso WHERE id = 1)
        THEN RAISE(ABORT, 'Quy định 2: Số lượng tồn của đầu sách sau khi bán phải ít nhất là số tồn tối thiểu')
        WHEN NEW.SLBan < 0
        THEN RAISE(ABORT, 'Số lượng bán không được nhỏ hơn 0')
    END;
END;

CREATE TRIGGER KT_QD2_INSERT_GIABAN
AFTER INSERT ON api_CT_HoaDon
FOR EACH ROW
BEGIN
    -- Assign GiaBan directly
    UPDATE api_CT_HoaDon 
	SET GiaBan = (
            SELECT GiaNhap * TiLe
            FROM api_CT_NhapSach, api_thamso
            WHERE api_CT_NhapSach.MaSach_id = NEW.MaSach_id
              AND api_thamso.id = 1
            ORDER BY MaPhieuNhap_id DESC
            LIMIT 1
        )
	WHERE id = NEW.id;

    -- Assign ThanhTien directly
    UPDATE api_CT_HoaDon
	SET ThanhTien = NEW.SLBan * GiaBan
	WHERE id = NEW.id;
END;


-- DROP TRIGGER KT_QD2_INSERT_GIABAN

-- CREATE TRIGGER KT_QD2_UPDATE
-- AFTER UPDATE ON api_CT_HoaDon
-- FOR EACH ROW
-- BEGIN
--     SELECT CASE 
--         WHEN (SELECT SoTienNo FROM api_KhachHang WHERE MaKhachHang = (SELECT MaKH_id FROM api_HoaDon WHERE MaHD = NEW.MaHD_id)) > (SELECT NoTD FROM api_thamso WHERE id = 1)
--         THEN RAISE(ABORT, 'Quy định 2: Không được bán cho khách hàng có số tiền nợ lớn hơn số tiền nợ tối đa')
--         WHEN (
--             SELECT SUM(S.SLTon) 
--             FROM api_Sach S 
--             WHERE S.MaDauSach_id = (SELECT MaDauSach_id FROM api_sach WHERE api_sach.MaSach = NEW.MaSach_id)
--         ) - NEW.SLBan < (SELECT TonTT FROM api_thamso WHERE id = 1)
--         THEN RAISE(ABORT, 'Quy định 2: Số lượng tồn của đầu sách sau khi bán phải ít nhất là số tồn tối thiểu')
--         WHEN NEW.SLBan < 0
--         THEN RAISE(ABORT, 'Số lượng bán không được nhỏ hơn 0')
--         WHEN NEW.GiaBan != (SELECT GiaNhap * (SELECT TiLe FROM api_thamso WHERE id = 1) FROM api_CT_NhapSach WHERE MaSach_id = NEW.MaSach_id ORDER BY MaPhieuNhap_id DESC LIMIT 1)
--         THEN RAISE(ABORT, 'Quy định 2: Đơn giá bán phải bằng đơn giá nhập nhân với tỉ lệ')
--     END;
-- END;

-- DROP TRIGGER KT_QD2_UPDATE

CREATE TRIGGER KT_QD4_INSERT
BEFORE INSERT ON api_PhieuThuTien
FOR EACH ROW
BEGIN
    SELECT CASE 
        WHEN NEW.SoTienThu > (SELECT SoTienNo FROM api_KhachHang WHERE MaKhachHang = NEW.MaKH_id)
        THEN RAISE(ABORT, 'Quy định 4: Số tiền thu không được vượt quá số tiền khách hàng đang nợ')
        WHEN NEW.SoTienThu < 0
        THEN RAISE(ABORT, 'Số tiền thu không được nhỏ hơn 0')
    END;
END;

CREATE TRIGGER KT_QD4_UPDATE
BEFORE UPDATE ON api_PhieuThuTien
FOR EACH ROW
BEGIN
    SELECT CASE 
        WHEN NEW.SoTienThu > (SELECT SoTienNo FROM api_KhachHang WHERE MaKhachHang = NEW.MaKH_id)
        THEN RAISE(ABORT, 'Quy định 4: Số tiền thu không được vượt quá số tiền khách hàng đang nợ')
        WHEN NEW.SoTienThu < 0
        THEN RAISE(ABORT, 'Số tiền thu không được nhỏ hơn 0')
    END;
END;

-- Trigger cập nhật số lượng tồn sau khi nhập
CREATE TRIGGER UPDATE_SLTON_AFTER_NHAP
AFTER INSERT ON api_CT_NhapSach
FOR EACH ROW
BEGIN
    UPDATE api_Sach 
    SET SLTon = SLTon + NEW.SLNhap
    WHERE MaSach = NEW.MaSach_id;
END;

-- Trigger cập nhật số lượng tồn sau khi bán
CREATE TRIGGER UPDATE_SLTON_AFTER_BAN
AFTER INSERT ON api_CT_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_Sach 
    SET SLTon = SLTon - NEW.SLBan
    WHERE MaSach = NEW.MaSach_id;
END;

-- Trigger cập nhật số lượng tồn sau khi cập nhật số lượng nhập
CREATE TRIGGER UPDATE_SLTON_AFTER_NHAP_UPDATE
AFTER UPDATE ON api_CT_NhapSach
FOR EACH ROW
BEGIN
    UPDATE api_Sach 
    SET SLTon = SLTon + (NEW.SLNhap - OLD.SLNhap)
    WHERE MaSach = NEW.MaSach_id;
END;

-- Trigger cập nhật số lượng tồn sau khi cập nhật số lượng bán
CREATE TRIGGER UPDATE_SLTON_AFTER_BAN_UPDATE
AFTER UPDATE ON api_CT_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_Sach 
    SET SLTon = SLTon + (OLD.SLBan - NEW.SLBan)
    WHERE MaSach = NEW.MaSach_id;
END;

-- Trigger tính thành tiền khi thêm CT hóa đơn
-- CREATE TRIGGER CALCULATE_THANHTIEN_INSERT
-- BEFORE INSERT ON api_CT_HoaDon
-- FOR EACH ROW
-- BEGIN
--     UPDATE api_CT_HoaDon 
--     SET ThanhTien = NEW.SLBan * NEW.GiaBan
--     WHERE ROWID = NEW.ROWID;
-- END;

-- Trigger tính thành tiền khi cập nhật CT hóa đơn
-- CREATE TRIGGER CALCULATE_THANHTIEN_UPDATE
-- AFTER UPDATE ON api_CT_HoaDon
-- FOR EACH ROW
-- BEGIN
--     UPDATE api_CT_HoaDon 
--     SET ThanhTien = NEW.SLBan * NEW.GiaBan
--     WHERE ROWID = NEW.ROWID;
-- END;

-- Trigger tính số tiền còn lại khi thêm hóa đơn
CREATE TRIGGER CALCULATE_CONLAI_INSERT
AFTER INSERT ON api_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_HoaDon 
    SET ConLai = NEW.TongTien - NEW.SoTienTra
    WHERE ROWID = NEW.ROWID;
END;

-- Trigger tính số tiền còn lại khi cập nhật hóa đơn
CREATE TRIGGER CALCULATE_CONLAI_UPDATE
AFTER UPDATE ON api_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_HoaDon 
    SET ConLai = NEW.TongTien - NEW.SoTienTra
    WHERE ROWID = NEW.ROWID;
END;

-- Trigger tính tổng tiền hóa đơn khi thêm CT_HoaDon
CREATE TRIGGER CALCULATE_INVOICE_TOTAL_INSERT
AFTER INSERT ON api_CT_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_HoaDon
    SET TongTien = (
        SELECT COALESCE(SUM(ThanhTien), 0)
        FROM api_CT_HoaDon
        WHERE MaHD_id = NEW.MaHD_id
    ),
    ConLai = (
        SELECT COALESCE(SUM(ThanhTien), 0)
        FROM api_CT_HoaDon
        WHERE MaHD_id = NEW.MaHD_id
    ) - SoTienTra
    WHERE MaHD = NEW.MaHD_id;
END;

-- Trigger tính tổng tiền hóa đơn khi cập nhật CT_HoaDon
CREATE TRIGGER CALCULATE_INVOICE_TOTAL_UPDATE
AFTER UPDATE ON api_CT_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_HoaDon
    SET TongTien = (
        SELECT COALESCE(SUM(ThanhTien), 0)
        FROM api_CT_HoaDon
        WHERE MaHD_id = NEW.MaHD_id
    ),
    ConLai = (
        SELECT COALESCE(SUM(ThanhTien), 0)
        FROM api_CT_HoaDon
        WHERE MaHD_id = NEW.MaHD_id
    ) - SoTienTra
    WHERE MaHD = NEW.MaHD_id;
END;

-- Trigger tính tổng tiền hóa đơn khi xóa CT_HoaDon
CREATE TRIGGER CALCULATE_INVOICE_TOTAL_DELETE
AFTER DELETE ON api_CT_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_HoaDon
    SET TongTien = (
        SELECT COALESCE(SUM(ThanhTien), 0)
        FROM api_CT_HoaDon
        WHERE MaHD_id = OLD.MaHD_id
    ),
    ConLai = (
        SELECT COALESCE(SUM(ThanhTien), 0)
        FROM api_CT_HoaDon
        WHERE MaHD_id = OLD.MaHD_id
    ) - SoTienTra
    WHERE MaHD = OLD.MaHD_id;
END;

-- Trigger tính số tiền nợ khách hàng khi thêm hóa đơn
CREATE TRIGGER UPDATE_SOTIENNO_AFTER_HOADON_INSERT
AFTER INSERT ON api_HoaDon
FOR EACH ROW
BEGIN
    UPDATE api_KhachHang
    SET SoTienNo = SoTienNo + NEW.ConLai
    WHERE MaKhachHang = NEW.MaKH_id;
END;

-- Trigger tính số tiền nợ khách hàng khi cập nhật hóa đơn
CREATE TRIGGER UPDATE_SOTIENNO_AFTER_HOADON_UPDATE
AFTER UPDATE ON api_HoaDon
FOR EACH ROW
WHEN OLD.ConLai != NEW.ConLai
BEGIN
    UPDATE api_KhachHang
    SET SoTienNo = SoTienNo + (NEW.ConLai - OLD.ConLai)
    WHERE MaKhachHang = NEW.MaKH_id;
END;

-- Trigger tính số tiền nợ khách hàng khi thêm phiếu thu
CREATE TRIGGER UPDATE_SOTIENNO_AFTER_PHIEUTHU_INSERT
AFTER INSERT ON api_PhieuThuTien
FOR EACH ROW
BEGIN
    UPDATE api_KhachHang
    SET SoTienNo = SoTienNo - NEW.SoTienThu
    WHERE MaKhachHang = NEW.MaKH_id;
END;

-- Trigger tính số tiền nợ khách hàng khi cập nhật phiếu thu
CREATE TRIGGER UPDATE_SOTIENNO_AFTER_PHIEUTHU_UPDATE
AFTER UPDATE ON api_PhieuThuTien
FOR EACH ROW
BEGIN
    UPDATE api_KhachHang
    SET SoTienNo = SoTienNo - (NEW.SoTienThu - OLD.SoTienThu)
    WHERE MaKhachHang = NEW.MaKH_id;
END;

-- Trigger kết xuất báo cáo tồn
CREATE TRIGGER CALCULATE_BCTON_INSERT
AFTER INSERT ON api_CT_BCTon
FOR EACH ROW
BEGIN
    -- Cập nhật TonDau và PhatSinh
    UPDATE api_CT_BCTon 
    SET 
        TonDau = COALESCE(
            (SELECT TonCuoi 
             FROM api_CT_BCTon CT
             JOIN api_BaoCaoTon BCT ON CT.MaBCTon_id = BCT.MaBCTon
             WHERE CT.MaSach_id = NEW.MaSach_id
             AND (BCT.Nam * 12 + BCT.Thang) = 
                 ((SELECT Nam * 12 + Thang - 1 
                   FROM api_BaoCaoTon 
                   WHERE MaBCTon = NEW.MaBCTon_id))
             LIMIT 1),
            0
        ),
        PhatSinh = (
            COALESCE((
                SELECT SUM(CTN.SLNhap)
                FROM api_CT_NhapSach CTN
                JOIN api_PhieuNhapSach PNS ON CTN.MaPhieuNhap_id = PNS.MaPhieuNhap
                WHERE CTN.MaSach_id = NEW.MaSach_id
                AND strftime('%Y-%m', PNS.NgayNhap) = (
                    SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                    FROM api_BaoCaoTon
                    WHERE MaBCTon = NEW.MaBCTon_id
                )
            ), 0)
            -
            COALESCE((
                SELECT SUM(CTH.SLBan)
                FROM api_CT_HoaDon CTH
                JOIN api_HoaDon HD ON CTH.MaHD_id = HD.MaHD
                WHERE CTH.MaSach_id = NEW.MaSach_id
                AND strftime('%Y-%m', HD.NgayLap) = (
                    SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                    FROM api_BaoCaoTon
                    WHERE MaBCTon = NEW.MaBCTon_id
                )
            ), 0)
        )
    WHERE id = NEW.id;

    -- Cập nhật TonCuoi = TonDau + PhatSinh
    UPDATE api_CT_BCTon 
    SET TonCuoi = TonDau + PhatSinh
    WHERE id = NEW.id;
END;

-- Trigger kết xuất báo cáo tồn khi cập nhật
CREATE TRIGGER CALCULATE_BCTON_UPDATE
AFTER UPDATE ON api_CT_BCTon
FOR EACH ROW
BEGIN
    -- TonDau should stay as is on updates (it's based on previous report)
    
    -- Calculate PhatSinh (imports - sales in current month)
    UPDATE api_CT_BCTon 
    SET PhatSinh = (
        SELECT COALESCE(
            (SELECT COALESCE(SUM(CTN.SLNhap), 0)
            FROM api_CT_NhapSach CTN
            JOIN api_PhieuNhapSach PNS ON CTN.MaPhieuNhap_id = PNS.MaPhieuNhap
            WHERE CTN.MaSach_id = NEW.MaSach_id
            AND strftime('%Y-%m', PNS.NgayNhap) = (
                SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                FROM api_BaoCaoTon
                WHERE MaBCTon = NEW.MaBCTon_id
            )), 0
        ) - COALESCE(
            (SELECT COALESCE(SUM(CTH.SLBan), 0)
            FROM api_CT_HoaDon CTH
            JOIN api_HoaDon HD ON CTH.MaHD_id = HD.MaHD
            WHERE CTH.MaSach_id = NEW.MaSach_id
            AND strftime('%Y-%m', HD.NgayLap) = (
                SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                FROM api_BaoCaoTon
                WHERE MaBCTon = NEW.MaBCTon_id
            )), 0
        )
    )
    WHERE id = NEW.id;

    -- Calculate TonCuoi (TonDau + PhatSinh)
    UPDATE api_CT_BCTon 
    SET TonCuoi = TonDau + PhatSinh
    WHERE id = NEW.id;
END;

-- Trigger kết xuất báo cáo công nợ
CREATE TRIGGER CALCULATE_BCCONGNO_INSERT
AFTER INSERT ON api_CT_BCCongNo
FOR EACH ROW
BEGIN
    -- Calculate NoDau based on previous month's report or current debt
    UPDATE api_CT_BCCongNo 
    SET NoDau = COALESCE(
        (SELECT NoCuoi 
         FROM api_CT_BCCongNo 
         JOIN api_BaoCaoCongNo ON api_CT_BCCongNo.MaBCCN_id = api_BaoCaoCongNo.MaBCCN
         WHERE api_CT_BCCongNo.MaKH_id = NEW.MaKH_id
         AND (api_BaoCaoCongNo.Nam * 12 + api_BaoCaoCongNo.Thang) = 
             (SELECT (Nam * 12 + Thang - 1) 
              FROM api_BaoCaoCongNo 
              WHERE MaBCCN = NEW.MaBCCN_id)
         LIMIT 1),
        0
    ),
    -- Calculate PhatSinh: new debts - payments in current month
    PhatSinh = (
        SELECT COALESCE(
            (SELECT COALESCE(SUM(HD.ConLai), 0)
            FROM api_HoaDon HD
            WHERE HD.MaKH_id = NEW.MaKH_id
            AND strftime('%Y-%m', HD.NgayLap) = (
                SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                FROM api_BaoCaoCongNo
                WHERE MaBCCN = NEW.MaBCCN_id
            )), 0
        ) - COALESCE(
            (SELECT COALESCE(SUM(PT.SoTienThu), 0)
            FROM api_PhieuThuTien PT
            WHERE PT.MaKH_id = NEW.MaKH_id
            AND strftime('%Y-%m', PT.NgayThu) = (
                SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                FROM api_BaoCaoCongNo
                WHERE MaBCCN = NEW.MaBCCN_id
            )), 0
        )
    )
    WHERE id = NEW.id;

    -- Calculate NoCuoi (NoDau + PhatSinh)
    UPDATE api_CT_BCCongNo 
    SET NoCuoi = NoDau + PhatSinh
    WHERE id = NEW.id;
END;

-- Trigger kết xuất báo cáo công nợ khi cập nhật
CREATE TRIGGER CALCULATE_BCCONGNO_UPDATE
AFTER UPDATE ON api_CT_BCCongNo
FOR EACH ROW
BEGIN
    -- NoDau should stay as is on updates (it's based on previous report)
    
    -- Calculate PhatSinh: new debts - payments in current month
    UPDATE api_CT_BCCongNo 
    SET PhatSinh = (
        SELECT COALESCE(
            (SELECT COALESCE(SUM(HD.ConLai), 0)
            FROM api_HoaDon HD
            WHERE HD.MaKH_id = NEW.MaKH_id
            AND strftime('%Y-%m', HD.NgayLap) = (
                SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                FROM api_BaoCaoCongNo
                WHERE MaBCCN = NEW.MaBCCN_id
            )), 0
        ) - COALESCE(
            (SELECT COALESCE(SUM(PT.SoTienThu), 0)
            FROM api_PhieuThuTien PT
            WHERE PT.MaKH_id = NEW.MaKH_id
            AND strftime('%Y-%m', PT.NgayThu) = (
                SELECT strftime('%Y-%m', date(Nam || '-' || printf('%02d', Thang) || '-01'))
                FROM api_BaoCaoCongNo
                WHERE MaBCCN = NEW.MaBCCN_id
            )), 0
        )
    )
    WHERE id = NEW.id;

    -- Calculate NoCuoi (NoDau + PhatSinh)
    UPDATE api_CT_BCCongNo 
    SET NoCuoi = NoDau + PhatSinh
    WHERE id = NEW.id;
END;