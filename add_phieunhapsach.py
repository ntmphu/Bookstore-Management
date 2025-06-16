# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import PhieuNhapSachSerializer

phieunhapsach_data = [
#   // Mã quy ước: PN001
  { "NguoiNhap_input": "NV001", "NgayNhap": "05/10/2023" },
#   // Mã quy ước: PN002
  { "NguoiNhap_input": "NV001", "NgayNhap": "20/10/2023" },
#   // Mã quy ước: PN003
  { "NguoiNhap_input": "NV001", "NgayNhap": "01/11/2023" },
#   // Mã quy ước: PN004
  { "NguoiNhap_input": "NV001", "NgayNhap": "28/11/2023" },
#   // Mã quy ước: PN005
  { "NguoiNhap_input": "NV001", "NgayNhap": "07/12/2023" },
#   // Mã quy ước: PN006
  { "NguoiNhap_input": "NV001", "NgayNhap": "04/01/2024" },
#   // Mã quy ước: PN007
  { "NguoiNhap_input": "NV001", "NgayNhap": "16/01/2024" },
#   // Mã quy ước: PN008
  { "NguoiNhap_input": "NV001", "NgayNhap": "19/02/2024" },
#   // Mã quy ước: PN009
  { "NguoiNhap_input": "NV001", "NgayNhap": "05/03/2024" },
#   // Mã quy ước: PN010
  { "NguoiNhap_input": "NV001", "NgayNhap": "22/03/2024" },

  { "NguoiNhap_input": "NV001", "NgayNhap": "10/04/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "25/04/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "05/05/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "18/05/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "02/06/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "15/06/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "28/06/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "07/07/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "21/07/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "04/08/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "19/08/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "03/09/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "16/09/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "30/09/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "08/10/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "22/10/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "05/11/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "19/11/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "03/12/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "17/12/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "31/12/2024" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "06/01/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "14/01/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "21/01/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "28/01/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "04/02/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "11/02/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "18/02/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "25/02/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "03/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "04/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "10/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "11/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "17/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "18/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "24/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "25/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "31/03/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "01/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "07/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "08/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "14/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "15/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "21/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "22/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "28/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "29/04/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "05/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "06/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "12/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "13/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "19/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "20/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "26/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "27/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "28/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "29/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "30/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "31/05/2025" },
  { "NguoiNhap_input": "NV001", "NgayNhap": "16/06/2025" }
]

success, failed = 0, 0

for item in phieunhapsach_data:
    serializer = PhieuNhapSachSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")