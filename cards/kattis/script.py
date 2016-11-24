#!/usr/bin/python3

import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def number_to_position(n):
	s = str(n)
	if s[-1] == '1':
		s += 'st'
	elif s[-1] == '2':
		s += 'nd'
	elif s[-1] == '3':
		s += 'rd'
	else:
		s += 'th'
	return s

def load_page(url):
	q = Request(url)
	q.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Firefox')
	q.add_header('Accept', 'text/html,application/xhtml+xml,applicationxml;q=0.9,*/*;q=0.8')
	q.add_header('Accept-Encoding', 'none')
	q.add_header('Accept-Language', 'en-IE,en,en-US')
	q.add_header('Connection', 'keep-alive')
	return urlopen(q).read()

def get_user_data(page):
	soup = BeautifulSoup(page, 'html.parser')
	data = {}
	table = soup.find('table')
	rows = table.find_all('tr')
	data['global_rank'] = number_to_position(int(rows[1].find_all('td')[0].string))
	data['score'] = (rows[1].find_all('td')[1].string)
	return data

def get_rank_data(page):
	soup = BeautifulSoup(page, 'html.parser')
	pos = 1337
	data = {}
	table = soup.find_all('table')[2]
	rows = table.find_all('tr')
	for row in rows[1:]:
		parts = row.find_all('td')
		link = parts[1].find('a')
		if link['href'] == '/users/iandioch':
			pos = int(parts[0].string)
			break
	return number_to_position(pos)


if __name__ == '__main__':
	page = load_page('https://open.kattis.com/users/iandioch')
	data = get_user_data(page)
	data['irish_rank'] = get_rank_data(load_page('https://open.kattis.com/countries/IRL'))
	json_data = json.dumps(data, indent=4)
	with open('/home/waterloo/ceres/cards/kattis/data.json', 'w') as filewriter:
		filewriter.write(json_data)
		filewriter.write("\n")
	print(json_data)
