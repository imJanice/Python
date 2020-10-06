#取得距離租屋最近的校車站牌
#順便修改字串None to NULL

import requests
import json

import sys
sys.path.append('C:\\JaniceData\\CODE\\Python\\my_models')
import mssql
import function

db = 'HouseDB'
(cnxn,cursor)=mssql.connect(db)


(bus_destination,house_origin,busStop,HID)=function.initData(cnxn,cursor)

table = 'House'

for i in range(len(house_origin)):
	if house_origin[i] == 'None' or house_origin[i] is None:
		#修改字串None to NULL
		
		key = 'LetLong'
		where = 'HID'
		value = 'NULL'
		hid = HID[i]
		#mssql.update_null_by_int(table,key,where,hid,cnxn,cursor)
		print(hid," : ",value)
	else:
		result_json = function.DistanceMatrixService(house_origin[i],bus_destination)
		time = function.nearBusStop(result_json,busStop)
		key = 'sBus'
		value = time
		where = 'LetLong'
		id = house_origin[i]
		print(id," : ",value)
		mssql.update_string_by_string(table,key,value,where,id,cnxn,cursor)
	

'''
for i in result_json['rows'][0]['elements']:
	print(i['distance']) 
'''
#距離房子最近的校車車站






	
#print(bus_destination)

#print(house_origin)
	
	


