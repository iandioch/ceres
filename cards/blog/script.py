#!/usr/bin/python3

import json
from datetime import datetime
from urllib.parse import urljoin
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

def day_of_month_to_str(s):
    s = str(int(s)) # remove zero padding
    if s == '1' or s == '21' or s == '31':
        return s + 'st'
    if s == '2' or s == '22':
        return s + 'nd'
    if s == '3' or s == '23':
        return s + 'rd'
    return s + 'th'

def date_str_to_str(d):
    e = datetime.strptime(d, '%Y-%m-%d')
    day = day_of_month_to_str(e.strftime('%d'))
    return e.strftime('%A ') + day + e.strftime(' %B %Y')

def get_data(page, root_url):
    soup = BeautifulSoup(page, 'html.parser')
    d = []
    for article in soup.find_all('article'):
        date = article.find('time').get('datetime')
        title = article.find('header').find('h1').string
        art_url = urljoin(root_url, article.find('a').get('href'))
        intro = article.find(class_=['text']).find('p').string
        d.append({
            'title': title,
            'date': date_str_to_str(date),
            'url': art_url,
            'intro': intro,
        })
        if len(d) == 5:
            break
    return d

if __name__ == '__main__':
    URL = 'http://mycode.doesnot.run'
    page = load_page(URL)
    data = get_data(page, URL)
    json_data = json.dumps(data, indent=4)
    with open('/home/noah/prog/ceres/cards/blog/data.json', 'w') as filewriter:
        filewriter.write(json_data)
        filewriter.write("\n")
    print(json_data)
