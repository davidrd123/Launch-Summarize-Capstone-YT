import os
import sys
import json
import base64
from pathlib import Path
import requests
import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
import googleapiclient.discovery
import inquirer

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


YT_DATA_API_BASE_URL = 'https://www.googleapis.com/youtube/v3'
YT_PLAYLIST_ITEMS_URL = f'{YT_DATA_API_BASE_URL}/playlistItems'

# Retrieve and decode the base64-encoded credentials from the environment
google_credentials_base64 = os.environ["GOOGLE_CREDENTIALS_BASE64"]
google_credentials_info = json.loads(base64.b64decode(google_credentials_base64))

# Build credentials from the service account info
credentials = google.oauth2.service_account.Credentials.from_service_account_info(google_credentials_info, scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])


# Set up the YouTube Data API client
youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

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
	print(f'Getting transcript for video_id: {video_id}')
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

	# Video title is going to start with 'Launch School Capstone Presentation: <Project Name>'
	# We want to remove the 'Launch School Capstone Presentation: ' part
	project_name = video_info_to_project_name(get_video_info(video_id))

	subfolder_path = transcripts_path / capstone_year / project_name
	subfolder_path.mkdir(parents=True, exist_ok=True)
	
	
	if not transcript:
		success, transcript = get_transcript(video_id)
		if not success:
			return False
	file_path = subfolder_path / f'{video_id}_transcript.txt'
	if file_path.exists():
		print(f'File already exists at {file_path} for video_id: {video_id}. Skipping...')
		return False
	with file_path.open('w', encoding='utf-8') as f:
		print(f'Writing transcript to {file_path}')
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

def video_info_to_project_name(video_info):
	title = video_info['items'][0]['snippet']['title']
	video_title = title.split(': ')[1]
	return video_title

def video_info_to_title(video_info):
	title = video_info['items'][0]['snippet']['title']
	# Remove invalid characters (e.g. /, \, :, etc.)
	title = ''.join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
	# Replace spaces with underscores
	title = title.replace(' ', '_')
	return title

def select_video_or_playlist():
	options = [
		'Video',
		'Playlist'
	]

	questions = [
		inquirer.List('video_or_playlist',
			message='Select video or playlist',
			choices=options,
		),
	]

	answers = inquirer.prompt(questions)
	return answers['video_or_playlist']

def download_transcript(video_id, playlist_id):
	success, transcript = get_transcript(video_id)
	if success:
		save_transcript(video_id, playlist_id, transcript)
	else:
		exit(transcript)

def playlist_id_to_video_ids(playlist_id):
	params = {
		'key': YT_DATA_API_KEY,
		'part': 'snippet',
		'playlistId': playlist_id,
		'maxResults': 50
	}
	response = requests.get(YT_PLAYLIST_ITEMS_URL, params=params)
	playlist_items = response.json()
	video_ids = []
	for item in playlist_items['items']:
		video_ids.append(item['snippet']['resourceId']['videoId'])
	return video_ids

def app():
	answer = select_video_or_playlist()
	if answer == 'Video':
		video_url = input('Enter video url: ')
		video_id = video_url_to_id(video_url)
		playlist_id = video_url_to_playlist_id(video_url) # returns None if no playlist ID found, needs to be handled
		video_playlist = get_video_playlist(playlist_id)

		print(f'video_playlist: {video_playlist}')
		print(f'Capstone year: {video_playlist_to_presentation_year(video_playlist)}')
		download_transcript(video_id, playlist_id)
	elif answer == 'Playlist':
		# print(f'Capstone year: {video_playlist_to_presentation_year(video_playlist)}')
		playlist_url = input('Enter playlist URL: ')
		playlist_id = video_url_to_playlist_id(playlist_url)
		video_ids = playlist_id_to_video_ids(playlist_id)
		print(f'video_ids: {video_ids}')
		for video_id in video_ids:
			download_transcript(video_id, playlist_id)
	else:
		print('Invalid option selected. Exiting...')
		exit()

	


if __name__ == '__main__':
	app()
