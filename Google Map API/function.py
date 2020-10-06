import googlemaps 
import json

import sys
sys.path.append('C:\\JaniceData\\CODE\\Python\\my_models')
import GoogleMapApi

def initData(cnxn,cursor):
	sql_commend_bus = '''
	select Let,Long
	from BusStop
	'''

	cursor.execute(sql_commend_bus)
	result = cursor.fetchall()
	cnxn.commit() 

	busLetLong = []
	for item in result:
		if item[0] is not None:
			busLetLong.append(str(item[0])+','+str(item[1]))
			
			
	sql_commend_house = '''
	select LetLong
	from House
	'''

	cursor.execute(sql_commend_house)
	result = cursor.fetchall()
	cnxn.commit() 

	houseLetLong = []
			
	for item in result:
		houseLetLong.append(item[0])
		
	sql_commend_stop = '''
	select BusStop
	from BusStop
	where Let is not NULL
	'''

	cursor.execute(sql_commend_stop)
	result = cursor.fetchall()
	cnxn.commit() 

	busStop = []
			
	for item in result:
		busStop.append(item[0])
		
	sql_commend_hid = '''
	select HID
	from House
	'''

	cursor.execute(sql_commend_hid)
	result = cursor.fetchall()
	cnxn.commit() 

	HID = []
			
	for item in result:
		HID.append(item[0])
		
	return busLetLong,houseLetLong,busStop,HID
	
def min(time,bus):
	t = time[0]
	b = bus[0]
	
	for i in range(len(time)):
		if time[i]<t:
			t=time[i]
			b=bus[i]
			
	return b
	

	
	
def nearBusStop(data,bus):
	time = []
	for i in data['rows'][0]['elements']:
		time.append(i['distance']['value'])
		
	short = min(time,bus)
	
	return short
		
	
	
def DistanceMatrixService(origins,dest):
	api_key = GoogleMapApi.api_key()
	client = googlemaps.Client(key=api_key)
	directions_result = client.distance_matrix(origins,dest,mode='walking',language='zh-TW')	
	return directions_result
	
	