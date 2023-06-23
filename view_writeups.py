import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)

import json
import streamlit as st

ROOT_DIR = os.getcwd()

# print(f'ROOT_DIR: {ROOT_DIR}');
# print(f'os.listdir(ROOT_DIR): {os.listdir(ROOT_DIR)}');

with open('team_to_topic.json', 'r') as f:
    team_to_topic = json.load(f)


transcripts_path = Path(ROOT_DIR) / 'transcripts'
if not transcripts_path.exists():
    print(f'E: Transcripts directory not found!')
    st.error("Error: Transcripts directory not found!")
    st.stop()

years = os.listdir(transcripts_path)
years = sorted([year for year in years if year != '.DS_Store'])

selected_year = st.sidebar.selectbox('Select a year', years)

presentations = os.listdir(Path(ROOT_DIR) / 'transcripts' / selected_year)
presentations = sorted([presentation for presentation in presentations if presentation != '.DS_Store'])

selected_presentation = st.sidebar.selectbox('Select a presentation', presentations)

files = os.listdir(Path(ROOT_DIR) / 'transcripts' / selected_year / selected_presentation)

# Find transcript file
transcript_file = [file for file in files if file.endswith('_transcript.txt')][0]

# Extract the video ID and create the YouTube URL
video_id = transcript_file.split('_transcript.txt')[0]
youtube_url = f"https://www.youtube.com/watch?v={video_id}"

# Filter to only 'summary_rewrite_*', 'rewrite_gpt-*', and 'summary_*' files
files = [file for file in files if file.startswith('summary_rewrite_') or file.startswith('rewrite_gpt-') or file.startswith('summary_')]

# Sort 'summary_rewrite_gpt-4*' first, then 'summary_rewrite_gpt-3.5*', then 'rewrite_gpt-*', then 'summary_*'
files = sorted(files, key=lambda file: (file.startswith('summary_rewrite_gpt-4'), file.startswith('summary_rewrite_gpt-3.5'), file.startswith('summary_'), file.startswith('rewrite_gpt-')), reverse=True)



st.video(youtube_url)


selected_file = st.sidebar.selectbox('Select a file', files)

file_path = Path(ROOT_DIR) / 'transcripts' / selected_year / selected_presentation / selected_file

if not file_path.is_file():
    file_content = f"Error: File not found: {selected_file}"
    st.error(f'Error: File not found: {selected_file}')
    print(file_content)
else:
    with open(file_path) as f:
        file_content = f.read()

title = f'[[{team_to_topic[selected_presentation]}]]'
st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)
st.markdown("[See LDA Visualization](https://davidrd123.github.io/Launch-Summarize-Capstone-YT/index.html)")
st.markdown("[Semantic Search over the Videos](https://launch-semantic-search-capstone-yt.vercel.app/)")
# st.title(f'{selected_presentation} - [[{team_to_topic[selected_presentation]}]]')
st.markdown(file_content)

# import streamlit.components.v1 as components

# with open("lda.html", 'r') as f:
#     html_string = f.read()
#     print(html_string[:100])

# components.html(html_string, height=600)