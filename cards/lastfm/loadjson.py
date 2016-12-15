#!/usr/bin/python3

import json, urllib.request, os.path

def get_json_web(url):
	try:
		bytedata= urllib.request.urlopen(url).read()
		return json.loads(str(bytedata))
	except Exception as e:
		print(e)
		return None

def get_json_file(path):
	if os.path.isfile('data.json'):
		with open('data.json', 'r') as data:
			try:
				return json.load(data)
			except Exception as e:
				print(e)
				return None
	else:
		return None


if __name__ == '__main__':
	print(get_json_web('http://noah.needs.money'))
	print(get_json_file('data.json'))

