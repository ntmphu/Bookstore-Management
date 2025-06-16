# bulk_add_hoadon.py

import os
import django

# Cấu hình settings cho Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Đổi 'tenproject' thành tên project của bạn
django.setup()

from api.serializers import CTHoaDonSerializer

ct_hoa_don_data = [
  #HD001
  { "MaHD_input": "HD001", "MaSach_input": "S001", "SLBan": 3 },
  { "MaHD_input": "HD001", "MaSach_input": "S008", "SLBan": 2 },
  
  #HD002
  { "MaHD_input": "HD002", "MaSach_input": "S015", "SLBan": 5 },
  { "MaHD_input": "HD002", "MaSach_input": "S022", "SLBan": 1 },
  { "MaHD_input": "HD002", "MaSach_input": "S031", "SLBan": 4 },

  #HD003
  { "MaHD_input": "HD003", "MaSach_input": "S050", "SLBan": 10 },

  #HD004
  { "MaHD_input": "HD004", "MaSach_input": "S102", "SLBan": 2 },
  { "MaHD_input": "HD004", "MaSach_input": "S124", "SLBan": 3 },
  { "MaHD_input": "HD004", "MaSach_input": "S157", "SLBan": 1 },

  #HD005
  { "MaHD_input": "HD005", "MaSach_input": "S045", "SLBan": 6 },
  { "MaHD_input": "HD005", "MaSach_input": "S111", "SLBan": 2 },

  #HD006
  { "MaHD_input": "HD006", "MaSach_input": "S009", "SLBan": 20 },
  { "MaHD_input": "HD006", "MaSach_input": "S077", "SLBan": 3 },
  { "MaHD_input": "HD006", "MaSach_input": "S199", "SLBan": 5 },

  #HD007
  { "MaHD_input": "HD007", "MaSach_input": "S200", "SLBan": 8 },
  { "MaHD_input": "HD007", "MaSach_input": "S188", "SLBan": 1 },
  { "MaHD_input": "HD007", "MaSach_input": "S123", "SLBan": 4 },
  { "MaHD_input": "HD007", "MaSach_input": "S061", "SLBan": 2 },

  #HD008
  { "MaHD_input": "HD008", "MaSach_input": "S002", "SLBan": 7 },

  #HD009
  { "MaHD_input": "HD009", "MaSach_input": "S019", "SLBan": 12 },
  { "MaHD_input": "HD009", "MaSach_input": "S029", "SLBan": 3 },

  #HD010
  { "MaHD_input": "HD010", "MaSach_input": "S055", "SLBan": 4 },
  { "MaHD_input": "HD010", "MaSach_input": "S099", "SLBan": 1 },
  { "MaHD_input": "HD010", "MaSach_input": "S177", "SLBan": 2 },
  
  #HD011
  { "MaHD_input": "HD011", "MaSach_input": "S012", "SLBan": 6 },
  { "MaHD_input": "HD011", "MaSach_input": "S081", "SLBan": 3 },

  #HD012
  { "MaHD_input": "HD012", "MaSach_input": "S025", "SLBan": 8 },
  { "MaHD_input": "HD012", "MaSach_input": "S115", "SLBan": 5 },
  { "MaHD_input": "HD012", "MaSach_input": "S155", "SLBan": 2 },

  #HD013
  { "MaHD_input": "HD013", "MaSach_input": "S182", "SLBan": 1 },
  { "MaHD_input": "HD013", "MaSach_input": "S190", "SLBan": 3 },
  
  #HD014
  { "MaHD_input": "HD014", "MaSach_input": "S003", "SLBan": 9 },
  
  #HD015
  { "MaHD_input": "HD015", "MaSach_input": "S040", "SLBan": 4 },
  { "MaHD_input": "HD015", "MaSach_input": "S135", "SLBan": 1 },
  { "MaHD_input": "HD015", "MaSach_input": "S148", "SLBan": 2 },
  { "MaHD_input": "HD015", "MaSach_input": "S166", "SLBan": 3 },

  #HD016
  { "MaHD_input": "HD016", "MaSach_input": "S005", "SLBan": 6 },
  { "MaHD_input": "HD016", "MaSach_input": "S073", "SLBan": 2 },

  #HD017
  { "MaHD_input": "HD017", "MaSach_input": "S088", "SLBan": 7 },
  { "MaHD_input": "HD017", "MaSach_input": "S100", "SLBan": 3 },

  #HD018
  { "MaHD_input": "HD018", "MaSach_input": "S001", "SLBan": 15 },
  
  #HD019
  { "MaHD_input": "HD019", "MaSach_input": "S110", "SLBan": 1 },
  { "MaHD_input": "HD019", "MaSach_input": "S120", "SLBan": 5 },
  
  #HD020
  { "MaHD_input": "HD020", "MaSach_input": "S130", "SLBan": 2 },
  { "MaHD_input": "HD020", "MaSach_input": "S140", "SLBan": 3 },
  { "MaHD_input": "HD020", "MaSach_input": "S150", "SLBan": 4 },
  { "MaHD_input": "HD020", "MaSach_input": "S160", "SLBan": 1 },

  #HD021
  { "MaHD_input": "HD021", "MaSach_input": "S170", "SLBan": 8 },
  { "MaHD_input": "HD021", "MaSach_input": "S180", "SLBan": 2 },
  
  #HD022
  { "MaHD_input": "HD022", "MaSach_input": "S195", "SLBan": 5 },
  { "MaHD_input": "HD022", "MaSach_input": "S007", "SLBan": 3 },

  #HD023
  { "MaHD_input": "HD023", "MaSach_input": "S017", "SLBan": 10 },

  #HD024
  { "MaHD_input": "HD024", "MaSach_input": "S027", "SLBan": 4 },
  { "MaHD_input": "HD024", "MaSach_input": "S037", "SLBan": 2 },
  { "MaHD_input": "HD024", "MaSach_input": "S047", "SLBan": 1 },

  #HD025
  { "MaHD_input": "HD025", "MaSach_input": "S057", "SLBan": 7 },
  { "MaHD_input": "HD025", "MaSach_input": "S067", "SLBan": 2 },

  #HD026
  { "MaHD_input": "HD026", "MaSach_input": "S078", "SLBan": 3 },
  { "MaHD_input": "HD026", "MaSach_input": "S089", "SLBan": 5 },

  #HD027
  { "MaHD_input": "HD027", "MaSach_input": "S091", "SLBan": 1 },
  { "MaHD_input": "HD027", "MaSach_input": "S101", "SLBan": 6 },
  { "MaHD_input": "HD027", "MaSach_input": "S112", "SLBan": 2 },
  { "MaHD_input": "HD027", "MaSach_input": "S122", "SLBan": 4 },

  #HD028
  { "MaHD_input": "HD028", "MaSach_input": "S132", "SLBan": 9 },

  #HD029
  { "MaHD_input": "HD029", "MaSach_input": "S142", "SLBan": 3 },
  { "MaHD_input": "HD029", "MaSach_input": "S152", "SLBan": 5 },

  #HD030
  { "MaHD_input": "HD030", "MaSach_input": "S162", "SLBan": 2 },
  { "MaHD_input": "HD030", "MaSach_input": "S172", "SLBan": 4 },
  { "MaHD_input": "HD030", "MaSach_input": "S183", "SLBan": 1 },
  
  #HD031
  { "MaHD_input": "HD031", "MaSach_input": "S193", "SLBan": 7 },
  { "MaHD_input": "HD031", "MaSach_input": "S004", "SLBan": 3 },

  #HD032
  { "MaHD_input": "HD032", "MaSach_input": "S014", "SLBan": 11 },
  { "MaHD_input": "HD032", "MaSach_input": "S024", "SLBan": 2 },

  #HD033
  { "MaHD_input": "HD033", "MaSach_input": "S034", "SLBan": 5 },
  
  #HD034
  { "MaHD_input": "HD034", "MaSach_input": "S044", "SLBan": 2 },
  { "MaHD_input": "HD034", "MaSach_input": "S054", "SLBan": 3 },
  { "MaHD_input": "HD034", "MaSach_input": "S064", "SLBan": 1 },
  
  #HD035
  { "MaHD_input": "HD035", "MaSach_input": "S074", "SLBan": 6 },
  { "MaHD_input": "HD035", "MaSach_input": "S084", "SLBan": 4 },

  #HD036
  { "MaHD_input": "HD036", "MaSach_input": "S094", "SLBan": 8 },
  { "MaHD_input": "HD036", "MaSach_input": "S104", "SLBan": 1 },
  { "MaHD_input": "HD036", "MaSach_input": "S114", "SLBan": 2 },

  #HD037
  { "MaHD_input": "HD037", "MaSach_input": "S125", "SLBan": 5 },
  { "MaHD_input": "HD037", "MaSach_input": "S135", "SLBan": 3 },

  #HD038
  { "MaHD_input": "HD038", "MaSach_input": "S145", "SLBan": 10 },
  
  #HD039
  { "MaHD_input": "HD039", "MaSach_input": "S156", "SLBan": 4 },
  { "MaHD_input": "HD039", "MaSach_input": "S167", "SLBan": 1 },
  { "MaHD_input": "HD039", "MaSach_input": "S178", "SLBan": 3 },

  #HD040
  { "MaHD_input": "HD040", "MaSach_input": "S189", "SLBan": 2 },
  { "MaHD_input": "HD040", "MaSach_input": "S191", "SLBan": 5 },
  
  #HD041
  { "MaHD_input": "HD041", "MaSach_input": "S006", "SLBan": 7 },
  { "MaHD_input": "HD041", "MaSach_input": "S016", "SLBan": 2 },
  { "MaHD_input": "HD041", "MaSach_input": "S026", "SLBan": 4 },
  { "MaHD_input": "HD041", "MaSach_input": "S036", "SLBan": 1 },
  
  #HD042
  { "MaHD_input": "HD042", "MaSach_input": "S046", "SLBan": 9 },
  { "MaHD_input": "HD042", "MaSach_input": "S056", "SLBan": 3 },
  
  #HD043
  { "MaHD_input": "HD043", "MaSach_input": "S066", "SLBan": 6 },
  
  #HD044
  { "MaHD_input": "HD044", "MaSach_input": "S076", "SLBan": 2 },
  { "MaHD_input": "HD044", "MaSach_input": "S086", "SLBan": 4 },

  #HD045
  { "MaHD_input": "HD045", "MaSach_input": "S096", "SLBan": 1 },
  { "MaHD_input": "HD045", "MaSach_input": "S106", "SLBan": 5 },
  { "MaHD_input": "HD045", "MaSach_input": "S116", "SLBan": 3 },
  
  #HD046
  { "MaHD_input": "HD046", "MaSach_input": "S126", "SLBan": 8 },
  { "MaHD_input": "HD046", "MaSach_input": "S136", "SLBan": 2 },

  #HD047
  { "MaHD_input": "HD047", "MaSach_input": "S146", "SLBan": 6 },
  { "MaHD_input": "HD047", "MaSach_input": "S158", "SLBan": 3 },

  #HD048
  { "MaHD_input": "HD048", "MaSach_input": "S168", "SLBan": 12 },
  
  #HD049
  { "MaHD_input": "HD049", "MaSach_input": "S178", "SLBan": 4 },
  { "MaHD_input": "HD049", "MaSach_input": "S188", "SLBan": 2 },
  
  #HD050
  { "MaHD_input": "HD050", "MaSach_input": "S198", "SLBan": 1 },
  { "MaHD_input": "HD050", "MaSach_input": "S011", "SLBan": 5 },
  { "MaHD_input": "HD050", "MaSach_input": "S021", "SLBan": 3 },
  { "MaHD_input": "HD050", "MaSach_input": "S031", "SLBan": 6 },

  #HD051
  { "MaHD_input": "HD051", "MaSach_input": "S041", "SLBan": 2 },
  { "MaHD_input": "HD051", "MaSach_input": "S051", "SLBan": 7 },

  #HD052
  { "MaHD_input": "HD052", "MaSach_input": "S062", "SLBan": 4 },
  { "MaHD_input": "HD052", "MaSach_input": "S072", "SLBan": 1 },
  { "MaHD_input": "HD052", "MaSach_input": "S082", "SLBan": 3 },
  
  #HD053
  { "MaHD_input": "HD053", "MaSach_input": "S092", "SLBan": 9 },
  
  #HD054
  { "MaHD_input": "HD054", "MaSach_input": "S103", "SLBan": 2 },
  { "MaHD_input": "HD054", "MaSach_input": "S113", "SLBan": 5 },

  #HD055
  { "MaHD_input": "HD055", "MaSach_input": "S124", "SLBan": 6 },
  { "MaHD_input": "HD055", "MaSach_input": "S134", "SLBan": 3 },
  { "MaHD_input": "HD055", "MaSach_input": "S144", "SLBan": 1 },

  #HD056
  { "MaHD_input": "HD056", "MaSach_input": "S154", "SLBan": 8 },
  { "MaHD_input": "HD056", "MaSach_input": "S164", "SLBan": 4 },

  #HD057
  { "MaHD_input": "HD057", "MaSach_input": "S174", "SLBan": 2 },
  { "MaHD_input": "HD057", "MaSach_input": "S184", "SLBan": 5 },

  #HD058
  { "MaHD_input": "HD058", "MaSach_input": "S194", "SLBan": 10 },
  { "MaHD_input": "HD058", "MaSach_input": "S018", "SLBan": 1 },

  #HD059
  { "MaHD_input": "HD059", "MaSach_input": "S028", "SLBan": 3 },
  { "MaHD_input": "HD059", "MaSach_input": "S038", "SLBan": 6 },
  { "MaHD_input": "HD059", "MaSach_input": "S048", "SLBan": 2 },

  #HD060
  { "MaHD_input": "HD060", "MaSach_input": "S058", "SLBan": 7 },
  { "MaHD_input": "HD060", "MaSach_input": "S068", "SLBan": 3 },
  { "MaHD_input": "HD060", "MaSach_input": "S078", "SLBan": 1 },

  #HD061
  { "MaHD_input": "HD061", "MaSach_input": "S087", "SLBan": 5 },
  { "MaHD_input": "HD061", "MaSach_input": "S097", "SLBan": 4 },

  #HD062
  { "MaHD_input": "HD062", "MaSach_input": "S107", "SLBan": 9 },

  #HD063
  { "MaHD_input": "HD063", "MaSach_input": "S117", "SLBan": 2 },
  { "MaHD_input": "HD063", "MaSach_input": "S127", "SLBan": 6 },
  { "MaHD_input": "HD063", "MaSach_input": "S137", "SLBan": 1 },
  { "MaHD_input": "HD063", "MaSach_input": "S147", "SLBan": 3 },

  #HD064
  { "MaHD_input": "HD064", "MaSach_input": "S157", "SLBan": 8 },
  { "MaHD_input": "HD064", "MaSach_input": "S167", "SLBan": 2 },
  
  #HD065
  { "MaHD_input": "HD065", "MaSach_input": "S176", "SLBan": 5 },
  { "MaHD_input": "HD065", "MaSach_input": "S186", "SLBan": 4 },

  #HD066
  { "MaHD_input": "HD066", "MaSach_input": "S196", "SLBan": 11 },
  { "MaHD_input": "HD066", "MaSach_input": "S013", "SLBan": 2 },

  #HD067
  { "MaHD_input": "HD067", "MaSach_input": "S023", "SLBan": 6 },
  { "MaHD_input": "HD067", "MaSach_input": "S033", "SLBan": 3 },
  { "MaHD_input": "HD067", "MaSach_input": "S043", "SLBan": 1 },
  
  #HD068
  { "MaHD_input": "HD068", "MaSach_input": "S053", "SLBan": 7 },
  { "MaHD_input": "HD068", "MaSach_input": "S063", "SLBan": 4 },
  
  #HD069
  { "MaHD_input": "HD069", "MaSach_input": "S075", "SLBan": 9 },
  { "MaHD_input": "HD069", "MaSach_input": "S085", "SLBan": 2 },

  #HD070
  { "MaHD_input": "HD070", "MaSach_input": "S095", "SLBan": 5 },
  { "MaHD_input": "HD070", "MaSach_input": "S105", "SLBan": 3 },
  { "MaHD_input": "HD070", "MaSach_input": "S115", "SLBan": 1 },
  { "MaHD_input": "HD070", "MaSach_input": "S125", "SLBan": 6 },

  #HD071
  { "MaHD_input": "HD071", "MaSach_input": "S138", "SLBan": 8 },

  # #HD072
  { "MaHD_input": "HD072", "MaSach_input": "S148", "SLBan": 4 },
  { "MaHD_input": "HD072", "MaSach_input": "S158", "SLBan": 2 },
  
  # #HD073
  { "MaHD_input": "HD073", "MaSach_input": "S169", "SLBan": 7 },
  { "MaHD_input": "HD073", "MaSach_input": "S179", "SLBan": 3 },
  
  # #HD074
  { "MaHD_input": "HD074", "MaSach_input": "S189", "SLBan": 10 },
  { "MaHD_input": "HD074", "MaSach_input": "S199", "SLBan": 5 },

  # #HD075
  { "MaHD_input": "HD075", "MaSach_input": "S010", "SLBan": 2 },
  { "MaHD_input": "HD075", "MaSach_input": "S020", "SLBan": 4 },
  { "MaHD_input": "HD075", "MaSach_input": "S030", "SLBan": 1 },
  
  # #HD076
  { "MaHD_input": "HD076", "MaSach_input": "S001", "SLBan": 8 },
  { "MaHD_input": "HD076", "MaSach_input": "S049", "SLBan": 3 },
  
  # #HD077
  { "MaHD_input": "HD077", "MaSach_input": "S059", "SLBan": 6 },
  { "MaHD_input": "HD077", "MaSach_input": "S069", "SLBan": 2 },
  { "MaHD_input": "HD077", "MaSach_input": "S079", "SLBan": 5 },

  # #HD078
  { "MaHD_input": "HD078", "MaSach_input": "S089", "SLBan": 1 },
  { "MaHD_input": "HD078", "MaSach_input": "S098", "SLBan": 4 },
  
  # #HD079
  { "MaHD_input": "HD079", "MaSach_input": "S108", "SLBan": 9 },
  
  # #HD080
  { "MaHD_input": "HD080", "MaSach_input": "S118", "SLBan": 3 },
  { "MaHD_input": "HD080", "MaSach_input": "S128", "SLBan": 5 },
  { "MaHD_input": "HD080", "MaSach_input": "S138", "SLBan": 2 },
  { "MaHD_input": "HD080", "MaSach_input": "S149", "SLBan": 1 },
  { "MaHD_input": "HD080", "MaSach_input": "S159", "SLBan": 4 }
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