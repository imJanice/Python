#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=25.0540279,121.5199219&radius=500&types=food&key= server api key

import googlemaps 
import json
import sys
sys.path.append('C:\\JaniceData\\CODE\\Python\\my_models')
import GoogleMapApi
import SQL

#、night_club
#done:convenience_store、grocery_or_supermarket'、laundry、movie_theater、department_store、store

def NearbySearch(lat,lon):
	api_key = GoogleMapApi.api_key()
	client = googlemaps.Client(key=api_key)
	result = client.places_nearby(
        location={'lat': lat, 'lng': lon}, 
        radius=500,
        type='night_club',   
		language='zh-TW')	
	return result
	

def insert(lat,lng,name,address,link):

	db = 'iDriver'
	(cnxn,cursor)=SQL.connect(db)
	sql = '''
	declare @time datetime2(0)
	set @time = SYSDATETIME()
	declare @oid int
	select @oid=max(OID)+1 from Object
	if not exists(select * from Object where Lat = %s and Lon = %s and Type = 101)
	begin
		
		DECLARE @chk tinyint
		SET @chk = 0
		Begin Transaction
		
			insert into Object (OID,BID,Type,Lat,Lon,Since)
			values (@oid,dbo.fn_GetBlockNum(%s,%s),102,%s,%s,@time)
			IF @@Error <> 0 BEGIN SET @chk = 1 END
			insert into Market (MID,Name,Address,Link,Since)
			values (@oid,'%s','%s','%s',GETDATE())
			IF @@Error <> 0 BEGIN SET @chk = 1 END
			
		
		IF @chk <> 0 BEGIN 
		Rollback Transaction  
		END
		ELSE BEGIN
			Commit Transaction 
		END
	end
	'''%(lat,lng,lat,lng,lat,lng,name,address,link)
	
	try:
		res = cursor.execute(sql).rowcount
		if res == 1:
			print('success:',name,lat,lng)
		else:
			print('exists:',name)
		cnxn.commit() 
	except:
		
		print('error:',lat,lng,name)
		print(sql)
	
	cnxn.close()
	
	
	
def init():
	
	
	market = []
	
	db = 'iDriver'
	(cnxn,cursor)=SQL.connect(db)
	sql = '''
	select OID,Lat,Lon from Object
	where Type = 100
	'''
	cursor.execute(sql)
	result = cursor.fetchall()
	cnxn.commit() 
	list = ['oid','lat','lng']
	house = SQL.rowToDict(list,result)
	cnxn.close()
	
	for h in house:
		print('oid:',house[h]['oid'])
		res = NearbySearch(house[h]['lat'],house[h]['lng'])
		for data in res['results']:
			lat = data['geometry']['location']['lat']
			lng = data['geometry']['location']['lng']
			latlon = str(lat)+','+str(lng)
			name = data['name']
			if latlon not in market:
				market.append(latlon)
				address = data['vicinity']
				link = 'https://www.google.com.tw/maps/search/'+name
				print(data['geometry']['location']['lat'])
				print(data['geometry']['location']['lng'])
				print(data['name'])
				print(data['vicinity'])
				insert(lat,lng,name,address,link)
	print(len(market))
	print(market)
		
init()

#oid: 67328

#print(NearbySearch(23.964409,120.961528))
