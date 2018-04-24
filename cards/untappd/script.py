#!/usr/bin/python3

import json
from datetime import datetime
from urllib.parse import urljoin
from urllib.request import urlopen, Request

def load_page(url):
    q = Request(url)
    q.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Firefox')
    q.add_header('Accept', 'text/html,application/xhtml+xml,applicationxml;q=0.9,*/*;q=0.8')
    q.add_header('Accept-Encoding', 'none')
    q.add_header('Accept-Language', 'en-IE,en,en-US')
    q.add_header('Connection', 'keep-alive')
    return urlopen(q).read()

if __name__ == '__main__':
    d = None
    with open('config.hidden.json', 'r') as f:
        d = json.load(f)
    url = 'https://api.untappd.com/v4/user/info/iandioch?client_id={}&client_secret={}'
    url = url.format(d['client_id'], d['client_secret'])
    data = json.loads(load_page(url))
    out = {}
    out['user'] = data['response']['user'].copy()
    del out['user']['recent_brews']
    out['latest'] = data['response']['user']['recent_brews']['items'][0]
    json_data = json.dumps(out, indent=4)
    with open('/home/noah/prog/ceres/cards/untappd/data.json', 'w') as filewriter:
        filewriter.write(json_data)
        filewriter.write("\n")
