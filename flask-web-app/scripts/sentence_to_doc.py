"""
A modified application for sentence embeddings: semantic search

Original example can be found at: https://www.sbert.net/docs/usage/semantic_search.html

This builds off the original example, and links corpus ids (or sentence ids)
back to its original document.
"""
from sentence_transformers import SentenceTransformer, util
import numpy as np

# embedder = SentenceTransformer("search-model.zip")

documents = [
    'A man is eating food. A man is eating a piece of bread. The girl is carrying a baby. A man is riding a horse. A woman is playing violin.',
    'Two men pushed carts through the woods. A man is riding a white horse on an enclosed ground. A monkey is playing drums. A cheetah is running behind its prey.' 
]

corpus = []
lookup = {}
offset = 0

for doc_id, doc_text in enumerate(documents):
    sentences = doc_text.split(".")
    num_sentences = len(sentences)
    corpus.extend(sentences)
    lookup.update({sen_id: doc_id for sen_id in range(offset, offset+num_sentences)})
    offset += num_sentences


corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

# Query sentences:
queries = ['A man is eating pasta.', 'Someone in a gorilla costume is playing a set of drums.', 'A cheetah chases prey on across a field.']


#Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
top_k = 5
for query in queries:
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    cos_scores = util.semantic_search(query_embedding, corpus_embeddings)[0][:5]
    print(cos_scores)
    for score in cos_scores:
        print(lookup[score["corpus_id"]], score["score"])