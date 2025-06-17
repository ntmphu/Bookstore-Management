# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import PhieuThuTienSerializer

phieuthutien_data = phieuthu_data_bosung = [
  { "NguoiThu_input": "NV002", "NgayThu": "15/04/2025", "MaKH_input": "KH004", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "20/05/2025", "MaKH_input": "KH004", "SoTienThu": 385000 },
  { "NguoiThu_input": "NV002", "NgayThu": "10/04/2025", "MaKH_input": "KH009", "SoTienThu": 500000 },
  { "NguoiThu_input": "NV002", "NgayThu": "11/05/2025", "MaKH_input": "KH009", "SoTienThu": 350000 },
  { "NguoiThu_input": "NV002", "NgayThu": "05/05/2025", "MaKH_input": "KH018", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "15/06/2025", "MaKH_input": "KH018", "SoTienThu": 250000 },
  { "NguoiThu_input": "NV002", "NgayThu": "22/04/2025", "MaKH_input": "KH019", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "18/04/2025", "MaKH_input": "KH028", "SoTienThu": 500000 },
  { "NguoiThu_input": "NV002", "NgayThu": "19/05/2025", "MaKH_input": "KH028", "SoTienThu": 500000 },
  { "NguoiThu_input": "NV002", "NgayThu": "21/06/2025", "MaKH_input": "KH028", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "25/04/2025", "MaKH_input": "KH032", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "30/05/2025", "MaKH_input": "KH034", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "14/04/2025", "MaKH_input": "KH039", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "16/05/2025", "MaKH_input": "KH039", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "20/06/2025", "MaKH_input": "KH040", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "28/04/2025", "MaKH_input": "KH042", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "30/05/2025", "MaKH_input": "KH042", "SoTienThu": 250000 },
  { "NguoiThu_input": "NV002", "NgayThu": "10/04/2025", "MaKH_input": "KH049", "SoTienThu": 500000 },
  { "NguoiThu_input": "NV002", "NgayThu": "12/05/2025", "MaKH_input": "KH049", "SoTienThu": 500000 },
  { "NguoiThu_input": "NV002", "NgayThu": "14/06/2025", "MaKH_input": "KH049", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "17/04/2025", "MaKH_input": "KH051", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "19/05/2025", "MaKH_input": "KH052", "SoTienThu": 250000 },
  { "NguoiThu_input": "NV002", "NgayThu": "21/06/2025", "MaKH_input": "KH054", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "23/04/2025", "MaKH_input": "KH057", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "25/05/2025", "MaKH_input": "KH058", "SoTienThu": 350000 },
  { "NguoiThu_input": "NV002", "NgayThu": "27/06/2025", "MaKH_input": "KH059", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "01/05/2025", "MaKH_input": "KH061", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "03/06/2025", "MaKH_input": "KH062", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "02/04/2025", "MaKH_input": "KH063", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "04/05/2025", "MaKH_input": "KH063", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "06/06/2025", "MaKH_input": "KH064", "SoTienThu": 350000 },
  { "NguoiThu_input": "NV002", "NgayThu": "08/04/2025", "MaKH_input": "KH067", "SoTienThu": 250000 },
  { "NguoiThu_input": "NV002", "NgayThu": "10/05/2025", "MaKH_input": "KH068", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "12/06/2025", "MaKH_input": "KH068", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "14/04/2025", "MaKH_input": "KH070", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "16/05/2025", "MaKH_input": "KH072", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "18/06/2025", "MaKH_input": "KH072", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "20/04/2025", "MaKH_input": "KH073", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "22/05/2025", "MaKH_input": "KH074", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "01/04/2025", "MaKH_input": "KH002", "SoTienThu": 455000 },
  { "NguoiThu_input": "NV002", "NgayThu": "03/05/2025", "MaKH_input": "KH007", "SoTienThu": 122700 },
  { "NguoiThu_input": "NV002", "NgayThu": "05/06/2025", "MaKH_input": "KH010", "SoTienThu": 664000 },
  { "NguoiThu_input": "NV002", "NgayThu": "07/04/2025", "MaKH_input": "KH012", "SoTienThu": 481700 },
  { "NguoiThu_input": "NV002", "NgayThu": "09/05/2025", "MaKH_input": "KH013", "SoTienThu": 345000 },
  { "NguoiThu_input": "NV002", "NgayThu": "11/06/2025", "MaKH_input": "KH015", "SoTienThu": 130000 },
  { "NguoiThu_input": "NV002", "NgayThu": "13/04/2025", "MaKH_input": "KH022", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "15/05/2025", "MaKH_input": "KH023", "SoTienThu": 174000 },
  { "NguoiThu_input": "NV002", "NgayThu": "17/06/2025", "MaKH_input": "KH024", "SoTienThu": 150000 },
  { "NguoiThu_input": "NV002", "NgayThu": "19/04/2025", "MaKH_input": "KH025", "SoTienThu": 280000 },
  { "NguoiThu_input": "NV002", "NgayThu": "21/05/2025", "MaKH_input": "KH033", "SoTienThu": 20000 },
  { "NguoiThu_input": "NV002", "NgayThu": "23/06/2025", "MaKH_input": "KH036", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "25/04/2025", "MaKH_input": "KH044", "SoTienThu": 281900 },
  { "NguoiThu_input": "NV002", "NgayThu": "27/05/2025", "MaKH_input": "KH046", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "29/06/2025", "MaKH_input": "KH047", "SoTienThu": 200000 },
  { "NguoiThu_input": "NV002", "NgayThu": "01/06/2025", "MaKH_input": "KH065", "SoTienThu": 500000 },
  { "NguoiThu_input": "NV002", "NgayThu": "03/04/2025", "MaKH_input": "KH066", "SoTienThu": 400000 },
  { "NguoiThu_input": "NV002", "NgayThu": "05/05/2025", "MaKH_input": "KH069", "SoTienThu": 300000 },
  { "NguoiThu_input": "NV002", "NgayThu": "07/06/2025", "MaKH_input": "KH071", "SoTienThu": 1500000 },
  { "NguoiThu_input": "NV002", "NgayThu": "09/04/2025", "MaKH_input": "KH075", "SoTienThu": 350000 }
]

success, failed = 0, 0

for item in phieuthutien_data:
    serializer = PhieuThuTienSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")