import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.DEBUG)


import streamlit as st

ROOT_DIR = os.getcwd()

# print(f'ROOT_DIR: {ROOT_DIR}');
# print(f'os.listdir(ROOT_DIR): {os.listdir(ROOT_DIR)}');

st.title("SummarizeYT")

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

selected_file = st.sidebar.selectbox('Select a file', files)

file_path = Path(ROOT_DIR) / 'transcripts' / selected_year / selected_presentation / selected_file

if not file_path.is_file():
    file_content = f"Error: File not found: {selected_file}"
    st.error(f'Error: File not found: {selected_file}')
    print(file_content)
else:
    with open(file_path) as f:
        file_content = f.read()


st.markdown(file_content)


