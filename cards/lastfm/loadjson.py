#!/usr/bin/python3

import json, urllib.request, os.path

def get_json_web(url):
	try:
		bytedata= urllib.request.urlopen(url).read()
		strdata = bytes.decode(bytedata)
		return json.loads(strdata)
	except Exception as e:
		print(e)
		return None

def get_json_file(path):
	if os.path.isfile(path):
		with open(path, 'r') as data:
			try:
				return json.load(data)
			except Exception as e:
				print(e)
				return None
	else:
		print('No such file found')
		return None


if __name__ == '__main__':
	print(get_json_web('http://noah.needs.money'))
	print(get_json_file('data.json'))

