#!/usr/bin/python3

from loadjson import get_json_web, get_json_file
import json, datetime

if __name__ == '__main__':
	config_data = get_json_file('config.hidden.json')
	if config_data is None:
		print('Unable to load config_data')
	username = config_data['username']
	api_key = config_data['api_key']
	
	recent_track_url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=%s&format=json&limit=1' % (username, api_key)
	full_data = get_json_web(recent_track_url)
	if full_data is None:
		print('Unable to load track data from API')
	# Must take index -1, as if there is a song currently
	# being scrobbled, it will be at position 0, and will
	# not have a date parameter.
	track_data = full_data['recenttracks']['track'][-1]
	track_name = track_data['name']
	track_artist = track_data['artist']['#text']
	track_date_uts = int(track_data['date']['uts'])
	track_date_str = datetime.datetime.fromtimestamp(
			track_date_uts,
	).strftime('%H:%M on %d/%m/%Y')
	print(track_name)
	print(track_artist)
	print(track_date_str)
	output_data = get_json_file('data.json')
	if output_data is None:
		output_data = {}
	output_data['last_song_title'] = track_name
	output_data['last_song_artist'] = track_artist
	output_data['last_song_date'] = track_date_str
	with open('data.json', 'w') as output_file:
		output_file.write(json.dumps(output_data,
			                     indent=4))
	
