# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import CTHoaDonSerializer

# ct_hoa_don_data = [
#   {"MaHD_input": "HD001", "MaSach_input": "S001", "SLBan": 2},
#   {"MaHD_input": "HD001", "MaSach_input": "S005", "SLBan": 3},
#   {"MaHD_input": "HD001", "MaSach_input": "S009", "SLBan": 1},
#   {"MaHD_input": "HD001", "MaSach_input": "S014", "SLBan": 4},

#   {"MaHD_input": "HD002", "MaSach_input": "S003", "SLBan": 2},
#   {"MaHD_input": "HD002", "MaSach_input": "S008", "SLBan": 1},
#   {"MaHD_input": "HD002", "MaSach_input": "S012", "SLBan": 3},
#   {"MaHD_input": "HD002", "MaSach_input": "S017", "SLBan": 2},

#   {"MaHD_input": "HD003", "MaSach_input": "S004", "SLBan": 4},
#   {"MaHD_input": "HD003", "MaSach_input": "S010", "SLBan": 1},
#   {"MaHD_input": "HD003", "MaSach_input": "S015", "SLBan": 3},
#   {"MaHD_input": "HD003", "MaSach_input": "S019", "SLBan": 2},

#   {"MaHD_input": "HD004", "MaSach_input": "S002", "SLBan": 2},
#   {"MaHD_input": "HD004", "MaSach_input": "S006", "SLBan": 1},
#   {"MaHD_input": "HD004", "MaSach_input": "S011", "SLBan": 5},
#   {"MaHD_input": "HD004", "MaSach_input": "S018", "SLBan": 2},

#   {"MaHD_input": "HD005", "MaSach_input": "S001", "SLBan": 3},
#   {"MaHD_input": "HD005", "MaSach_input": "S007", "SLBan": 1},
#   {"MaHD_input": "HD005", "MaSach_input": "S013", "SLBan": 2},
#   {"MaHD_input": "HD005", "MaSach_input": "S020", "SLBan": 4},

#   {"MaHD_input": "HD006", "MaSach_input": "S003", "SLBan": 2},
#   {"MaHD_input": "HD006", "MaSach_input": "S009", "SLBan": 3},
#   {"MaHD_input": "HD006", "MaSach_input": "S014", "SLBan": 1},
#   {"MaHD_input": "HD006", "MaSach_input": "S016", "SLBan": 5},

#   {"MaHD_input": "HD007", "MaSach_input": "S005", "SLBan": 2},
#   {"MaHD_input": "HD007", "MaSach_input": "S008", "SLBan": 3},
#   {"MaHD_input": "HD007", "MaSach_input": "S012", "SLBan": 2},
#   {"MaHD_input": "HD007", "MaSach_input": "S017", "SLBan": 1},

#   {"MaHD_input": "HD008", "MaSach_input": "S004", "SLBan": 4},
#   {"MaHD_input": "HD008", "MaSach_input": "S006", "SLBan": 1},
#   {"MaHD_input": "HD008", "MaSach_input": "S015", "SLBan": 3},
#   {"MaHD_input": "HD008", "MaSach_input": "S018", "SLBan": 2},

#   {"MaHD_input": "HD009", "MaSach_input": "S002", "SLBan": 3},
#   {"MaHD_input": "HD009", "MaSach_input": "S007", "SLBan": 2},
#   {"MaHD_input": "HD009", "MaSach_input": "S010", "SLBan": 1},
#   {"MaHD_input": "HD009", "MaSach_input": "S013", "SLBan": 5},

#   {"MaHD_input": "HD010", "MaSach_input": "S001", "SLBan": 2},
#   {"MaHD_input": "HD010", "MaSach_input": "S011", "SLBan": 3},
#   {"MaHD_input": "HD010", "MaSach_input": "S016", "SLBan": 1},
#   {"MaHD_input": "HD010", "MaSach_input": "S019", "SLBan": 4},

#   {"MaHD_input": "HD011", "MaSach_input": "S002", "SLBan": 3},
#   {"MaHD_input": "HD011", "MaSach_input": "S006", "SLBan": 2},
#   {"MaHD_input": "HD011", "MaSach_input": "S013", "SLBan": 1},
#   {"MaHD_input": "HD011", "MaSach_input": "S018", "SLBan": 4},

#   {"MaHD_input": "HD012", "MaSach_input": "S003", "SLBan": 2},
#   {"MaHD_input": "HD012", "MaSach_input": "S007", "SLBan": 5},
#   {"MaHD_input": "HD012", "MaSach_input": "S011", "SLBan": 1},
#   {"MaHD_input": "HD012", "MaSach_input": "S016", "SLBan": 2},

#   {"MaHD_input": "HD013", "MaSach_input": "S001", "SLBan": 4},
#   {"MaHD_input": "HD013", "MaSach_input": "S009", "SLBan": 3},
#   {"MaHD_input": "HD013", "MaSach_input": "S014", "SLBan": 2},
#   {"MaHD_input": "HD013", "MaSach_input": "S020", "SLBan": 1},

#   {"MaHD_input": "HD014", "MaSach_input": "S004", "SLBan": 3},
#   {"MaHD_input": "HD014", "MaSach_input": "S005", "SLBan": 2},
#   {"MaHD_input": "HD014", "MaSach_input": "S012", "SLBan": 1},
#   {"MaHD_input": "HD014", "MaSach_input": "S017", "SLBan": 4},

#   {"MaHD_input": "HD015", "MaSach_input": "S006", "SLBan": 1},
#   {"MaHD_input": "HD015", "MaSach_input": "S010", "SLBan": 3},
#   {"MaHD_input": "HD015", "MaSach_input": "S015", "SLBan": 2},
#   {"MaHD_input": "HD015", "MaSach_input": "S019", "SLBan": 5},

#   {"MaHD_input": "HD016", "MaSach_input": "S002", "SLBan": 4},
#   {"MaHD_input": "HD016", "MaSach_input": "S008", "SLBan": 3},
#   {"MaHD_input": "HD016", "MaSach_input": "S013", "SLBan": 1},
#   {"MaHD_input": "HD016", "MaSach_input": "S018", "SLBan": 2},

#   {"MaHD_input": "HD017", "MaSach_input": "S003", "SLBan": 3},
#   {"MaHD_input": "HD017", "MaSach_input": "S007", "SLBan": 2},
#   {"MaHD_input": "HD017", "MaSach_input": "S011", "SLBan": 4},
#   {"MaHD_input": "HD017", "MaSach_input": "S016", "SLBan": 1},

#   {"MaHD_input": "HD018", "MaSach_input": "S001", "SLBan": 1},
#   {"MaHD_input": "HD018", "MaSach_input": "S009", "SLBan": 2},
#   {"MaHD_input": "HD018", "MaSach_input": "S014", "SLBan": 5},
#   {"MaHD_input": "HD018", "MaSach_input": "S020", "SLBan": 3},

#   {"MaHD_input": "HD019", "MaSach_input": "S004", "SLBan": 3},
#   {"MaHD_input": "HD019", "MaSach_input": "S005", "SLBan": 1},
#   {"MaHD_input": "HD019", "MaSach_input": "S012", "SLBan": 2},
#   {"MaHD_input": "HD019", "MaSach_input": "S017", "SLBan": 4},

#   {"MaHD_input": "HD020", "MaSach_input": "S006", "SLBan": 2},
#   {"MaHD_input": "HD020", "MaSach_input": "S010", "SLBan": 4},
#   {"MaHD_input": "HD020", "MaSach_input": "S015", "SLBan": 3},
#   {"MaHD_input": "HD020", "MaSach_input": "S019", "SLBan": 1}
# ]

ct_hoa_don_data = [
  # { "MaHD_input": "HD001", "MaSach_input": "S001", "SLBan": 2 },
  # { "MaHD_input": "HD001", "MaSach_input": "S004", "SLBan": 1 },
  # { "MaHD_input": "HD002", "MaSach_input": "S002", "SLBan": 3 },
  # { "MaHD_input": "HD002", "MaSach_input": "S005", "SLBan": 2 },
  # { "MaHD_input": "HD003", "MaSach_input": "S003", "SLBan": 4 },
  # { "MaHD_input": "HD003", "MaSach_input": "S006", "SLBan": 1 },
  # { "MaHD_input": "HD004", "MaSach_input": "S005", "SLBan": 2 },
  # { "MaHD_input": "HD004", "MaSach_input": "S007", "SLBan": 3 },
  # { "MaHD_input": "HD005", "MaSach_input": "S008", "SLBan": 2 },
  # { "MaHD_input": "HD005", "MaSach_input": "S001", "SLBan": 1 },
  # { "MaHD_input": "HD006", "MaSach_input": "S015", "SLBan": 5 },
  # { "MaHD_input": "HD006", "MaSach_input": "S010", "SLBan": 2 },
  # { "MaHD_input": "HD007", "MaSach_input": "S013", "SLBan": 2 },
  # { "MaHD_input": "HD007", "MaSach_input": "S009", "SLBan": 1 },
  # { "MaHD_input": "HD008", "MaSach_input": "S014", "SLBan": 3 },
  # { "MaHD_input": "HD008", "MaSach_input": "S012", "SLBan": 1 },
  # { "MaHD_input": "HD009", "MaSach_input": "S015", "SLBan": 4 },
  # { "MaHD_input": "HD009", "MaSach_input": "S014", "SLBan": 2 },
  # { "MaHD_input": "HD010", "MaSach_input": "S007", "SLBan": 2 },
  # { "MaHD_input": "HD010", "MaSach_input": "S004", "SLBan": 3 },
  # { "MaHD_input": "HD011", "MaSach_input": "S011", "SLBan": 1 },
  # { "MaHD_input": "HD011", "MaSach_input": "S014", "SLBan": 2 },
  # { "MaHD_input": "HD012", "MaSach_input": "S002", "SLBan": 4 },
  # { "MaHD_input": "HD012", "MaSach_input": "S014", "SLBan": 2 }
]


success, failed = 0, 0

for item in ct_hoa_don_data:
    serializer = CTHoaDonSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")