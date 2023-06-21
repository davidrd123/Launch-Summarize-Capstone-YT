import os
import nltk
from nltk.tokenize import sent_tokenize, TextTilingTokenizer
from sentence_transformers import SentenceTransformer
import scipy.cluster.hierarchy as hcluster
import spacy
import pickle
from pathlib import Path
import inquirer

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers import BertTokenizer, BertForMaskedLM
import torch

os.environ['NLTK_DATA'] = '/Users/daviddickinson/nltk_data'

def clean_transcript(transcript):
	# remove 'uh' and 'um' from transcript
	cleaned_transcript = transcript.replace('uh', '').replace('um', '')
	return cleaned_transcript


def process_transcript_nltk(transcript):
	# sentences = sent_tokenize(transcript)
	# return sentences
	tt = TextTilingTokenizer()
	sentences = tt.tokenize(transcript)
	return sentences

def process_transcript_spacy(transcript):
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(transcript)
	sentences = [sent.text for sent in doc.sents]
	return sentences

def process_transcript_bert_huggingface(transcript):
	
	# model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
	# tokenizer = AutoTokenizer.from_pretrained(model_name)
	# model = AutoModelForSequenceClassification.from_pretrained(model_name)

	# nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
	# result = nlp(transcript)
	# return result
	tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
	model = BertForMaskedLM.from_pretrained('bert-base-uncased')
	model.eval()

	words = transcript.split()
	punctuated_transcript = []
	# Break the transcript into chunks of max_length tokens
	max_length = 512
	chunks = [words[i:i + max_length] for i in range(0, len(words), max_length)]
	for chunk in chunks:
		for i in range(len(chunk)):
			masked_transcript = chunk[:i] + ["[MASK]"] + chunk[i+1:]
			input_ids = tokenizer.encode(" ".join(masked_transcript), return_tensors='pt')
			with torch.no_grad():
				outputs = model(input_ids)
			predictions = outputs[0]
			predicted_index = torch.argmax(predictions[0, i+1]).item()
			predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
			punctuated_transcript.append(chunk[i])
			if predicted_token in [".", ",", "?", "!"]:
				punctuated_transcript.append(predicted_token)

	punctuated_transcript = " ".join(punctuated_transcript)
	return punctuated_transcript


def select_directory(subdirs):
	# # Print out a menu with all the subdirectories
	# for i, subdir in enumerate(subdirs, start=1):
	#     print(f"{i}. {subdir.name}")

	# # Ask the user to select a directory
	# choice = int(input("Select a directory: ")) - 1
	# selected_dir = subdirs[choice]

	# Create a list of subdir names
	subdir_names = [subdir.name for subdir in subdirs]

	# Create a list prompt
	questions = [
			inquirer.List('chosen_dir',
										message="Select a directory",
										choices=subdir_names,
										)
	]

	# Get the user's answer
	answers = inquirer.prompt(questions)

	# Find the selected subdir
	selected_dir = next(subdir for subdir in subdirs if subdir.name == answers['chosen_dir'])
	return selected_dir

def select_segmenter():
	# Create a list prompt
	questions = [
		inquirer.List('chosen_segmenter',
						message="Select a segmenter",
						choices=['nltk', 'spacy', 'bert'],
						)
	]

	# Get the user's answer
	answers = inquirer.prompt(questions)

	# Find the selected subdir
	selected_segmenter = answers['chosen_segmenter']
	return selected_segmenter

def app():
	transcripts_path = Path('transcripts')

	# Get a list of all subdirectories in the transcripts folder
	subdirs = [d for d in transcripts_path.iterdir() if d.is_dir()]

	# Ask the user to select a directory
	selected_dir = select_directory(subdirs)

	# Ask the user to select a segmenter (e.g. nltk, spacy, etc.
	selected_segmenter = select_segmenter()

	# Should only be one transcript ending in _transcript.txt
	transcript_path = [f for f in selected_dir.iterdir() if f.name.endswith('_transcript.txt')][0]

	# Read the transcript
	with transcript_path.open('r', encoding='utf-8') as f:
		transcript = f.read()

	# Clean the transcript
	cleaned_transcript = clean_transcript(transcript)

	# Process the transcript
	if selected_segmenter == 'nltk':
		sentences = process_transcript_nltk(cleaned_transcript)
	elif selected_segmenter == 'spacy':
		sentences = process_transcript_spacy(cleaned_transcript)
	elif selected_segmenter == 'bert':
		sentences = process_transcript_bert_huggingface(cleaned_transcript)
	else:
		raise ValueError(f"Invalid segmenter: {selected_segmenter}")
	
	print(sentences)




if __name__ == '__main__':
		nltk.download('punkt')  # Ensure the Punkt tokenizer is downloaded
		app()