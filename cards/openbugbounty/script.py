#!/usr/bin/python3

import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def load_page(url):
	q = Request(url)
	q.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Firefox')
	q.add_header('Accept', 'text/html,application/xhtml+xml,applicationxml;q=0.9,*/*;q=0.8')
	q.add_header('Accept-Encoding', 'none')
	q.add_header('Accept-Language', 'en-IE,en,en-US')
	q.add_header('Connection', 'keep-alive')
	return urlopen(q).read()

def get_data(page):
	soup = BeautifulSoup(page, 'html.parser')
	info = soup.find(class_=["reporter-info", "reporter-profile"])
	data = {}
	rows = info.find_all('tr')
	
	data['num_vulns'] = int(rows[0].find_all('td')[1].string)
	data['num_vip'] = int(rows[1].find_all('td')[1].string)
	data['num_top_vip_of_week'] = len(rows[4].find_all(src="/images/stars/bronze-vip.png"))
	return data

if __name__ == '__main__':
	page = load_page('https://www.openbugbounty.org/researchers/iandioch/')
	data = get_data(page)
	json_data = json.dumps(data, indent=4)
	with open('/home/waterloo/ceres/cards/openbugbounty/data.json', 'w') as filewriter:
		filewriter.write(json_data)
		filewriter.write("\n")
	print(json_data)
