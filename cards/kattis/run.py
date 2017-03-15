#!/usr/bin/python3

import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_cloc_data():
	data = {}
	with open('/tmp/cloc.csv', 'r') as filereader:
		csv = filereader.read()
		print(csv)
		curr_lang = 0
		total_files = 0
		langs = {}
		for lang in csv.split('\n')[1:]:
			parts = lang.split(',')
			if len(parts) == 1:
				break
			print(parts)
			langs[parts[1]] = int(parts[0])

		for lang in sorted(langs, key=lambda x:langs[x], reverse=True):
			data['lang%d' % curr_lang] = lang
			num_files = langs[lang]
			data['num_lang%d' % curr_lang] = num_files
			total_files += num_files
			curr_lang += 1
		data['num_solutions'] = total_files
	return data


def number_to_position(n):
	s = str(n)
	if s[-1] == '1' and (len(s) == 1 or s[-2] != '1'):
		s += 'st'
	elif (len(s) == 1 or s[-2] != '1') and s[-1] == '2':
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
	cloc_data = get_cloc_data()
	for k in cloc_data:
		data[k] = cloc_data[k]
	json_data = json.dumps(data, indent=4)
	with open('/home/waterloo/ceres/cards/kattis/data.json', 'w') as filewriter:
		filewriter.write(json_data)
		filewriter.write("\n")
	print(json_data)
