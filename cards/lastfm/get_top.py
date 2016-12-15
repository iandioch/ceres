#!/usr/bin/python3

from loadjson import get_json_web, get_json_file
import json, datetime

NUM_ARTISTS = 3

if __name__ == '__main__':
	config_data = get_json_file('config.hidden.json')
	if config_data is None:
		print('Unable to load config_data')
	username = config_data['username']
	api_key = config_data['api_key']
	
	recent_track_url = 'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=%s&api_key=%s&format=json&limit=%d' % (username, api_key, NUM_ARTISTS)
	full_data = get_json_web(recent_track_url)
	if full_data is None:
		print('Unable to load artist data from API')
	new_output_data = {}
	all_artist_data = full_data['topartists']['artist']
	for i in range(3):
		artist_data = all_artist_data[i]	
		new_output_data['top_artist%d' % i] = \
			artist_data['name']
		new_output_data['top_artist%d_plays' % i] = \
			artist_data['playcount']
	print(new_output_data)
	output_data = get_json_file('data.json')
	if output_data is None:
		output_data = {}
	for key in new_output_data:
		output_data[key] = new_output_data[key]
	with open('data.json', 'w') as output_file:
		output_file.write(json.dumps(output_data,
			                     indent=4))
	
