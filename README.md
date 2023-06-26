# Launch School Capstone Project Transcript Analysis

This repository provides tools and methodologies to extract and analyze transcripts from Launch School Capstone Projects. The project consists of a four-step pipeline - fetching video transcripts, processing transcripts, modeling topic data, and delivering an interactive presentation of the results.

Experience the process live and interact with results at [Capstone Summary Web App](https://launch-summarize-capstone-yt.streamlit.app/).

## Setup & Requirements

1. **Virtual Environment Activation**

Before running any scripts, activate your virtual environment (.venv) or Conda environment:

```bash
pip install -r requirements.txt
```

2. **API Credentials**

Required API keys for YouTube Data and OpenAI should reside in your `.env` file as `YT_DATA_API_KEY` and `OPENAI_API_KEY` respectively.

## Step-by-Step Usage

### 1. Fetching Video Transcripts

Running `get_transcript.py` fetches transcripts from YouTube videos. Input the specific video URL when the script prompts:

```bash
python get_transcript.py
```

Each fetched transcript is stored in a directory named after the project and categorized under corresponding `<year>/<project_name>` directories.

### 2. Transcript Processing with GPT Models 

`process_transcript_gpt.py` offers control over transcript processing using GPT models. The script produces an interactive CLI menu allowing you to select a project and a GPT model - either 'gpt-4' or 'gpt-3.5-turbo-16k' - for processing.

```bash
python process_transcript_gpt.py
```

Options available within the processing menu include:

- **"Rewrite Transcript in Shorter Form"**: It condenses the transcript retaining key points. If a rewritten form doesn't exist, this operation should be performed first.

- **"Summarize Rewrite in Outline Form"**: Provides an outline summary for the rewritten transcript.

- **"Summarize Transcript in Outline Form"**: Facilitates an outline summary for raw transcripts. Note: This option requires the use of 'gpt-3.5-turbo-16k' for transcripts exceeding 8k tokens.

- **"Get token count of Transcript"** and **"Get token count of Rewrite"**: Both options return the token count for respective transcripts.

### 3. Topic Modeling on Transcripts

LDA (Latent Dirichlet Allocation) implemented in the `topic_modeling.py` script surfaces dominant topics from the transcripts.

```bash
python topic_modeling.py
```

It uses either raw transcripts or a rewritten form (depends on uncommented lines in the script) and proposes a set of topics for each document. Options for calculating coherence and executing a grid search for parameter optimization are available. Uncomment `# pyLDAvis.save_html(lda_viz, 'lda.html')` to output an easy-to-understand interactive HTML visualization.

The results also cluster projects by the identified primary topic and measure the level of association. It allows for a comparison and understanding of the broad topics covered per project.

### 4. Interactive Summary Visualization with Streamlit

The final step encompasses an accessible and interactive summary visualization, available via a Streamlit app. To launch the app, run:

```bash
streamlit run view_writeups.py
```

Now you can embark on analyzing previous Capstone Projects transcripts and discover valuable insights!
