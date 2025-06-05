# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import PhieuNhapSachSerializer

# phieunhapsach_data = [
#   { "NguoiNhap_input": "NV001", "NgayNhap": "05/01/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "12/02/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "21/03/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "06/04/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "18/05/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "25/06/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "02/07/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "11/08/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "17/09/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "05/10/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "14/11/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "30/12/2024" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "07/01/2025" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "22/02/2025" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "13/03/2025" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "09/04/2025" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "20/05/2025" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "02/06/2025" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "18/06/2025" },
#   { "NguoiNhap_input": "NV001", "NgayNhap": "29/06/2025" }
# ]

phieunhapsach_data = [
    { "NguoiNhap_input": "NV001", "NgayNhap": "13/03/2024" }
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