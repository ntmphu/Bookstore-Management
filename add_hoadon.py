# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()
from api.models import HoaDon
from api.serializers import HoaDonSerializer
from django.db import transaction

# hoa_dons_data = [
#   { "NgayLap": "15/04/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH015" },
#   { "NgayLap": "18/04/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH032" },
#   { "NgayLap": "22/04/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH005" },
#   { "NgayLap": "25/04/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH051" },
#   { "NgayLap": "02/05/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH071" },
#   { "NgayLap": "06/05/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH022" },
#   { "NgayLap": "10/05/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH045" },
#   { "NgayLap": "15/05/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH011" },
#   { "NgayLap": "20/05/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH063" },
#   { "NgayLap": "25/05/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH002" },
#   { "NgayLap": "01/06/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH018" },
#   { "NgayLap": "05/06/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH033" },
#   { "NgayLap": "11/06/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH050" },
#   { "NgayLap": "17/06/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH008" },
#   { "NgayLap": "24/06/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH029" },
#   { "NgayLap": "01/07/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH041" },
#   { "NgayLap": "08/07/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH055" },
#   { "NgayLap": "15/07/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH003" },
#   { "NgayLap": "22/07/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH068" },
#   { "NgayLap": "29/07/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH020" },
#   { "NgayLap": "05/08/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH038" },
#   { "NgayLap": "12/08/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH074" },
#   { "NgayLap": "19/08/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH013" },
#   { "NgayLap": "26/08/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH048" },
#   { "NgayLap": "02/09/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH060" },
#   { "NgayLap": "09/09/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH007" },
#   { "NgayLap": "16/09/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH025" },
#   { "NgayLap": "23/09/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH058" },
#   { "NgayLap": "30/09/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH034" },
#   { "NgayLap": "07/10/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH019" },
#   { "NgayLap": "14/10/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH044" },
#   { "NgayLap": "21/10/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH070" },
#   { "NgayLap": "28/10/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH001" },
#   { "NgayLap": "04/11/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH053" },
#   { "NgayLap": "11/11/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH028" },
#   { "NgayLap": "18/11/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH065" },
#   { "NgayLap": "25/11/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH010" },
#   { "NgayLap": "02/12/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH040" },
#   { "NgayLap": "09/12/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH069" },
#   { "NgayLap": "16/12/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH024" },
#   { "NgayLap": "23/12/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH057" },
#   { "NgayLap": "30/12/2024", "NguoiLapHD_input": "NV002", "MaKH_input": "KH004" },
#   { "NgayLap": "06/01/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH037" },
#   { "NgayLap": "13/01/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH062" },
#   { "NgayLap": "20/01/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH017" },
#   { "NgayLap": "27/01/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH049" },
#   { "NgayLap": "03/02/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH072" },
#   { "NgayLap": "10/02/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH009" },
#   { "NgayLap": "17/02/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH031" },
#   { "NgayLap": "24/02/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH054" },
#   { "NgayLap": "03/03/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH023" },
#   { "NgayLap": "10/03/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH066" },
#   { "NgayLap": "17/03/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH012" },
#   { "NgayLap": "24/03/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH047" },
#   { "NgayLap": "31/03/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH073" },
#   { "NgayLap": "07/04/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH006" },
#   { "NgayLap": "14/04/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH036" },
#   { "NgayLap": "21/04/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH059" },
#   { "NgayLap": "28/04/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH021" },
#   { "NgayLap": "05/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH043" },
#   { "NgayLap": "07/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH064" },
#   { "NgayLap": "09/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH014" },
#   { "NgayLap": "12/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH052" },
#   { "NgayLap": "14/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH027" },
#   { "NgayLap": "16/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH067" },
#   { "NgayLap": "19/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH030" },
#   { "NgayLap": "21/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH046" },
#   { "NgayLap": "23/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH075" },
#   { "NgayLap": "26/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH016" },
#   { "NgayLap": "28/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH039" },
#   { "NgayLap": "30/05/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH056" },
#   { "NgayLap": "02/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH026" },
#   { "NgayLap": "04/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH061" },
#   { "NgayLap": "06/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH035" },
#   { "NgayLap": "09/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH042" },
#   { "NgayLap": "11/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH001" },
#   { "NgayLap": "13/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH029" },
#   { "NgayLap": "16/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH050" },
#   { "NgayLap": "18/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH071" },
#   { "NgayLap": "20/06/2025", "NguoiLapHD_input": "NV002", "MaKH_input": "KH008" }
# ]

# success, failed = 0, 0

# for item in hoa_dons_data:
#     serializer = HoaDonSerializer(data=item)
#     if serializer.is_valid():
#         serializer.save()
#         print(f"✅ Thêm thành công: {item}")
#         success += 1
#     else:
#         print(f"❌ Thêm thất bại: {item}")
#         print(serializer.errors)
#         failed += 1

# print(f"\nTổng cộng: {success} thành công, {failed} thất bại")

sotientra_data = [
  { "SoTienTra": 300000 },
  { "SoTienTra": 1000000 },
  { "SoTienTra": 100000 },
  { "SoTienTra": 550000 },
  { "SoTienTra": 500000 },
  { "SoTienTra": 1182000 },
  { "SoTienTra": 1295400 },
  { "SoTienTra": 300000 },
  { "SoTienTra": 650000 },
  { "SoTienTra": 593700 },
  { "SoTienTra": 600000 },
  { "SoTienTra": 500000 },
  { "SoTienTra": 300000 },
  { "SoTienTra": 75000 },
  { "SoTienTra": 780000 },
  { "SoTienTra": 829400 },
  { "SoTienTra": 1100000 },
  { "SoTienTra": 0 },
  { "SoTienTra": 200000 },
  { "SoTienTra": 958200 },
  { "SoTienTra": 300000 },
  { "SoTienTra": 100000 },
  { "SoTienTra": 100000 },
  { "SoTienTra": 320000 },
  { "SoTienTra": 880000 },
  { "SoTienTra": 622700 },
  { "SoTienTra": 340000 },
  { "SoTienTra": 80000 },
  { "SoTienTra": 759000 },
  { "SoTienTra": 300000 },
  { "SoTienTra": 600000 },
  { "SoTienTra": 400000 },
  { "SoTienTra": 670000 },
  { "SoTienTra": 250000 },
  { "SoTienTra": 15000 },
  { "SoTienTra": 40000 },
  { "SoTienTra": 1000000 },
  { "SoTienTra": 400000 },
  { "SoTienTra": 0 },
  { "SoTienTra": 150000 },
  { "SoTienTra": 1281800 },
  { "SoTienTra": 1000000 },
  { "SoTienTra": 500000 },
  { "SoTienTra": 200000 },
  { "SoTienTra": 1000000 },
  { "SoTienTra": 800000 },
  { "SoTienTra": 90000 },
  { "SoTienTra": 900000 },
  { "SoTienTra": 0 },
  { "SoTienTra": 1300000 },
  { "SoTienTra": 60000 },
  { "SoTienTra": 900000 },
  { "SoTienTra": 230000 },
  { "SoTienTra": 200000 },
  { "SoTienTra": 450000 },
  { "SoTienTra": 1300000 },
  { "SoTienTra": 850000 },
  { "SoTienTra": 1300000 },
  { "SoTienTra": 1150000 },
  { "SoTienTra": 1100000 },
  { "SoTienTra": 950000 },
  { "SoTienTra": 581700 },
  { "SoTienTra": 600000 },
  { "SoTienTra": 500000 },
  { "SoTienTra": 300000 },
  { "SoTienTra": 150000 },
  { "SoTienTra": 400000 },
  { "SoTienTra": 600000 },
  { "SoTienTra": 700000 },
  { "SoTienTra": 900000 },
  { "SoTienTra": 504000 },
  { "SoTienTra": 0 },
  { "SoTienTra": 550000 },
  { "SoTienTra": 800000 },
  { "SoTienTra": 400000 },
  { "SoTienTra": 650000 },
  { "SoTienTra": 700000 },
  { "SoTienTra": 400000 },
  { "SoTienTra": 101700 },
  { "SoTienTra": 900000 }
]

with transaction.atomic():
  success, failed = 0, 0
  for tientra, hd in zip(sotientra_data, HoaDon.objects.all()):
      original_data = HoaDonSerializer(hd).data
      # Ghi đè SoTienTra
      original_data["SoTienTra"] = tientra["SoTienTra"]
      original_data["MaKH_input"] = original_data["MaKH"]
      original_data["NguoiLapHD_input"] = original_data["NguoiLapHD"]
      # Tạo serializer với toàn bộ dữ liệu
      serializer = HoaDonSerializer(hd, data=original_data)
      if serializer.is_valid():
          serializer.save()
          print(f"✅ Thêm thành công: {tientra}")
          success += 1
      else:
          print(f"Invalid data for HoaDon ID {hd.MaHD}: {serializer.errors}")
          failed += 1
      print(f"\nTổng cộng: {success} thành công, {failed} thất bại")