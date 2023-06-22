# Launch School Capstone Project Transcript Analysis

This repository allows you to extract and analyze transcripts from previous Launch School Capstone Projects through various methodologies. The processing pipeline involves fetching video transcripts, transcript processing, topic modeling, and interactive presentation of results.

You can find a Streamlit App to view and interact with the results at <https://summarize-capstone-yt.streamlit.app/>

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

The processing of transcripts using GPT models is controlled by `process_transcript_gpt.py`. When executed, this script prompts an interactive CLI menu for processing preferences.

```bash
python process_transcript_gpt.py
```

In the CLI’s menu, you can select the project you want to process by its `<year>` and `<project_name>`. Then, you’ll choose a suitable GPT model for processing. The available GPT models are `'gpt-4'` and `'gpt-3.5-turbo-16k'`. 

The processing options include:
- **"Rewrite Transcript in Shorter Form"**: Condenses the transcript while maintaining key points. This should be done before any other option if it's not already complete.
- **"Summarize Rewrite in Outline Form"**: Creates an outline for the rewritten transcript, which can be used with either `'gpt-4'` or `'gpt-3.5-turbo-16k'` models.
- **"Summarize Transcript in Outline Form"**: Provides a summary in outline form of the raw transcript. Typically, this option is only feasible with `'gpt-3.5-turbo-16k'` as raw transcripts of an hour-long video contain around 10k tokens, surpassing the `'gpt-4'` models limit of 8k tokens.
- **"Get token count of Transcript"**: Summarises the token number in the raw transcript.
- **"Get token count of Rewrite**": Gives the count of tokens in the rewritten transcript.

### 3. Topic Modeling of Transcripts

For an in-depth analysis to extract dominant topics from the transcripts, use the `topic_modeling.py` script to perform Latent Dirichlet Allocation (LDA).

```bash
python topic_modeling.py
```

The script takes the raw transcripts or rewrite (depending on the lines of code that are uncommented), and applies LDA to derive a set of proposed topics that most represent the content. There are sections included for calculating coherence and performing a grid search for refining hyperparameters and the number of topics. 

The produced output provides an insight into computed topics mapped with their correlated terms. For an easy visualisation, uncomment `# pyLDAvis.save_html(lda_viz, 'lda.html')` - this will generate an interactive HTML page.

Simultaneously, each project is annotated by identified topic labels showcasing the strength of its association with the topic. For example 'Project  Firefly  is about topic  5  with a contribution of  99.87 %'. This method reveals thematic connections among various projects and their underlying main topics.

### 4. Summaries Visualization with Streamlit

Employ `view_writeups.py` to launch a Streamlit app for accessible and interactive summary visualization.

```bash
streamlit run view_writeups.py
```

**Note:** Each mentioned step contributes to the analysis of the Capstone Project transcripts, providing crucial insights derived from their YouTube video transcripts.

Leap into transcript analysis and uncover the kernels of knowledge from previous Capstone Projects!