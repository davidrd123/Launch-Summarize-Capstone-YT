Certainly, here's a more detailed structured version:

# Capstone Project Transcript Analysis

This repository allows you to extract and analyze transcripts from previous Capstone Projects through various methodologies. The extensive process involves fetching video transcripts, transcript processing, topic modeling, and interactive presentation of results.

## Setup

1. **Environment Activation**

Activate your .venv or Conda environment:

```bash
pip install -r requirements.txt
```

2. **API Keys**

Have a `.env` file prepared with the following keys:
  - `YT_DATA_API_KEY`: For access to YouTube Data API
  - `OPENAI_API_KEY`: For accessing OpenAI API

## Usage

### 1. Video Transcript Extraction

The script `get_transcript.py` is used to fetch transcripts from YouTube videos. Run the following command and provide the specific video URL when prompted:

```bash
python get_transcript.py
```

The fetched transcript will be saved under a directory structure `<year>/<project_name>`. The year is derived from the playlist name and project name from the video title.

### 2. GPT-Based Transcript Processing 

Use the `process_transcript_gpt.py` script to process the transcripts. It facilitates an interactive CLI menu. 

```bash
python process_transcript_gpt.py
```

This allows you to select options like:
- "Rewrite Transcript in Shorter Form"
- "Get token count of Transcript"
- "Summarize Rewrite in Outline Form"
- "Summarize Transcript in Outline Form"
- "Get token count of Rewrite"

Follow the instructions provided in the CLI.

### 3. Topic Modeling of Transcripts

For topic modeling, use `topic_modeling.py`.

```bash
python topic_modeling.py
```

This applies the LDA (Latent Dirichlet Allocation) approach, proposing topics for the documents. The output includes details about topics, their corresponding terms, and project-to-topic allocations.

### 4. Summaries Visualization with Streamlit

Employ `view_writeups.py` to launch a Streamlit app for accessible and interactive summary visualization.

```bash
streamlit run view_writeups.py
```

**Note:** Each mentioned step contributes to the analysis of the Capstone Project transcripts, providing crucial insights derived from their YouTube video transcripts.

Leap into transcript analysis and uncover the kernels of knowledge from previous Capstone Projects!