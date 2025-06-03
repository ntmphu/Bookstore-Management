# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import HoaDonSerializer

# hoa_dons_data = [
# 	{ "NgayLap": "10/01/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH001" },
# 	{ "NgayLap": "22/01/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH002" },
# 	{ "NgayLap": "05/02/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH003" },
# 	{ "NgayLap": "15/02/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH004" },
# 	{ "NgayLap": "03/03/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH005" },
# 	{ "NgayLap": "17/03/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH006" },
# 	{ "NgayLap": "08/04/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH007" },
# 	{ "NgayLap": "20/04/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH008" },
# 	{ "NgayLap": "01/05/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH009" },
# 	{ "NgayLap": "12/05/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH010" },
# 	{ "NgayLap": "24/05/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH011" },
# 	{ "NgayLap": "06/06/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH012" },
# 	{ "NgayLap": "14/06/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH013" },
# 	{ "NgayLap": "26/06/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH014" },
# 	{ "NgayLap": "09/01/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH015" },
# 	{ "NgayLap": "18/02/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH016" },
# 	{ "NgayLap": "27/03/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH017" },
# 	{ "NgayLap": "07/04/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH018" },
# 	{ "NgayLap": "19/05/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH019" },
# 	{ "NgayLap": "30/06/2025", "NguoiLapHD_input": "NV001", "MaKH_input": "KH020" }
# ]

hoa_dons_data = [
  { "NgayLap": "05/01/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH001" },
  { "NgayLap": "14/02/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH002" },
  { "NgayLap": "23/03/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH003" },
  { "NgayLap": "08/04/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH004" },
  { "NgayLap": "19/05/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH005" },
  { "NgayLap": "03/06/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH006" },
  { "NgayLap": "12/07/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH007" },
  { "NgayLap": "27/08/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH008" },
  { "NgayLap": "11/09/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH009" },
  { "NgayLap": "20/10/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH010" },
  { "NgayLap": "04/11/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH001" },
  { "NgayLap": "15/12/2024", "NguoiLapHD_input": "NV001", "MaKH_input": "KH002" }
]


success, failed = 0, 0

for item in hoa_dons_data:
    serializer = HoaDonSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")