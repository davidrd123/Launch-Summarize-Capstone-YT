import os
from pathlib import Path
from gensim import corpora, models
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

nltk.download('stopwords')
nltk.download('wordnet')

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


list_of_transcripts = {}

transcripts_path = Path('transcripts')
# Iterate through each year
years = [year for year in os.listdir(transcripts_path) if year != '.DS_Store']
for year in years:
	# Get all directory names in the year directory not including .DS_Store
	project_names = [project for project in os.listdir(transcripts_path / year) if project != '.DS_Store']

	for project in project_names:
		# transcript is in the file matching '<video_id>_transcript.txt', regex match to filter the files down to it
		# transcript = [transcripts_path / year / project / file for file in os.listdir(transcripts_path / year / project) if file.endswith('_transcript.txt')][0]
		transcript = [transcripts_path / year / project / file for file in os.listdir(transcripts_path / year / project) if file.startswith('rewrite_gpt-3.5')][0]        
		with open(transcript) as f:
			list_of_transcripts[project] = f.read()
		
# list_of_transcripts is your list of all transcript strings
# texts = [clean(doc).split() for doc in list_of_transcripts]
texts = {project: clean(transcript).split() for project, transcript in list_of_transcripts.items()}

# Create a dictionary representation of the documents.
dictionary = corpora.Dictionary(texts.values())

# Convert document (a list of words) into the bag-of-words format = list of (token_id, token_count) tuples.
corpus_bow = [dictionary.doc2bow(text) for text in texts.values()]

# Train the LDA model
lda_model = models.LdaModel(corpus_bow, num_topics=10, id2word=dictionary, passes=15)

# Print the topics
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)

corpus_topics = [sorted(topics, key=lambda record: -record[1])[0] 
                 for topics in lda_model.get_document_topics(corpus_bow) ]

for project, corpus_topic in zip(list_of_transcripts.keys(), corpus_topics):
    print("Project ", project, " is about topic ", corpus_topic[0], " with a contribution of ", round(corpus_topic[1]*100, 2), "%")

# for i, corpus_topic in enumerate(corpus_topics):
#     print("Document ", i, " is about topic ", corpus_topic[0], " with a contribution of ", round(corpus_topic[1]*100, 2), "%")
