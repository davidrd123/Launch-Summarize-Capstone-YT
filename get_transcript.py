import os
import sys
from pathlib import Path
import requests
from googleapiclient.discovery import build
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

YT_DATA_API_KEY = os.getenv('YT_DATA_API_KEY')

yt_data_api_key = 'AIzaSyB3WFRMXvfeZH45R0neeHq3LOem0buIuxg'
yt_data_url = 'https://www.googleapis.com/youtube/v3/videos'
yt_playlists_url = 'https://www.googleapis.com/youtube/v3/playlists'

target_video_url = 'https://www.youtube.com/watch?v=I3sinNeqwZU'


def video_url_to_id(video_url):
	# Handle case of further parameters
	if '&' in video_url:
		video_id = video_url.split('v=')[1].split('&')[0]
	else:
		video_id = video_url.split('v=')[1]
	return video_id

def video_url_to_playlist_id(video_url):
	if 'list=' not in video_url:
		return None
	
	playlist_id = video_url.split('list=')[-1]
	if '&' in playlist_id:
		playlist_id = playlist_id.split('&')[0]
	return playlist_id

def get_transcript(video_id):
	try:
		transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
		
		full_text = ''
		for i in transcript:
			full_text += i['text'] + ' '
		return True, full_text
	except Exception as e:
		return False, f'\nUnable to get transcript for video_id: {video_id}\n{e}'

def save_transcript(video_id, playlist_id, transcript):
	video_title = video_info_to_title(get_video_info(video_id))
	capstone_year = video_playlist_to_presentation_year(get_video_playlist(playlist_id))
	transcripts_path = Path('transcripts')

	subfolder_path = transcripts_path / capstone_year / video_title
	subfolder_path.mkdir(parents=True, exist_ok=True)
	
	# Path(f'transcripts/{capstone_year}/{video_title}').mkdir(parents=True, exist_ok=True)

	if not transcript:
		success, transcript = get_transcript(video_id)
		if not success:
			return False
	file_path = subfolder_path / f'{video_id}_transcript.txt'
	with file_path.open('w', encoding='utf-8') as f:
		f.write(transcript)
	
	return True

def get_video_playlist(video_playlist_id):
	params = {
		'key': YT_DATA_API_KEY,
		'part': 'snippet',
		'id': video_playlist_id
	}
	response = requests.get(yt_playlists_url, params=params)
	return response.json()

def video_playlist_to_presentation_year(video_playlist):
	title = video_playlist['items'][0]['snippet']['title']
	# Find year at beginning of title
	year = title.split(' ')[0]
	return year
	

def get_video_info(video_id):
	params = {
		'key': YT_DATA_API_KEY,
		'part': 'snippet',
		'id': video_id
	}
	response = requests.get(yt_data_url, params=params)
	return response.json()

def video_info_to_title(video_info):
	title = video_info['items'][0]['snippet']['title']
	# Remove invalid characters (e.g. /, \, :, etc.)
	title = ''.join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
	# Replace spaces with underscores
	title = title.replace(' ', '_')
	return title


def app():
	video_url = input('Enter video url: ')
	if not video_url:
		video_url = target_video_url
		# video_url = input('Enter video url: ')
	# print(f'video_url: {video_url}')

	video_id = video_url_to_id(video_url)
	playlist_id = video_url_to_playlist_id(video_url) # returns None if no playlist ID found, needs to be handled
	video_playlist = get_video_playlist(playlist_id)

	# print(f'Capstone year: {video_playlist_to_presentation_year(video_playlist)}')
	

	success, transcript = get_transcript(video_id)
	print(video_id)  
	if success:
		print("Success!")
		save_transcript(video_id, playlist_id, transcript)		
	else:
		exit(transcript)

	video_info = get_video_info(video_id)
	print(video_info_to_title(video_info))


if __name__ == '__main__':
	app()
