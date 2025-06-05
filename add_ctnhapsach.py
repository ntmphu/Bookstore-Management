# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import CTNhapSachSerializer

# ctnhapsach_data = [
# #   { "MaPhieuNhap_input": "PN001", "MaSach_input": "S001", "SLNhap": 150, "GiaNhap": 45000 },
# #   { "MaPhieuNhap_input": "PN001", "MaSach_input": "S004", "SLNhap": 150, "GiaNhap": 50000 },

# #   { "MaPhieuNhap_input": "PN002", "MaSach_input": "S002", "SLNhap": 150, "GiaNhap": 60000 },
# #   { "MaPhieuNhap_input": "PN002", "MaSach_input": "S006", "SLNhap": 180, "GiaNhap": 47000 },

# #   { "MaPhieuNhap_input": "PN003", "MaSach_input": "S009", "SLNhap": 150, "GiaNhap": 52000 },
# #   { "MaPhieuNhap_input": "PN003", "MaSach_input": "S0010", "SLNhap": 150, "GiaNhap": 48000 },

# #   { "MaPhieuNhap_input": "PN004", "MaSach_input": "S001", "SLNhap": 160, "GiaNhap": 55000 },
# #   { "MaPhieuNhap_input": "PN004", "MaSach_input": "S002", "SLNhap": 200, "GiaNhap": 49500 },

# #   { "MaPhieuNhap_input": "PN005", "MaSach_input": "S009", "SLNhap": 220, "GiaNhap": 53000 },
# #   { "MaPhieuNhap_input": "PN005", "MaSach_input": "S011", "SLNhap": 150, "GiaNhap": 46000 },

# #   { "MaPhieuNhap_input": "PN006", "MaSach_input": "S012", "SLNhap": 170, "GiaNhap": 51000 },
# #   { "MaPhieuNhap_input": "PN006", "MaSach_input": "S003", "SLNhap": 190, "GiaNhap": 49000 },

# #   { "MaPhieuNhap_input": "PN007", "MaSach_input": "S005", "SLNhap": 110, "GiaNhap": 47000 },
# #   { "MaPhieuNhap_input": "PN007", "MaSach_input": "S007", "SLNhap": 160, "GiaNhap": 54000 },

# #   { "MaPhieuNhap_input": "PN008", "MaSach_input": "S005", "SLNhap": 200, "GiaNhap": 50000 },
# #   { "MaPhieuNhap_input": "PN008", "MaSach_input": "S004", "SLNhap": 150, "GiaNhap": 45500 },

# #   { "MaPhieuNhap_input": "PN009", "MaSach_input": "S006", "SLNhap": 210, "GiaNhap": 53000 },
# #   { "MaPhieuNhap_input": "PN009", "MaSach_input": "S008", "SLNhap": 170, "GiaNhap": 48000 },

# #   { "MaPhieuNhap_input": "PN010", "MaSach_input": "S009", "SLNhap": 150, "GiaNhap": 47000 },
#   { "MaPhieuNhap_input": "PN010", "MaSach_input": "S013", "SLNhap": 150, "GiaNhap": 44000 },

#   { "MaPhieuNhap_input": "PN011", "MaSach_input": "S001", "SLNhap": 250, "GiaNhap": 51000 },
#   { "MaPhieuNhap_input": "PN011", "MaSach_input": "S002", "SLNhap": 180, "GiaNhap": 50000 },

#   { "MaPhieuNhap_input": "PN012", "MaSach_input": "S003", "SLNhap": 150, "GiaNhap": 47000 },
#   { "MaPhieuNhap_input": "PN012", "MaSach_input": "S004", "SLNhap": 150, "GiaNhap": 49000 },

#   { "MaPhieuNhap_input": "PN013", "MaSach_input": "S005", "SLNhap": 150, "GiaNhap": 52000 },
#   { "MaPhieuNhap_input": "PN013", "MaSach_input": "S006", "SLNhap": 150, "GiaNhap": 45000 },

#   { "MaPhieuNhap_input": "PN014", "MaSach_input": "S007", "SLNhap": 190, "GiaNhap": 49500 },
#   { "MaPhieuNhap_input": "PN014", "MaSach_input": "S008", "SLNhap": 200, "GiaNhap": 50000 },

#   { "MaPhieuNhap_input": "PN015", "MaSach_input": "S009", "SLNhap": 150, "GiaNhap": 51000 },
#   { "MaPhieuNhap_input": "PN015", "MaSach_input": "S010", "SLNhap": 170, "GiaNhap": 46000 },

#   { "MaPhieuNhap_input": "PN016", "MaSach_input": "S001", "SLNhap": 230, "GiaNhap": 53000 },
#   { "MaPhieuNhap_input": "PN016", "MaSach_input": "S003", "SLNhap": 200, "GiaNhap": 48000 },

#   { "MaPhieuNhap_input": "PN017", "MaSach_input": "S004", "SLNhap": 220, "GiaNhap": 50000 },
#   { "MaPhieuNhap_input": "PN017", "MaSach_input": "S005", "SLNhap": 160, "GiaNhap": 49000 },

#   { "MaPhieuNhap_input": "PN018", "MaSach_input": "S006", "SLNhap": 180, "GiaNhap": 47000 },
#   { "MaPhieuNhap_input": "PN018", "MaSach_input": "S007", "SLNhap": 210, "GiaNhap": 55000 },

#   { "MaPhieuNhap_input": "PN019", "MaSach_input": "S008", "SLNhap": 190, "GiaNhap": 52000 },
#   { "MaPhieuNhap_input": "PN019", "MaSach_input": "S009", "SLNhap": 150, "GiaNhap": 49500 },

#   { "MaPhieuNhap_input": "PN020", "MaSach_input": "S002", "SLNhap": 150, "GiaNhap": 47000 },
#   { "MaPhieuNhap_input": "PN020", "MaSach_input": "S010", "SLNhap": 150, "GiaNhap": 48000 }
# ]

ctnhapsach_data = [
  { "MaPhieuNhap_input": "PN011", "MaSach_input": "S014", "SLNhap": 150, "GiaNhap": 60000 }
#   { "MaPhieuNhap_input": "PN002", "MaSach_input": "S006", "SLNhap": 180, "GiaNhap": 47000 },    
]

success, failed = 0, 0

for item in ctnhapsach_data:
    serializer = CTNhapSachSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")