# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import CTNhapSachSerializer

ctnhapsach_data = [
  # // Phiếu PN001 (05/10/2023)
  { "MaPhieuNhap_input": "PN001", "MaSach_input": "S003", "SLNhap": 200, "GiaNhap": 110000 },
  { "MaPhieuNhap_input": "PN001", "MaSach_input": "S015", "SLNhap": 250, "GiaNhap": 75000 },
  
  # // Phiếu PN002 (20/10/2023)
  { "MaPhieuNhap_input": "PN002", "MaSach_input": "S022", "SLNhap": 180, "GiaNhap": 89000 },
  { "MaPhieuNhap_input": "PN002", "MaSach_input": "S008", "SLNhap": 300, "GiaNhap": 55000 },
  
  # // Phiếu PN003 (01/11/2023)
  { "MaPhieuNhap_input": "PN003", "MaSach_input": "S031", "SLNhap": 160, "GiaNhap": 125000 },
  { "MaPhieuNhap_input": "PN003", "MaSach_input": "S045", "SLNhap": 220, "GiaNhap": 68000 },
  { "MaPhieuNhap_input": "PN003", "MaSach_input": "S050", "SLNhap": 190, "GiaNhap": 95000 },

  # // Phiếu PN004 (28/11/2023)
  { "MaPhieuNhap_input": "PN004", "MaSach_input": "S061", "SLNhap": 200, "GiaNhap": 150000 },
  { "MaPhieuNhap_input": "PN004", "MaSach_input": "S073", "SLNhap": 170, "GiaNhap": 72000 },
  
  # // Phiếu PN005 (07/12/2023)
  { "MaPhieuNhap_input": "PN005", "MaSach_input": "S001", "SLNhap": 400, "GiaNhap": 80000 },
  { "MaPhieuNhap_input": "PN005", "MaSach_input": "S088", "SLNhap": 250, "GiaNhap": 99000 },

  # // Phiếu PN006 (04/01/2024)
  { "MaPhieuNhap_input": "PN006", "MaSach_input": "S102", "SLNhap": 150, "GiaNhap": 135000 },
  { "MaPhieuNhap_input": "PN006", "MaSach_input": "S111", "SLNhap": 210, "GiaNhap": 65000 },
  { "MaPhieuNhap_input": "PN006", "MaSach_input": "S019", "SLNhap": 300, "GiaNhap": 45000 },

  # // Phiếu PN007 (16/01/2024)
  { "MaPhieuNhap_input": "PN007", "MaSach_input": "S124", "SLNhap": 280, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN007", "MaSach_input": "S135", "SLNhap": 180, "GiaNhap": 115000 },
  
  # // Phiếu PN008 (19/02/2024)
  { "MaPhieuNhap_input": "PN008", "MaSach_input": "S005", "SLNhap": 200, "GiaNhap": 105000 },
  { "MaPhieuNhap_input": "PN008", "MaSach_input": "S148", "SLNhap": 250, "GiaNhap": 92000 },

  # // Phiếu PN009 (05/03/2024)
  { "MaPhieuNhap_input": "PN009", "MaSach_input": "S029", "SLNhap": 170, "GiaNhap": 58000 },
  { "MaPhieuNhap_input": "PN009", "MaSach_input": "S157", "SLNhap": 350, "GiaNhap": 78000 },
  { "MaPhieuNhap_input": "PN009", "MaSach_input": "S166", "SLNhap": 160, "GiaNhap": 140000 },

  # // Phiếu PN010 (22/03/2024)
  { "MaPhieuNhap_input": "PN010", "MaSach_input": "S040", "SLNhap": 240, "GiaNhap": 62000 },
  { "MaPhieuNhap_input": "PN010", "MaSach_input": "S177", "SLNhap": 200, "GiaNhap": 102000 },

  # // Phiếu PN011
  { "MaPhieuNhap_input": "PN011", "MaSach_input": "S182", "SLNhap": 180, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN011", "MaSach_input": "S002", "SLNhap": 220, "GiaNhap": 180000 },
  { "MaPhieuNhap_input": "PN011", "MaSach_input": "S045", "SLNhap": 250, "GiaNhap": 70000 },
  { "MaPhieuNhap_input": "PN011", "MaSach_input": "S111", "SLNhap": 160, "GiaNhap": 65000 },
  { "MaPhieuNhap_input": "PN011", "MaSach_input": "S199", "SLNhap": 300, "GiaNhap": 50000 },

  # // Phiếu PN012
  { "MaPhieuNhap_input": "PN012", "MaSach_input": "S190", "SLNhap": 180, "GiaNhap": 70000 },
  { "MaPhieuNhap_input": "PN012", "MaSach_input": "S055", "SLNhap": 300, "GiaNhap": 95000 },
  { "MaPhieuNhap_input": "PN012", "MaSach_input": "S099", "SLNhap": 250, "GiaNhap": 112000 },
  { "MaPhieuNhap_input": "PN012", "MaSach_input": "S012", "SLNhap": 200, "GiaNhap": 60000 },
  { "MaPhieuNhap_input": "PN012", "MaSach_input": "S081", "SLNhap": 170, "GiaNhap": 130000 },
  { "MaPhieuNhap_input": "PN012", "MaSach_input": "S025", "SLNhap": 260, "GiaNhap": 160000 },

  # // Phiếu PN013
  { "MaPhieuNhap_input": "PN013", "MaSach_input": "S115", "SLNhap": 210, "GiaNhap": 83000 },
  { "MaPhieuNhap_input": "PN013", "MaSach_input": "S155", "SLNhap": 180, "GiaNhap": 77000 },
  { "MaPhieuNhap_input": "PN013", "MaSach_input": "S009", "SLNhap": 500, "GiaNhap": 40000 },
  { "MaPhieuNhap_input": "PN013", "MaSach_input": "S077", "SLNhap": 250, "GiaNhap": 94000 },
  { "MaPhieuNhap_input": "PN013", "MaSach_input": "S123", "SLNhap": 160, "GiaNhap": 122000 },

  # // Phiếu PN014
  { "MaPhieuNhap_input": "PN014", "MaSach_input": "S188", "SLNhap": 230, "GiaNhap": 67000 },
  { "MaPhieuNhap_input": "PN014", "MaSach_input": "S200", "SLNhap": 200, "GiaNhap": 79000 },
  { "MaPhieuNhap_input": "PN014", "MaSach_input": "S003", "SLNhap": 210, "GiaNhap": 112000 },
  { "MaPhieuNhap_input": "PN014", "MaSach_input": "S015", "SLNhap": 250, "GiaNhap": 78000 },
  { "MaPhieuNhap_input": "PN014", "MaSach_input": "S031", "SLNhap": 160, "GiaNhap": 128000 },

  # // Phiếu PN015
  { "MaPhieuNhap_input": "PN015", "MaSach_input": "S040", "SLNhap": 240, "GiaNhap": 65000 },
  { "MaPhieuNhap_input": "PN015", "MaSach_input": "S008", "SLNhap": 310, "GiaNhap": 57000 },
  { "MaPhieuNhap_input": "PN015", "MaSach_input": "S102", "SLNhap": 150, "GiaNhap": 138000 },
  { "MaPhieuNhap_input": "PN015", "MaSach_input": "S124", "SLNhap": 280, "GiaNhap": 90000 },
  { "MaPhieuNhap_input": "PN015", "MaSach_input": "S029", "SLNhap": 170, "GiaNhap": 60000 },
  
  # // Phiếu PN016
  { "MaPhieuNhap_input": "PN016", "MaSach_input": "S157", "SLNhap": 350, "GiaNhap": 80000 },
  { "MaPhieuNhap_input": "PN016", "MaSach_input": "S166", "SLNhap": 160, "GiaNhap": 142000 },
  { "MaPhieuNhap_input": "PN016", "MaSach_input": "S177", "SLNhap": 200, "GiaNhap": 105000 },
  { "MaPhieuNhap_input": "PN016", "MaSach_input": "S005", "SLNhap": 200, "GiaNhap": 107000 },
  { "MaPhieuNhap_input": "PN016", "MaSach_input": "S019", "SLNhap": 270, "GiaNhap": 48000 },
  
  # // Phiếu PN017
  { "MaPhieuNhap_input": "PN017", "MaSach_input": "S022", "SLNhap": 190, "GiaNhap": 91000 },
  { "MaPhieuNhap_input": "PN017", "MaSach_input": "S045", "SLNhap": 230, "GiaNhap": 72000 },
  { "MaPhieuNhap_input": "PN017", "MaSach_input": "S050", "SLNhap": 180, "GiaNhap": 98000 },
  { "MaPhieuNhap_input": "PN017", "MaSach_input": "S061", "SLNhap": 210, "GiaNhap": 152000 },
  { "MaPhieuNhap_input": "PN017", "MaSach_input": "S073", "SLNhap": 170, "GiaNhap": 75000 },

  # // Phiếu PN018
  { "MaPhieuNhap_input": "PN018", "MaSach_input": "S088", "SLNhap": 250, "GiaNhap": 101000 },
  { "MaPhieuNhap_input": "PN018", "MaSach_input": "S100", "SLNhap": 150, "GiaNhap": 140000 },
  { "MaPhieuNhap_input": "PN018", "MaSach_input": "S110", "SLNhap": 220, "GiaNhap": 69000 },
  { "MaPhieuNhap_input": "PN018", "MaSach_input": "S120", "SLNhap": 180, "GiaNhap": 118000 },
  { "MaPhieuNhap_input": "PN018", "MaSach_input": "S130", "SLNhap": 290, "GiaNhap": 95000 },

  # // Phiếu PN019
  { "MaPhieuNhap_input": "PN019", "MaSach_input": "S140", "SLNhap": 200, "GiaNhap": 110000 },
  { "MaPhieuNhap_input": "PN019", "MaSach_input": "S150", "SLNhap": 260, "GiaNhap": 82000 },
  { "MaPhieuNhap_input": "PN019", "MaSach_input": "S160", "SLNhap": 170, "GiaNhap": 79000 },
  { "MaPhieuNhap_input": "PN019", "MaSach_input": "S170", "SLNhap": 310, "GiaNhap": 61000 },
  { "MaPhieuNhap_input": "PN019", "MaSach_input": "S180", "SLNhap": 160, "GiaNhap": 148000 },

  # // Phiếu PN020
  { "MaPhieuNhap_input": "PN020", "MaSach_input": "S195", "SLNhap": 240, "GiaNhap": 90000 },
  { "MaPhieuNhap_input": "PN020", "MaSach_input": "S007", "SLNhap": 190, "GiaNhap": 100000 },
  { "MaPhieuNhap_input": "PN020", "MaSach_input": "S017", "SLNhap": 280, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN020", "MaSach_input": "S027", "SLNhap": 150, "GiaNhap": 135000 },
  { "MaPhieuNhap_input": "PN020", "MaSach_input": "S037", "SLNhap": 220, "GiaNhap": 73000 },
  
  # // Phiếu PN021
  { "MaPhieuNhap_input": "PN021", "MaSach_input": "S047", "SLNhap": 300, "GiaNhap": 96000 },
  { "MaPhieuNhap_input": "PN021", "MaSach_input": "S057", "SLNhap": 180, "GiaNhap": 120000 },
  { "MaPhieuNhap_input": "PN021", "MaSach_input": "S067", "SLNhap": 210, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN021", "MaSach_input": "S078", "SLNhap": 250, "GiaNhap": 78000 },
  { "MaPhieuNhap_input": "PN021", "MaSach_input": "S089", "SLNhap": 170, "GiaNhap": 105000 },

  # // Phiếu PN022
  { "MaPhieuNhap_input": "PN022", "MaSach_input": "S091", "SLNhap": 230, "GiaNhap": 92000 },
  { "MaPhieuNhap_input": "PN022", "MaSach_input": "S101", "SLNhap": 200, "GiaNhap": 115000 },
  { "MaPhieuNhap_input": "PN022", "MaSach_input": "S112", "SLNhap": 150, "GiaNhap": 130000 },
  { "MaPhieuNhap_input": "PN022", "MaSach_input": "S122", "SLNhap": 270, "GiaNhap": 80000 },
  { "MaPhieuNhap_input": "PN022", "MaSach_input": "S132", "SLNhap": 190, "GiaNhap": 99000 },

  # // Phiếu PN023
  { "MaPhieuNhap_input": "PN023", "MaSach_input": "S142", "SLNhap": 260, "GiaNhap": 89000 },
  { "MaPhieuNhap_input": "PN023", "MaSach_input": "S152", "SLNhap": 180, "GiaNhap": 125000 },
  { "MaPhieuNhap_input": "PN023", "MaSach_input": "S162", "SLNhap": 220, "GiaNhap": 84000 },
  { "MaPhieuNhap_input": "PN023", "MaSach_input": "S172", "SLNhap": 300, "GiaNhap": 72000 },
  { "MaPhieuNhap_input": "PN023", "MaSach_input": "S183", "SLNhap": 160, "GiaNhap": 140000 },

  # // Phiếu PN024
  { "MaPhieuNhap_input": "PN024", "MaSach_input": "S193", "SLNhap": 240, "GiaNhap": 93000 },
  { "MaPhieuNhap_input": "PN024", "MaSach_input": "S004", "SLNhap": 200, "GiaNhap": 108000 },
  { "MaPhieuNhap_input": "PN024", "MaSach_input": "S014", "SLNhap": 170, "GiaNhap": 118000 },
  { "MaPhieuNhap_input": "PN024", "MaSach_input": "S024", "SLNhap": 280, "GiaNhap": 81000 },
  { "MaPhieuNhap_input": "PN024", "MaSach_input": "S034", "SLNhap": 150, "GiaNhap": 132000 },

  # // Phiếu PN025
  { "MaPhieuNhap_input": "PN025", "MaSach_input": "S044", "SLNhap": 210, "GiaNhap": 97000 },
  { "MaPhieuNhap_input": "PN025", "MaSach_input": "S054", "SLNhap": 250, "GiaNhap": 86000 },
  { "MaPhieuNhap_input": "PN025", "MaSach_input": "S064", "SLNhap": 190, "GiaNhap": 110000 },
  { "MaPhieuNhap_input": "PN025", "MaSach_input": "S074", "SLNhap": 270, "GiaNhap": 76000 },
  { "MaPhieuNhap_input": "PN025", "MaSach_input": "S084", "SLNhap": 180, "GiaNhap": 128000 },
  
  # // Phiếu PN026
  { "MaPhieuNhap_input": "PN026", "MaSach_input": "S094", "SLNhap": 230, "GiaNhap": 94000 },
  { "MaPhieuNhap_input": "PN026", "MaSach_input": "S104", "SLNhap": 200, "GiaNhap": 112000 },
  { "MaPhieuNhap_input": "PN026", "MaSach_input": "S114", "SLNhap": 160, "GiaNhap": 134000 },
  { "MaPhieuNhap_input": "PN026", "MaSach_input": "S125", "SLNhap": 290, "GiaNhap": 83000 },
  { "MaPhieuNhap_input": "PN026", "MaSach_input": "S135", "SLNhap": 150, "GiaNhap": 99000 },

  # // Phiếu PN027
  { "MaPhieuNhap_input": "PN027", "MaSach_input": "S145", "SLNhap": 260, "GiaNhap": 87000 },
  { "MaPhieuNhap_input": "PN027", "MaSach_input": "S156", "SLNhap": 180, "GiaNhap": 122000 },
  { "MaPhieuNhap_input": "PN027", "MaSach_input": "S167", "SLNhap": 220, "GiaNhap": 91000 },
  { "MaPhieuNhap_input": "PN027", "MaSach_input": "S178", "SLNhap": 300, "GiaNhap": 74000 },
  { "MaPhieuNhap_input": "PN027", "MaSach_input": "S189", "SLNhap": 170, "GiaNhap": 141000 },

  # // Phiếu PN028
  { "MaPhieuNhap_input": "PN028", "MaSach_input": "S191", "SLNhap": 240, "GiaNhap": 96000 },
  { "MaPhieuNhap_input": "PN028", "MaSach_input": "S006", "SLNhap": 200, "GiaNhap": 109000 },
  { "MaPhieuNhap_input": "PN028", "MaSach_input": "S016", "SLNhap": 150, "GiaNhap": 119000 },
  { "MaPhieuNhap_input": "PN028", "MaSach_input": "S026", "SLNhap": 280, "GiaNhap": 82000 },
  { "MaPhieuNhap_input": "PN028", "MaSach_input": "S036", "SLNhap": 190, "GiaNhap": 133000 },

  # // Phiếu PN029
  { "MaPhieuNhap_input": "PN029", "MaSach_input": "S046", "SLNhap": 210, "GiaNhap": 98000 },
  { "MaPhieuNhap_input": "PN029", "MaSach_input": "S056", "SLNhap": 250, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN029", "MaSach_input": "S066", "SLNhap": 160, "GiaNhap": 111000 },
  { "MaPhieuNhap_input": "PN029", "MaSach_input": "S076", "SLNhap": 270, "GiaNhap": 75000 },
  { "MaPhieuNhap_input": "PN029", "MaSach_input": "S086", "SLNhap": 180, "GiaNhap": 129000 },

  # // Phiếu PN030
  { "MaPhieuNhap_input": "PN030", "MaSach_input": "S096", "SLNhap": 230, "GiaNhap": 93000 },
  { "MaPhieuNhap_input": "PN030", "MaSach_input": "S106", "SLNhap": 200, "GiaNhap": 113000 },
  { "MaPhieuNhap_input": "PN030", "MaSach_input": "S116", "SLNhap": 170, "GiaNhap": 136000 },
  { "MaPhieuNhap_input": "PN030", "MaSach_input": "S126", "SLNhap": 290, "GiaNhap": 84000 },
  { "MaPhieuNhap_input": "PN030", "MaSach_input": "S136", "SLNhap": 150, "GiaNhap": 101000 },

  # // Phiếu PN031
  { "MaPhieuNhap_input": "PN031", "MaSach_input": "S146", "SLNhap": 260, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN031", "MaSach_input": "S158", "SLNhap": 180, "GiaNhap": 123000 },
  { "MaPhieuNhap_input": "PN031", "MaSach_input": "S168", "SLNhap": 220, "GiaNhap": 90000 },
  { "MaPhieuNhap_input": "PN031", "MaSach_input": "S178", "SLNhap": 300, "GiaNhap": 73000 },
  { "MaPhieuNhap_input": "PN031", "MaSach_input": "S188", "SLNhap": 170, "GiaNhap": 142000 },

  # // Phiếu PN032
  { "MaPhieuNhap_input": "PN032", "MaSach_input": "S198", "SLNhap": 240, "GiaNhap": 97000 },
  { "MaPhieuNhap_input": "PN032", "MaSach_input": "S001", "SLNhap": 400, "GiaNhap": 80000 },
  { "MaPhieuNhap_input": "PN032", "MaSach_input": "S011", "SLNhap": 150, "GiaNhap": 120000 },
  { "MaPhieuNhap_input": "PN032", "MaSach_input": "S021", "SLNhap": 280, "GiaNhap": 83000 },
  { "MaPhieuNhap_input": "PN032", "MaSach_input": "S031", "SLNhap": 190, "GiaNhap": 134000 },

  # // Phiếu PN033
  { "MaPhieuNhap_input": "PN033", "MaSach_input": "S041", "SLNhap": 210, "GiaNhap": 99000 },
  { "MaPhieuNhap_input": "PN033", "MaSach_input": "S051", "SLNhap": 250, "GiaNhap": 86000 },
  { "MaPhieuNhap_input": "PN033", "MaSach_input": "S062", "SLNhap": 160, "GiaNhap": 112000 },
  { "MaPhieuNhap_input": "PN033", "MaSach_input": "S072", "SLNhap": 270, "GiaNhap": 76000 },
  { "MaPhieuNhap_input": "PN033", "MaSach_input": "S082", "SLNhap": 180, "GiaNhap": 130000 },

  # // Phiếu PN034
  { "MaPhieuNhap_input": "PN034", "MaSach_input": "S092", "SLNhap": 230, "GiaNhap": 94000 },
  { "MaPhieuNhap_input": "PN034", "MaSach_input": "S103", "SLNhap": 200, "GiaNhap": 114000 },
  { "MaPhieuNhap_input": "PN034", "MaSach_input": "S113", "SLNhap": 170, "GiaNhap": 137000 },
  { "MaPhieuNhap_input": "PN034", "MaSach_input": "S124", "SLNhap": 290, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN034", "MaSach_input": "S134", "SLNhap": 150, "GiaNhap": 102000 },

  # // Phiếu PN035
  { "MaPhieuNhap_input": "PN035", "MaSach_input": "S144", "SLNhap": 260, "GiaNhap": 89000 },
  { "MaPhieuNhap_input": "PN035", "MaSach_input": "S154", "SLNhap": 180, "GiaNhap": 124000 },
  { "MaPhieuNhap_input": "PN035", "MaSach_input": "S164", "SLNhap": 220, "GiaNhap": 91000 },
  { "MaPhieuNhap_input": "PN035", "MaSach_input": "S174", "SLNhap": 300, "GiaNhap": 74000 },
  { "MaPhieuNhap_input": "PN035", "MaSach_input": "S184", "SLNhap": 170, "GiaNhap": 143000 },

  # // Phiếu PN036
  { "MaPhieuNhap_input": "PN036", "MaSach_input": "S194", "SLNhap": 240, "GiaNhap": 98000 },
  { "MaPhieuNhap_input": "PN036", "MaSach_input": "S008", "SLNhap": 310, "GiaNhap": 58000 },
  { "MaPhieuNhap_input": "PN036", "MaSach_input": "S018", "SLNhap": 150, "GiaNhap": 121000 },
  { "MaPhieuNhap_input": "PN036", "MaSach_input": "S028", "SLNhap": 280, "GiaNhap": 84000 },
  { "MaPhieuNhap_input": "PN036", "MaSach_input": "S038", "SLNhap": 190, "GiaNhap": 135000 },

  # // Phiếu PN037
  { "MaPhieuNhap_input": "PN037", "MaSach_input": "S048", "SLNhap": 210, "GiaNhap": 100000 },
  { "MaPhieuNhap_input": "PN037", "MaSach_input": "S058", "SLNhap": 250, "GiaNhap": 87000 },
  { "MaPhieuNhap_input": "PN037", "MaSach_input": "S068", "SLNhap": 160, "GiaNhap": 113000 },
  { "MaPhieuNhap_input": "PN037", "MaSach_input": "S078", "SLNhap": 270, "GiaNhap": 77000 },
  { "MaPhieuNhap_input": "PN037", "MaSach_input": "S087", "SLNhap": 180, "GiaNhap": 131000 },

  # // Phiếu PN038
  { "MaPhieuNhap_input": "PN038", "MaSach_input": "S097", "SLNhap": 230, "GiaNhap": 95000 },
  { "MaPhieuNhap_input": "PN038", "MaSach_input": "S107", "SLNhap": 200, "GiaNhap": 115000 },
  { "MaPhieuNhap_input": "PN038", "MaSach_input": "S117", "SLNhap": 170, "GiaNhap": 138000 },
  { "MaPhieuNhap_input": "PN038", "MaSach_input": "S127", "SLNhap": 290, "GiaNhap": 86000 },
  { "MaPhieuNhap_input": "PN038", "MaSach_input": "S137", "SLNhap": 150, "GiaNhap": 103000 },

  # // Phiếu PN039
  { "MaPhieuNhap_input": "PN039", "MaSach_input": "S147", "SLNhap": 260, "GiaNhap": 90000 },
  { "MaPhieuNhap_input": "PN039", "MaSach_input": "S157", "SLNhap": 180, "GiaNhap": 125000 },
  { "MaPhieuNhap_input": "PN039", "MaSach_input": "S167", "SLNhap": 220, "GiaNhap": 92000 },
  { "MaPhieuNhap_input": "PN039", "MaSach_input": "S176", "SLNhap": 300, "GiaNhap": 75000 },
  { "MaPhieuNhap_input": "PN039", "MaSach_input": "S186", "SLNhap": 170, "GiaNhap": 144000 },

  # // Phiếu PN040
  { "MaPhieuNhap_input": "PN040", "MaSach_input": "S196", "SLNhap": 240, "GiaNhap": 99000 },
  { "MaPhieuNhap_input": "PN040", "MaSach_input": "S013", "SLNhap": 200, "GiaNhap": 107000 },
  { "MaPhieuNhap_input": "PN040", "MaSach_input": "S023", "SLNhap": 150, "GiaNhap": 122000 },
  { "MaPhieuNhap_input": "PN040", "MaSach_input": "S033", "SLNhap": 280, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN040", "MaSach_input": "S043", "SLNhap": 190, "GiaNhap": 136000 },

  # // ... (Tiếp tục cho các phiếu còn lại)

  { "MaPhieuNhap_input": "PN041", "MaSach_input": "S182", "SLNhap": 180, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN041", "MaSach_input": "S002", "SLNhap": 220, "GiaNhap": 180000 },
  { "MaPhieuNhap_input": "PN041", "MaSach_input": "S045", "SLNhap": 250, "GiaNhap": 70000 },
  { "MaPhieuNhap_input": "PN041", "MaSach_input": "S111", "SLNhap": 160, "GiaNhap": 65000 },
  { "MaPhieuNhap_input": "PN041", "MaSach_input": "S199", "SLNhap": 300, "GiaNhap": 50000 },

  # // Phiếu PN012
  { "MaPhieuNhap_input": "PN042", "MaSach_input": "S190", "SLNhap": 180, "GiaNhap": 70000 },
  { "MaPhieuNhap_input": "PN042", "MaSach_input": "S055", "SLNhap": 300, "GiaNhap": 95000 },
  { "MaPhieuNhap_input": "PN042", "MaSach_input": "S099", "SLNhap": 250, "GiaNhap": 112000 },
  { "MaPhieuNhap_input": "PN042", "MaSach_input": "S012", "SLNhap": 200, "GiaNhap": 60000 },
  { "MaPhieuNhap_input": "PN042", "MaSach_input": "S081", "SLNhap": 170, "GiaNhap": 130000 },
  { "MaPhieuNhap_input": "PN042", "MaSach_input": "S025", "SLNhap": 260, "GiaNhap": 160000 },

  # // Phiếu PN013
  { "MaPhieuNhap_input": "PN043", "MaSach_input": "S115", "SLNhap": 210, "GiaNhap": 83000 },
  { "MaPhieuNhap_input": "PN043", "MaSach_input": "S155", "SLNhap": 180, "GiaNhap": 77000 },
  { "MaPhieuNhap_input": "PN043", "MaSach_input": "S009", "SLNhap": 500, "GiaNhap": 40000 },
  { "MaPhieuNhap_input": "PN043", "MaSach_input": "S077", "SLNhap": 250, "GiaNhap": 94000 },
  { "MaPhieuNhap_input": "PN043", "MaSach_input": "S123", "SLNhap": 160, "GiaNhap": 122000 },

  # // Phiếu PN014
  { "MaPhieuNhap_input": "PN044", "MaSach_input": "S188", "SLNhap": 230, "GiaNhap": 67000 },
  { "MaPhieuNhap_input": "PN044", "MaSach_input": "S200", "SLNhap": 200, "GiaNhap": 79000 },
  { "MaPhieuNhap_input": "PN044", "MaSach_input": "S003", "SLNhap": 210, "GiaNhap": 112000 },
  { "MaPhieuNhap_input": "PN044", "MaSach_input": "S015", "SLNhap": 250, "GiaNhap": 78000 },
  { "MaPhieuNhap_input": "PN044", "MaSach_input": "S031", "SLNhap": 160, "GiaNhap": 128000 },

  # // Phiếu PN015
  { "MaPhieuNhap_input": "PN045", "MaSach_input": "S040", "SLNhap": 240, "GiaNhap": 65000 },
  { "MaPhieuNhap_input": "PN045", "MaSach_input": "S008", "SLNhap": 310, "GiaNhap": 57000 },
  { "MaPhieuNhap_input": "PN045", "MaSach_input": "S102", "SLNhap": 150, "GiaNhap": 138000 },
  { "MaPhieuNhap_input": "PN045", "MaSach_input": "S124", "SLNhap": 280, "GiaNhap": 90000 },
  { "MaPhieuNhap_input": "PN045", "MaSach_input": "S029", "SLNhap": 170, "GiaNhap": 60000 },
  { "MaPhieuNhap_input": "PN045", "MaSach_input": "S157", "SLNhap": 350, "GiaNhap": 80000 },
  
  # // Phiếu PN016
  { "MaPhieuNhap_input": "PN046", "MaSach_input": "S166", "SLNhap": 160, "GiaNhap": 142000 },
  { "MaPhieuNhap_input": "PN046", "MaSach_input": "S177", "SLNhap": 200, "GiaNhap": 105000 },
  { "MaPhieuNhap_input": "PN046", "MaSach_input": "S005", "SLNhap": 200, "GiaNhap": 107000 },
  { "MaPhieuNhap_input": "PN046", "MaSach_input": "S019", "SLNhap": 270, "GiaNhap": 48000 },
  { "MaPhieuNhap_input": "PN046", "MaSach_input": "S022", "SLNhap": 190, "GiaNhap": 91000 },
  
  # // Phiếu PN017
  { "MaPhieuNhap_input": "PN047", "MaSach_input": "S045", "SLNhap": 230, "GiaNhap": 72000 },
  { "MaPhieuNhap_input": "PN047", "MaSach_input": "S050", "SLNhap": 180, "GiaNhap": 98000 },
  { "MaPhieuNhap_input": "PN047", "MaSach_input": "S061", "SLNhap": 210, "GiaNhap": 152000 },
  { "MaPhieuNhap_input": "PN047", "MaSach_input": "S073", "SLNhap": 170, "GiaNhap": 75000 },
  { "MaPhieuNhap_input": "PN047", "MaSach_input": "S088", "SLNhap": 250, "GiaNhap": 101000 },

  { "MaPhieuNhap_input": "PN048", "MaSach_input": "S112", "SLNhap": 150, "GiaNhap": 95000 },
  { "MaPhieuNhap_input": "PN048", "MaSach_input": "S113", "SLNhap": 200, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN048", "MaSach_input": "S114", "SLNhap": 250, "GiaNhap": 75000 },
  { "MaPhieuNhap_input": "PN048", "MaSach_input": "S116", "SLNhap": 180, "GiaNhap": 115000 },
  { "MaPhieuNhap_input": "PN048", "MaSach_input": "S117", "SLNhap": 300, "GiaNhap": 65000 },

  # // Phiếu PN041
  { "MaPhieuNhap_input": "PN049", "MaSach_input": "S118", "SLNhap": 220, "GiaNhap": 92000 },
  { "MaPhieuNhap_input": "PN049", "MaSach_input": "S119", "SLNhap": 170, "GiaNhap": 120000 },
  { "MaPhieuNhap_input": "PN049", "MaSach_input": "S120", "SLNhap": 280, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN049", "MaSach_input": "S121", "SLNhap": 190, "GiaNhap": 105000 },
  { "MaPhieuNhap_input": "PN049", "MaSach_input": "S122", "SLNhap": 240, "GiaNhap": 78000 },

  # // Phiếu PN050
  { "MaPhieuNhap_input": "PN050", "MaSach_input": "S053", "SLNhap": 210, "GiaNhap": 101000 },
  { "MaPhieuNhap_input": "PN050", "MaSach_input": "S063", "SLNhap": 250, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN050", "MaSach_input": "S075", "SLNhap": 160, "GiaNhap": 114000 },
  { "MaPhieuNhap_input": "PN050", "MaSach_input": "S085", "SLNhap": 270, "GiaNhap": 78000 },
  { "MaPhieuNhap_input": "PN050", "MaSach_input": "S095", "SLNhap": 180, "GiaNhap": 132000 },

  # // Phiếu PN051
  { "MaPhieuNhap_input": "PN051", "MaSach_input": "S105", "SLNhap": 230, "GiaNhap": 96000 },
  { "MaPhieuNhap_input": "PN051", "MaSach_input": "S115", "SLNhap": 200, "GiaNhap": 116000 },
  { "MaPhieuNhap_input": "PN051", "MaSach_input": "S125", "SLNhap": 170, "GiaNhap": 139000 },
  { "MaPhieuNhap_input": "PN051", "MaSach_input": "S138", "SLNhap": 290, "GiaNhap": 87000 },
  { "MaPhieuNhap_input": "PN051", "MaSach_input": "S148", "SLNhap": 150, "GiaNhap": 104000 },
  
  # // Phiếu PN052
  { "MaPhieuNhap_input": "PN052", "MaSach_input": "S158", "SLNhap": 260, "GiaNhap": 91000 },
  { "MaPhieuNhap_input": "PN052", "MaSach_input": "S169", "SLNhap": 180, "GiaNhap": 126000 },
  { "MaPhieuNhap_input": "PN052", "MaSach_input": "S179", "SLNhap": 220, "GiaNhap": 93000 },
  { "MaPhieuNhap_input": "PN052", "MaSach_input": "S189", "SLNhap": 300, "GiaNhap": 76000 },
  { "MaPhieuNhap_input": "PN052", "MaSach_input": "S199", "SLNhap": 170, "GiaNhap": 145000 },

  { "MaPhieuNhap_input": "PN053", "MaSach_input": "S125", "SLNhap": 160, "GiaNhap": 99000 },
  { "MaPhieuNhap_input": "PN053", "MaSach_input": "S126", "SLNhap": 210, "GiaNhap": 82000 },
  { "MaPhieuNhap_input": "PN053", "MaSach_input": "S127", "SLNhap": 260, "GiaNhap": 73000 },
  { "MaPhieuNhap_input": "PN053", "MaSach_input": "S128", "SLNhap": 155, "GiaNhap": 118000 },
  { "MaPhieuNhap_input": "PN053", "MaSach_input": "S129", "SLNhap": 310, "GiaNhap": 69000 },

  # // ... (Tiếp tục cho các phiếu còn lại)
  
  # // Phiếu PN068
  { "MaPhieuNhap_input": "PN054", "MaSach_input": "S188", "SLNhap": 230, "GiaNhap": 72000 },
  { "MaPhieuNhap_input": "PN054", "MaSach_input": "S001", "SLNhap": 400, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN054", "MaSach_input": "S010", "SLNhap": 250, "GiaNhap": 95000 },
  { "MaPhieuNhap_input": "PN054", "MaSach_input": "S020", "SLNhap": 180, "GiaNhap": 105000 },
  { "MaPhieuNhap_input": "PN054", "MaSach_input": "S030", "SLNhap": 160, "GiaNhap": 115000 },

  # // Phiếu PN069
  { "MaPhieuNhap_input": "PN055", "MaSach_input": "S200", "SLNhap": 200, "GiaNhap": 85000 },
  { "MaPhieuNhap_input": "PN055", "MaSach_input": "S198", "SLNhap": 220, "GiaNhap": 76000 },
  { "MaPhieuNhap_input": "PN055", "MaSach_input": "S197", "SLNhap": 300, "GiaNhap": 92000 },
  { "MaPhieuNhap_input": "PN055", "MaSach_input": "S196", "SLNhap": 170, "GiaNhap": 110000 },
  { "MaPhieuNhap_input": "PN055", "MaSach_input": "S195", "SLNhap": 250, "GiaNhap": 68000 },
  { "MaPhieuNhap_input": "PN055", "MaSach_input": "S194", "SLNhap": 150, "GiaNhap": 130000 },

  # // Phiếu PN070
  { "MaPhieuNhap_input": "PN056", "MaSach_input": "S001", "SLNhap": 450, "GiaNhap": 86000 },
  { "MaPhieuNhap_input": "PN056", "MaSach_input": "S011", "SLNhap": 200, "GiaNhap": 99000 },
  { "MaPhieuNhap_input": "PN056", "MaSach_input": "S021", "SLNhap": 180, "GiaNhap": 102000 },
  { "MaPhieuNhap_input": "PN056", "MaSach_input": "S032", "SLNhap": 260, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN056", "MaSach_input": "S042", "SLNhap": 310, "GiaNhap": 74000 },

  { "MaPhieuNhap_input": "PN057", "MaSach_input": "S083", "SLNhap": 250, "GiaNhap": 92000 },
  { "MaPhieuNhap_input": "PN057", "MaSach_input": "S105", "SLNhap": 180, "GiaNhap": 120000 },
  { "MaPhieuNhap_input": "PN057", "MaSach_input": "S014", "SLNhap": 300, "GiaNhap": 75000 },
  { "MaPhieuNhap_input": "PN057", "MaSach_input": "S192", "SLNhap": 160, "GiaNhap": 145000 },
  { "MaPhieuNhap_input": "PN057", "MaSach_input": "S053", "SLNhap": 220, "GiaNhap": 88000 },

  # // Phiếu PN058
  { "MaPhieuNhap_input": "PN058", "MaSach_input": "S039", "SLNhap": 170, "GiaNhap": 110000 },
  { "MaPhieuNhap_input": "PN058", "MaSach_input": "S117", "SLNhap": 240, "GiaNhap": 95000 },
  { "MaPhieuNhap_input": "PN058", "MaSach_input": "S181", "SLNhap": 200, "GiaNhap": 81000 },
  { "MaPhieuNhap_input": "PN058", "MaSach_input": "S093", "SLNhap": 350, "GiaNhap": 65000 },
  { "MaPhieuNhap_input": "PN058", "MaSach_input": "S149", "SLNhap": 150, "GiaNhap": 150000 },
  { "MaPhieuNhap_input": "PN058", "MaSach_input": "S004", "SLNhap": 260, "GiaNhap": 105000 },

  # // Phiếu PN059
  { "MaPhieuNhap_input": "PN059", "MaSach_input": "S133", "SLNhap": 280, "GiaNhap": 89000 },
  { "MaPhieuNhap_input": "PN059", "MaSach_input": "S067", "SLNhap": 190, "GiaNhap": 125000 },
  { "MaPhieuNhap_input": "PN059", "MaSach_input": "S176", "SLNhap": 210, "GiaNhap": 98000 },
  { "MaPhieuNhap_input": "PN059", "MaSach_input": "S082", "SLNhap": 160, "GiaNhap": 132000 },
  { "MaPhieuNhap_input": "PN059", "MaSach_input": "S156", "SLNhap": 320, "GiaNhap": 77000 },

  # // Phiếu PN060
  { "MaPhieuNhap_input": "PN060", "MaSach_input": "S010", "SLNhap": 240, "GiaNhap": 100000 },
  { "MaPhieuNhap_input": "PN060", "MaSach_input": "S020", "SLNhap": 200, "GiaNhap": 108000 },
  { "MaPhieuNhap_input": "PN060", "MaSach_input": "S030", "SLNhap": 150, "GiaNhap": 123000 },
  { "MaPhieuNhap_input": "PN060", "MaSach_input": "S049", "SLNhap": 280, "GiaNhap": 86000 },
  { "MaPhieuNhap_input": "PN060", "MaSach_input": "S059", "SLNhap": 190, "GiaNhap": 137000 },

  # // Phiếu PN061
  { "MaPhieuNhap_input": "PN061", "MaSach_input": "S069", "SLNhap": 210, "GiaNhap": 102000 },
  { "MaPhieuNhap_input": "PN061", "MaSach_input": "S079", "SLNhap": 250, "GiaNhap": 89000 },
  { "MaPhieuNhap_input": "PN061", "MaSach_input": "S089", "SLNhap": 160, "GiaNhap": 115000 },
  { "MaPhieuNhap_input": "PN061", "MaSach_input": "S098", "SLNhap": 270, "GiaNhap": 79000 },
  { "MaPhieuNhap_input": "PN061", "MaSach_input": "S108", "SLNhap": 180, "GiaNhap": 133000 },

  # // Phiếu PN062
  { "MaPhieuNhap_input": "PN062", "MaSach_input": "S118", "SLNhap": 230, "GiaNhap": 97000 },
  { "MaPhieuNhap_input": "PN062", "MaSach_input": "S128", "SLNhap": 200, "GiaNhap": 117000 },
  { "MaPhieuNhap_input": "PN062", "MaSach_input": "S138", "SLNhap": 170, "GiaNhap": 140000 },
  { "MaPhieuNhap_input": "PN062", "MaSach_input": "S149", "SLNhap": 290, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN062", "MaSach_input": "S159", "SLNhap": 150, "GiaNhap": 105000 },

  # // Phiếu PN063
  { "MaPhieuNhap_input": "PN063", "MaSach_input": "S165", "SLNhap": 260, "GiaNhap": 92000 },
  { "MaPhieuNhap_input": "PN063", "MaSach_input": "S175", "SLNhap": 180, "GiaNhap": 127000 },
  { "MaPhieuNhap_input": "PN063", "MaSach_input": "S185", "SLNhap": 220, "GiaNhap": 94000 },
  { "MaPhieuNhap_input": "PN063", "MaSach_input": "S195", "SLNhap": 300, "GiaNhap": 77000 },
  { "MaPhieuNhap_input": "PN063", "MaSach_input": "S005", "SLNhap": 170, "GiaNhap": 146000 },

  # // Phiếu PN064
  { "MaPhieuNhap_input": "PN064", "MaSach_input": "S015", "SLNhap": 240, "GiaNhap": 101000 },
  { "MaPhieuNhap_input": "PN064", "MaSach_input": "S025", "SLNhap": 200, "GiaNhap": 109000 },
  { "MaPhieuNhap_input": "PN064", "MaSach_input": "S035", "SLNhap": 150, "GiaNhap": 124000 },
  { "MaPhieuNhap_input": "PN064", "MaSach_input": "S045", "SLNhap": 280, "GiaNhap": 87000 },
  { "MaPhieuNhap_input": "PN064", "MaSach_input": "S052", "SLNhap": 190, "GiaNhap": 138000 },
  
  # // Phiếu PN065
  { "MaPhieuNhap_input": "PN065", "MaSach_input": "S062", "SLNhap": 210, "GiaNhap": 103000 },
  { "MaPhieuNhap_input": "PN065", "MaSach_input": "S071", "SLNhap": 250, "GiaNhap": 90000 },
  { "MaPhieuNhap_input": "PN065", "MaSach_input": "S081", "SLNhap": 160, "GiaNhap": 116000 },
  { "MaPhieuNhap_input": "PN065", "MaSach_input": "S091", "SLNhap": 270, "GiaNhap": 80000 },
  { "MaPhieuNhap_input": "PN065", "MaSach_input": "S109", "SLNhap": 180, "GiaNhap": 134000 },
  
  # // Phiếu PN066
  { "MaPhieuNhap_input": "PN066", "MaSach_input": "S119", "SLNhap": 230, "GiaNhap": 98000 },
  { "MaPhieuNhap_input": "PN066", "MaSach_input": "S129", "SLNhap": 200, "GiaNhap": 118000 },
  { "MaPhieuNhap_input": "PN066", "MaSach_input": "S139", "SLNhap": 170, "GiaNhap": 141000 },
  { "MaPhieuNhap_input": "PN066", "MaSach_input": "S143", "SLNhap": 290, "GiaNhap": 89000 },
  { "MaPhieuNhap_input": "PN066", "MaSach_input": "S153", "SLNhap": 150, "GiaNhap": 106000 },

  # // Phiếu PN067
  { "MaPhieuNhap_input": "PN067", "MaSach_input": "S163", "SLNhap": 260, "GiaNhap": 93000 },
  { "MaPhieuNhap_input": "PN067", "MaSach_input": "S173", "SLNhap": 180, "GiaNhap": 128000 },
  { "MaPhieuNhap_input": "PN067", "MaSach_input": "S187", "SLNhap": 220, "GiaNhap": 95000 },
  { "MaPhieuNhap_input": "PN067", "MaSach_input": "S197", "SLNhap": 300, "GiaNhap": 78000 },
  { "MaPhieuNhap_input": "PN067", "MaSach_input": "S007", "SLNhap": 170, "GiaNhap": 147000 },

  # // Phiếu PN068
  { "MaPhieuNhap_input": "PN068", "MaSach_input": "S018", "SLNhap": 240, "GiaNhap": 102000 },
  { "MaPhieuNhap_input": "PN068", "MaSach_input": "S028", "SLNhap": 200, "GiaNhap": 110000 },
  { "MaPhieuNhap_input": "PN068", "MaSach_input": "S038", "SLNhap": 150, "GiaNhap": 125000 },
  { "MaPhieuNhap_input": "PN068", "MaSach_input": "S048", "SLNhap": 280, "GiaNhap": 88000 },
  { "MaPhieuNhap_input": "PN068", "MaSach_input": "S058", "SLNhap": 190, "GiaNhap": 139000 },

  # // Phiếu PN069
  { "MaPhieuNhap_input": "PN069", "MaSach_input": "S060", "SLNhap": 210, "GiaNhap": 104000 },
  { "MaPhieuNhap_input": "PN069", "MaSach_input": "S070", "SLNhap": 250, "GiaNhap": 91000 },
  { "MaPhieuNhap_input": "PN069", "MaSach_input": "S080", "SLNhap": 160, "GiaNhap": 117000 },
  { "MaPhieuNhap_input": "PN069", "MaSach_input": "S090", "SLNhap": 270, "GiaNhap": 81000 },
  { "MaPhieuNhap_input": "PN069", "MaSach_input": "S100", "SLNhap": 180, "GiaNhap": 135000 },

  # // Phiếu PN070
  { "MaPhieuNhap_input": "PN070", "MaSach_input": "S121", "SLNhap": 230, "GiaNhap": 99000 },
  { "MaPhieuNhap_input": "PN070", "MaSach_input": "S131", "SLNhap": 200, "GiaNhap": 119000 },
  { "MaPhieuNhap_input": "PN070", "MaSach_input": "S141", "SLNhap": 170, "GiaNhap": 142000 },
  { "MaPhieuNhap_input": "PN070", "MaSach_input": "S151", "SLNhap": 290, "GiaNhap": 90000 },
  { "MaPhieuNhap_input": "PN070", "MaSach_input": "S161", "SLNhap": 150, "GiaNhap": 107000 }
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