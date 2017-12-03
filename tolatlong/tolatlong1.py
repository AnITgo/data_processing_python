#coding:utf-8
from urllib.request import urlopen, quote
import requests
import json

def getlnglat(address):
	#url = 'http://api.map.baidu.com/geocoder/v2/'
	url = 'https://maps.googleapis.com/maps/api/geocode/json'
	output = 'json'
	#ak = 'cne4Y0vDmuavTuipGLtVhTC5bKmt98Cr'
	ak = 'AIzaSyCCv8wMmLGYvx5MKc4ynJRSvnTW2FRbsHI'
	add = quote(address)
	#uri = url + '?' + 'address=' + add  + '&output=' + output + '&ak=' + ak
	uri = url + '?' + 'address=' + add  + '&ak=' + ak
	req = urlopen(uri)
	res = req.read().decode()
	temp = json.loads(res)
	#print(temp['results'][0]['geometry']['location']['lat'])
	status = temp['status']
	print(status)
	if status=='OK':
		lat = temp['results'][0]['geometry']['location']['lat']
		lng = temp['results'][0]['geometry']['location']['lng']

	else:	
		lat = "null"
		lng = "null"
	return lat,lng
def __jsonDump(name,_json):
	with open(name + '.json','a') as outfile:
		json.dump(_json,outfile,ensure_ascii=False)
	with open(name + '.json','a') as outfile:
		outfile.write(',\n')
if __name__ == '__main__':
	#file = open("location_name.json",encoding='utf-8')
	data=[]
	newData=[]
	with open('location_name2.json', 'rb') as f:
		file = json.load(f)
	data = [x for x in file]

	# for line in file:
	# 	data.append(json.loads(line[1]))
	
	for dic in data:
		address = dic['LOCATION']
		print(address)
		lat,lng = getlnglat(address)
		dic['latitude'] = lat
		dic['longitude'] = lng
		newData.append(dic)
		print(dic)
	for dic in newData:
		__jsonDump("new222",dic)