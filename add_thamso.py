# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import ThamSoSerializer

thamso_data = [
  {
      "SLNhapTT": 150,
      "TonTD": 300,
      "NoTD": 1000000,
      "TonTT": 20,
      "TiLe": 1.05,
      "SDQD4": 1
  }
]

success, failed = 0, 0

for item in thamso_data:
    serializer = ThamSoSerializer(data=item)
    if serializer.is_valid():
        serializer.save()
        print(f"✅ Thêm thành công: {item}")
        success += 1
    else:
        print(f"❌ Thêm thất bại: {item}")
        print(serializer.errors)
        failed += 1

print(f"\nTổng cộng: {success} thành công, {failed} thất bại")