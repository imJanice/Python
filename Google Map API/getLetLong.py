def getLatLong(address):
	lat_lng="NULL"
	
	#API
	fileRoad = "C:/JaniceData/CODE/Python/WKE/DataProcessing/Google_map_GetLatitude&Longitude/GoogleMap_API_Key.txt"
	f = open(fileRoad,'r',encoding='UTF-8')
	API_key = f.read()
	#print(API_key)
	
	kw = '南投縣'
	
	if kw in address:
		url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='+API_key 
		#print(url)
		try:
			response = request('get', url)
			html = json.loads(response.text)
			json_data = json.dumps(html,sort_keys = True ,indent = 4)
			#print(json_data)
			lat = html['results'][0]['geometry']['location']['lat']
			lng = html['results'][0]['geometry']['location']['lng']
			#print(html['results'][0]['geometry']['location'])
			#print("lat:",lat)
			#print("lng:",lng)
			lat_lng = str(lat)+','+str(lng)
		
		except Exception as e:
			print("%s failed"%(address))
			print(e)
			lat_lng="NULL"

		
	#print("%s lat_lng %s"%(address,lat_lng))
	return lat_lng
	
	
res = getLatLong('南投縣埔里鎮民治二街16號')