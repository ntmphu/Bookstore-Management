# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import PhieuThuTienSerializer

phieuthutien_data = [
  { "NguoiThu_input": "NV001", "NgayThu": "12/03/2025", "MaKH_input": "KH001", "SoTienThu": 10000 },
  { "NguoiThu_input": "NV001", "NgayThu": "15/03/2025", "MaKH_input": "KH001", "SoTienThu": 8000 },

  { "NguoiThu_input": "NV001", "NgayThu": "11/03/2025", "MaKH_input": "KH002", "SoTienThu": 9000 },
  { "NguoiThu_input": "NV001", "NgayThu": "18/03/2025", "MaKH_input": "KH002", "SoTienThu": 6000 },
  { "NguoiThu_input": "NV001", "NgayThu": "25/03/2025", "MaKH_input": "KH002", "SoTienThu": 7000 },

  { "NguoiThu_input": "NV001", "NgayThu": "10/03/2025", "MaKH_input": "KH003", "SoTienThu": 9500 },
  { "NguoiThu_input": "NV001", "NgayThu": "22/03/2025", "MaKH_input": "KH003", "SoTienThu": 10500 },

  { "NguoiThu_input": "NV001", "NgayThu": "14/03/2025", "MaKH_input": "KH004", "SoTienThu": 5000 },

  { "NguoiThu_input": "NV001", "NgayThu": "13/03/2025", "MaKH_input": "KH005", "SoTienThu": 12000 },
  { "NguoiThu_input": "NV001", "NgayThu": "19/03/2025", "MaKH_input": "KH005", "SoTienThu": 6000 },

  { "NguoiThu_input": "NV001", "NgayThu": "17/03/2025", "MaKH_input": "KH006", "SoTienThu": 7000 },

  { "NguoiThu_input": "NV001", "NgayThu": "16/03/2025", "MaKH_input": "KH007", "SoTienThu": 11000 },
  { "NguoiThu_input": "NV001", "NgayThu": "24/03/2025", "MaKH_input": "KH007", "SoTienThu": 9000 },

  { "NguoiThu_input": "NV001", "NgayThu": "12/03/2025", "MaKH_input": "KH008", "SoTienThu": 7500 },

  { "NguoiThu_input": "NV001", "NgayThu": "13/03/2025", "MaKH_input": "KH009", "SoTienThu": 8000 },
  { "NguoiThu_input": "NV001", "NgayThu": "20/03/2025", "MaKH_input": "KH009", "SoTienThu": 7000 },

  { "NguoiThu_input": "NV001", "NgayThu": "14/03/2025", "MaKH_input": "KH010", "SoTienThu": 6500 },
  { "NguoiThu_input": "NV001", "NgayThu": "21/03/2025", "MaKH_input": "KH010", "SoTienThu": 8500 },

  { "NguoiThu_input": "NV001", "NgayThu": "23/03/2025", "MaKH_input": "KH004", "SoTienThu": 4000 },
  { "NguoiThu_input": "NV001", "NgayThu": "01/04/2025", "MaKH_input": "KH001", "SoTienThu": 75000 },
  { "NguoiThu_input": "NV001", "NgayThu": "05/04/2025", "MaKH_input": "KH001", "SoTienThu": 132000 },
  { "NguoiThu_input": "NV001", "NgayThu": "09/04/2025", "MaKH_input": "KH001", "SoTienThu": 98000 },
  { "NguoiThu_input": "NV001", "NgayThu": "12/04/2025", "MaKH_input": "KH001", "SoTienThu": 150000 },

  { "NguoiThu_input": "NV001", "NgayThu": "02/04/2025", "MaKH_input": "KH002", "SoTienThu": 64000 },
  { "NguoiThu_input": "NV001", "NgayThu": "07/04/2025", "MaKH_input": "KH002", "SoTienThu": 113000 },
  { "NguoiThu_input": "NV001", "NgayThu": "13/04/2025", "MaKH_input": "KH002", "SoTienThu": 127000 },
  { "NguoiThu_input": "NV001", "NgayThu": "20/04/2025", "MaKH_input": "KH002", "SoTienThu": 56000 },

  { "NguoiThu_input": "NV001", "NgayThu": "03/04/2025", "MaKH_input": "KH003", "SoTienThu": 92000 },
  { "NguoiThu_input": "NV001", "NgayThu": "10/04/2025", "MaKH_input": "KH003", "SoTienThu": 145000 },
  { "NguoiThu_input": "NV001", "NgayThu": "15/04/2025", "MaKH_input": "KH003", "SoTienThu": 117000 },
  { "NguoiThu_input": "NV001", "NgayThu": "21/04/2025", "MaKH_input": "KH003", "SoTienThu": 168000 },

  { "NguoiThu_input": "NV001", "NgayThu": "04/04/2025", "MaKH_input": "KH004", "SoTienThu": 71000 },
  { "NguoiThu_input": "NV001", "NgayThu": "08/04/2025", "MaKH_input": "KH004", "SoTienThu": 88000 },
  { "NguoiThu_input": "NV001", "NgayThu": "14/04/2025", "MaKH_input": "KH004", "SoTienThu": 105000 },
  { "NguoiThu_input": "NV001", "NgayThu": "18/04/2025", "MaKH_input": "KH004", "SoTienThu": 192000 },

  { "NguoiThu_input": "NV001", "NgayThu": "01/04/2025", "MaKH_input": "KH005", "SoTienThu": 67000 },
  { "NguoiThu_input": "NV001", "NgayThu": "06/04/2025", "MaKH_input": "KH005", "SoTienThu": 123000 },
  { "NguoiThu_input": "NV001", "NgayThu": "11/04/2025", "MaKH_input": "KH005", "SoTienThu": 114000 },
  { "NguoiThu_input": "NV001", "NgayThu": "17/04/2025", "MaKH_input": "KH005", "SoTienThu": 178000 },

  { "NguoiThu_input": "NV001", "NgayThu": "03/04/2025", "MaKH_input": "KH006", "SoTienThu": 84000 },
  { "NguoiThu_input": "NV001", "NgayThu": "07/04/2025", "MaKH_input": "KH006", "SoTienThu": 157000 },
  { "NguoiThu_input": "NV001", "NgayThu": "12/04/2025", "MaKH_input": "KH006", "SoTienThu": 119000 },
  { "NguoiThu_input": "NV001", "NgayThu": "19/04/2025", "MaKH_input": "KH006", "SoTienThu": 91000 },

  { "NguoiThu_input": "NV001", "NgayThu": "02/04/2025", "MaKH_input": "KH007", "SoTienThu": 61000 },
  { "NguoiThu_input": "NV001", "NgayThu": "09/04/2025", "MaKH_input": "KH007", "SoTienThu": 93000 },
  { "NguoiThu_input": "NV001", "NgayThu": "16/04/2025", "MaKH_input": "KH007", "SoTienThu": 162000 },
  { "NguoiThu_input": "NV001", "NgayThu": "22/04/2025", "MaKH_input": "KH007", "SoTienThu": 104000 },

  { "NguoiThu_input": "NV001", "NgayThu": "05/04/2025", "MaKH_input": "KH008", "SoTienThu": 74000 },
  { "NguoiThu_input": "NV001", "NgayThu": "10/04/2025", "MaKH_input": "KH008", "SoTienThu": 136000 },
  { "NguoiThu_input": "NV001", "NgayThu": "15/04/2025", "MaKH_input": "KH008", "SoTienThu": 158000 },
  { "NguoiThu_input": "NV001", "NgayThu": "23/04/2025", "MaKH_input": "KH008", "SoTienThu": 98000 },

  { "NguoiThu_input": "NV001", "NgayThu": "06/04/2025", "MaKH_input": "KH009", "SoTienThu": 111000 },
  { "NguoiThu_input": "NV001", "NgayThu": "11/04/2025", "MaKH_input": "KH009", "SoTienThu": 137000 },
  { "NguoiThu_input": "NV001", "NgayThu": "17/04/2025", "MaKH_input": "KH009", "SoTienThu": 66000 },
  { "NguoiThu_input": "NV001", "NgayThu": "25/04/2025", "MaKH_input": "KH009", "SoTienThu": 195000 },

  { "NguoiThu_input": "NV001", "NgayThu": "08/04/2025", "MaKH_input": "KH010", "SoTienThu": 87000 },
  { "NguoiThu_input": "NV001", "NgayThu": "14/04/2025", "MaKH_input": "KH010", "SoTienThu": 121000 },
  { "NguoiThu_input": "NV001", "NgayThu": "20/04/2025", "MaKH_input": "KH010", "SoTienThu": 143000 },
  { "NguoiThu_input": "NV001", "NgayThu": "26/04/2025", "MaKH_input": "KH010", "SoTienThu": 164000 }
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