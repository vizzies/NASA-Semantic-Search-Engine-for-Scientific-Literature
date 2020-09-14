## Science Discovery Engine  
Develop an intelligent literature searchand analysis application that reads NASA-relevant scientific articles using natural language processing and textmining, returns knowledge analysis andrelevant scientific findings, and reveals knowledge gaps and multi-disciplinary research opportunities.  

## Summary  
This project explores the use of Natural Language Processing (NLP) and web development for a proof of concept for a science discovery engine. The project aims to improve the discovery experience that exists in current tools such as the Ames Research Center (ARC) TI publication website. We utilized BERT models, state-of-the-art technologies in NLP, which are trained in accuracy—they are able to parse the context and nuance of queries, allowing them to better understand the intent of users' searches.

### How We Addressed This Challenge  
Tranformers (BERT)  
Our project uses the latest technologies in the Natural Language Processing field to create an intelligent semantic search engine specifically for scientific articles. The main architecture of our project stems from Transformers, the latest state-of-the-art novel architecture that is able to solve sequence-to-sequence (Seq2Seq) problems with long-range dependencies. This was first proposed in a paper from Google Brain, titled 'Attention is All You Need' that shows how transformers rely on self-attention mechanisms, instead of convolutions or solely recurrent neural networks like previous technologies. We decided to use the BERT architecture, which has a structure that consists of encoder and decoder parts, making it easy for fine tuning. (Side note: Google Search actually uses BERT extensively)

### Project Implementation  
The project implementation includes three parts: a Natural Language Processing (NLP) model, an interactive mockup of the user interface, and a lightweight web API for serving query results. 

The NLP model uses Bidirectional Encoder Representations from Transformers (BERT) for semantic search. The model generates scores for the most relevant sentences from Ames Research Center (ARC) TI Publications from user generated queries. In addition to the scores; the title, abstract, abstract character length, and word count are provided. The model is embedded into a Flask application with a set of endpoints for processing user queries and returning results, as well as referencing specific publications by a unique identifier. 

The interactive mockup showcases what the user interface would look like and how it would behave. The mockup features a search bar which accepts natural language queries, receives search results, and visually displays those results similarly to common search engines such as Google. 

### Future Integration  
With more time, the team would integrate these components to create a fully-functional tool which could be used for science discovery. This integration would allow users to navigate to a website, which would submit queries to the Flask application, receive search results, and display them.

## How We Developed this Project  
### Inspiration  
The fact that we had a lot of people with mixed skills in data visualization and natural language processing inspired us to choose this challenge, as it would be a good opportunity to put everyone's skills to use in a collaborative manner. 

### Approach  
The reason we chose to approach this challenge with BERT is because it has been used in several successful search engines, and it is considered one of the most modern technologies in NLP with its use of transformers and recurrent neural networks. 

### Tools  
Python, PyTorch, BERT, HuggingFace Transformers, Sentence_Transformers, Pandas, SciPy, Pickle, Google Cloud Pub/Sub, Google Colab Environment/GPUs, Flask, Figma, and HTML/CSS

## Development  
### Front-end Development  
We started drafting the application in Figma, then went straight into developing due to time constraints. Due to time, we decided to place more emphasis on the visualization component (mockup) in Figma while still ensuring we would have a front-end developed product.

### Model-Development & Processing  
Originally, we intended to use a model that classified the documents, but after realizing that the data was not pre-labeled, we switched to a Semantics Search that utilizes a Sentence_Transformers library to take in user queries and find five sentences most related to the user query from the entire corpus based on cosine similarity. It then gives all related info—link, text, info, abstract, abstract length, title, authors, publisher, date—in each document that those sentences came from. 

We had issues with processing the data for embedding because the model was expecting a 2D array, while we were try to process a 3D array. We had to transform the data into a format that was accepted by the model, which was a challenge to overcome. We figured this out by using an encoder and changing our data frame to match the correct format.

We reshaped the datasets—fixing ligatures and removing white spaces, punctuation & numbers, html tags, hyphenation at the end of lines, single characters, and multiple spaces—to prepare for the model processing.

### Back-end Development  
We're using a Flask application running Flask-RESTful. Our database is a SQL database, and the library we're using is SQLAlchemy to interact with and manipulate the database with Python objects. The "/results" endpoint returns results formatted as list, and "/results/id" returns a specific result with the given id.

There is one query parameter "q", (ex. "/results?q=dummysearchterm"). On startup, the app encodes the model with the sentences from the pickle file. If the "q" parameter is specified, Flask will call the function "get_search_results" to get the top n items where "n" is the number of desired results.

**Project Demo**  
(Emailed to Llewellyn, Alicia (JSC-JA)[KBR Wyle Services, LLC] <alicia.llewellyn-1@nasa.gov>; Biegel, Bryan A. (ARC-T) <bryan.biegel@nasa.gov>)

**Project Code**  
[https://github.com/vizzies/NASA-Semantic-Search-Engine-for-Scientific-Literature](https://github.com/vizzies/NASA-Semantic-Search-Engine-for-Scientific-Literature)

**Data & Resources**  
* [https://ti.arc.nasa.gov/publications/](https://ti.arc.nasa.gov/publications/) (Ames Code TI repository)
* [https://nasa.sharepoint.com/:f:/t/DTHackathon/EtzKKE6PKAhLs7eNZF1IYrYBOKXppJMS__RvFdSPN7AcyQ?e=1fFVgE](https://nasa.sharepoint.com/:f:/t/DTHackathon/EtzKKE6PKAhLs7eNZF1IYrYBOKXppJMS__RvFdSPN7AcyQ?e=1fFVgE) (Selected datasets from Ames Code TI repository)
* [https://nasa.sharepoint.com/:x:/t/DTHackathon/ES4X1hXMHDhJq0OidHKy8_EBwHn-P3bKv_AeI4tMC85G1g?e=1aHxIo](https://nasa.sharepoint.com/:x:/t/DTHackathon/ES4X1hXMHDhJq0OidHKy8_EBwHn-P3bKv_AeI4tMC85G1g?e=1aHxIo) (Example semantic queries and expected matching documents within the code TI publications dataset)
* [https://github.com/UKPLab/sentence-transformers](https://github.com/UKPLab/sentence-transformers) (Sentence Transformers)
* [https://flask.palletsprojects.com/en/1.1.x/](https://flask.palletsprojects.com/en/1.1.x/) (Application Building Framework)
* [https://www.figma.com/](https://www.figma.com/)Tool used for creating front-end mockup
* [https://pytorch.org/](https://pytorch.org/)
* [https://github.com/huggingface/transformers](https://github.com/huggingface/transformers) (HuggingFace Transformers)  

**Tags**  
•#artificial-intelligence #machine-learning #search-engine #semantic-search #NLP #text-mining #scientific-literature #feature-engineering #model-development #web-development #BERT

