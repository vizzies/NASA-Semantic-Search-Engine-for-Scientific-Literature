# -*- coding: utf-8 -*-
"""Semantic-Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/vizzies/Building-BERT-Model/blob/master/Semantic_Search.ipynb
"""

# from google.colab import drive
# drive.mount(‘/content/gdrive’)

# GPU Setup

import torch

# If there's a GPU available...
if torch.cuda.is_available():    

    # Tell PyTorch to use the GPU.    
    device = torch.device("cuda")

    print('There are %d GPU(s) available.' % torch.cuda.device_count())

    print('We will use the GPU:', torch.cuda.get_device_name(0))

# If not...
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

"""# Import Data Below and Parse"""

import pandas

import unicodedata

# Import this into the Colab via the Files section
with open('/content/arc-code-ti-publications.pkl', 'rb') as f:
    pubs = pandas.read_pickle(f)

import re
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)
    
def preprocess_text(sen):

    sentence = str(sen)

    # Removing html tags
    sentence = remove_tags(sentence)

    # Remove hyphenation if at the end of a line
    sentence = sentence.replace('-\n', '')

    # Fix ligatures
    sentence = unicodedata.normalize("NFKD", sentence)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence

# Not really needed any more but will leave in and just comment out
# full_texts = []
# sentences = list(pubs['Text'])
# for sen in sentences:
#     full_texts.append(preprocess_text(str(sen)))

pubs.drop(pubs[pubs['Text'] == 'PDF error occurred'].index, inplace = True) 

pubs.drop_duplicates(subset=['Text'])

pubs['Text Processed'] = pubs.apply(lambda row: preprocess_text(row['Text']), axis=1)

pubs['Word Count'] = pubs.apply(lambda row: len(row['Text Processed'].split()), axis=1)

text_df = pubs[['Text Processed',]].copy()

print(text_df)

!pip install -U sentence-transformers

"""## BERT Sentence Tranformers Semantic Search"""

"""
This is a simple application for sentence embeddings: semantic search
given query sentence,this finds the most similar sentence in this corpus
script outputs for various queries the top 5 most similar publications in the corpus
*Used open source code to aid in development
"""
from sentence_transformers import SentenceTransformer
import scipy.spatial
import pickle as pkl
embedder = SentenceTransformer('bert-base-nli-mean-tokens')

sentences = list(text_df['Text Processed'])

# Eaxmple query sentences
queries = ['How to evolve architecture for constellations and simulation', 'Build behavior of complex aerospace and modeling of safety']
query_embeddings = embedder.encode(queries,show_progress_bar=True)
text_embeddings = embedder.encode(sentences, show_progress_bar=True)
#
# Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
closest_n = 5
print("\nTop 5 most similar sentences in corpus:")
for query, query_embedding in zip(queries, query_embeddings):
    distances = scipy.spatial.distance.cdist([query_embedding], text_embeddings, "cosine")[0]

    results = zip(range(len(distances)), distances)
    results = sorted(results, key=lambda x: x[1])

    print("------------------------User Query: ------------------------")
    print("--",query,"--")
    print("------------------------------------------------------------")


# Print out all information for the publications related to user query and a relevancy score
    for idx, distance in results[0:closest_n]:
        print("Relevancy Score:   ", "(Score: %.0f%%)" % ((1-distance) * 100.0) , "\n" )
        row_dict = pubs.iloc[idx].to_dict() # pubs.loc[pubs.index== sentences[idx]].to_dict()
        #print(row_dict)
        print("Title:  " , row_dict["Title"]  , "\n")
        print("Authors:  " , row_dict["Authors"] , "\n")
        print("Date:  " , row_dict["Date"] , "\n")
        print("Link:  " , row_dict["Link"] , "\n")
        print("Abstract Length:  " , row_dict["Abstract Length"] , "\n")
        print("Abstract:  " , row_dict["Abstract"] , "\n")
        print("-------------------------------------------")
