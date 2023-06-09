import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re
Base_df = pd.read_csv("Back-End/wikir.csv") 
documents_df = pd.read_csv("Back-End/wikir-French.csv")

# Data Cleaning
same ={
    "ii":"the second",
    "us":"united states of america",
    "etc":"extra",
    "pov":"point of view",
    "ASAP": "As Soon As Possible",
    "FAQ": "Frequently Asked Questions",
    "CEO": "Chief Executive Officer",
    "CFO": "Chief Financial Officer",
    "COO": "Chief Operating Officer",
    "DIY": "Do It Yourself",
    "FYI": "For Your Information",
    "HR": "Human Resources",
    "IT": "Information Technology",
    "JPEG": "Joint Photographic Experts Group",
    "PDF": "Portable Document Format",
    "TBA": "To Be Announced",
    "UFO": "Unidentified Flying Object",
    "VPN": "Virtual Private Network",
    "WYSIWYG": "What You See Is What You Get",
    "USA": "United States of America",
    "UK": "United Kingdom",
    "UN": "United Nations",
    "NASA": "National Aeronautics and Space Administration",
    "FBI": "Federal Bureau of Investigation",
    "NATO": "North Atlantic Treaty Organization",
    "WWW": "World Wide Web",
    "HTML": "Hypertext Markup Language",
    "CSS": "Cascading Style Sheets",
    "JSON": "JavaScript Object Notation",
    "API": "Application Programming Interface",
    "URL": "Uniform Resource Locator",
    "SMS": "Short Message Service",
    "WiFi": "Wireless Fidelity",
    "GPS": "Global Positioning System",
    "CEO": "Chief Executive Officer",
    "CIO": "Chief Information Officer",
    "CTO": "Chief Technology Officer",
    "HR": "Human Resources",
    "PR": "Public Relations",
    "FAQ": "Frequently Asked Questions",
    "FYI": "For Your Information",
    "ETA": "Estimated Time of Arrival",
    "DIY": "Do It Yourself",
    "PC": "Personal Computer",
    "CPU": "Central Processing Unit",
    "RAM": "Random Access Memory",
    "HDD": "Hard Disk Drive",
    "SSD": "Solid State Drive",
    "USB": "Universal Serial Bus",
    "AI": "Artificial Intelligence",
    "IoT": "Internet of Things",
    "AR": "Augmented Reality",
    "VR": "Virtual Reality",
    "ML": "Machine Learning",
    "DL": "Deep Learning",
    "ATM": "Automated Teller Machine",
    "B2B": "Business to Business",
    "B2C": "Business to Consumer",
    "CCTV": "Closed Circuit Television",
    "CRM": "Customer Relationship Management",
    "DNS": "Domain Name System",
    "DVD": "Digital Versatile Disc",
    "GIF": "Graphics Interchange Format",
    "HTML5": "Hypertext Markup Language version 5",
    "HTTP": "Hypertext Transfer Protocol",
    "HTTPS": "Hypertext Transfer Protocol Secure",
    "IMAP": "Internet Message Access Protocol",
    "IP": "Internet Protocol",
    "ISP": "Internet Service Provider",
    "JPEG": "Joint Photographic Experts Group",
    "LAN": "Local Area Network",
    "LCD": "Liquid Crystal Display",
    "LTE": "Long Term Evolution",
    "MBA": "Master of Business Administration",
    "MP3": "MPEG Audio Layer-3",
    "PDF": "Portable Document Format",
    "PHP": "Hypertext Preprocessor",
    "POP": "Post Office Protocol",
    }


trash_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
def remove_trash(text):
  return re.sub("["+"".join(trash)+"]","",text)


def lower(text):
  return text.lower()

def replace_sames(text, sames=same):
  temp = text
  for word in text.split(' '):
    if word in sames.keys():
      temp = temp.replace(word, sames[word])
  return temp

english_stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def remove_stopwords(text, stopwords = english_stopwords):
  ls = []
  for word in text.split(' '):
    if(word != '' and word.lower() not in english_stopwords):
       ls.append(word)
  return ' '.join(ls)

from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nltk.download('wordnet')

def lemmatize(text):
  return ' '.join([lemmatizer.lemmatize(i)for i in text.split(' ')])
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
def stem(text):
    return ' '.join([stemmer.stem(i)for i in text.split(' ')]) 

def data_process(text_df, remove_trash_=True, lower_=True, replace_sames_=True, same_dict=same, remove_stopwords_=True, lemmatize_=True, stem_=True):
  if(type(text_df)==type(pd.DataFrame())):
    if remove_trash_: text_df = text_df.apply(lambda x: remove_trash(x))
    if lower_: text_df = text_df.apply(lambda x: lower(x))
    if replace_sames_: text_df = text_df.apply(lambda x: replace_sames(x, same_dict))
    if remove_stopwords_: text_df = text_df.apply(lambda x: remove_stopwords_(x))
    if lemmatize_: text_df = text_df.apply(lambda x: lemmatize(x))
    if stem_: text_df = text_df.apply(lambda x: stem(x))
  if(type(text_df)==type(str())):
    if remove_trash_: text_df = remove_trash(text_df)
    if lower_: text_df = lower(text_df)
    if replace_sames_: text_df = replace_sames(text_df, same_dict)
    if remove_stopwords_: text_df = remove_stopwords(text_df)
    if lemmatize_: text_df = lemmatize(text_df)
    if stem_: text_df = stem(text_df)
  return text_df

def get_recommendations(docs_df, scores_array, start=0, n=10, TextColName="text"):
  sorted_indices = scores_array.argsort()[::-1]
  start = min(start, len(sorted_indices))
  n = min(start+n, len(sorted_indices))
  docs_id = list()
  for position, idx in enumerate(sorted_indices[start:start+n]):
    row = docs_df.iloc[idx]
    text = row[TextColName]
    score = scores_array[idx]
    print(docs_df.iloc[idx].doc_id)
    print(f"{position + 1} {idx} [score = {score}]: {text}")
    docs_id.append(docs_df.iloc[idx].doc_id)
  return docs_id

english_Vectorizer = TfidfVectorizer()
corpus = list(preprocess(Base_df.text.astype('U')))
english_corpus_vectorized = english_Vectorizer.fit_transform(corpus)

from sklearn.feature_extraction.text import TfidfVectorizer
french_Vectorizer = TfidfVectorizer()
corpus = list(preprocess(documents_df.text))
french_corpus_vectorized = french_Vectorizer.fit_transform(corpus)



import joblib
english_corpus_vectorized = joblib.load('Back-End/wikir_vectorizer.tfidf')
french_corpus_vectorized = joblib.load('Back-End/wikir-French_vectorizer.tfidf')

def get_docs_french(q, docs_df, start=0, n=10, TextColName="text"):
  query = data_process(text_df=q)
  query_vectorized = french_Vectorizer.transform([query])
  scores = query_vectorized.dot(french_corpus_vectorized.transpose())
  scores_array = scores.toarray()[0]
  docs_id = get_recommendations(docs_df, scores_array, start, n)
  docs_df =  docs_df.set_index('doc_id')
  docs_df = docs_df.loc[docs_id]
  print(docs_df.text.head())
  print(docs_df.columns)
  print(docs_df)
  docs_list = []
  for doc in docs_df:
    print("doc: " + str(doc))
    docs_list.append({"doc_id":str(doc.doc_id), "title":str(doc.title), "text":str(doc.text)})
  return docs_list

def get_docs_english(q, docs_df, start=0, n=10, TextColName="text"):
  query = data_process(text_df=q)
  query_vectorized = english_Vectorizer.transform([query])
  scores = query_vectorized.dot(english_corpus_vectorized.transpose())
  scores_array = scores.toarray()[0]
  docs_id = get_recommendations(docs_df, scores_array, start, n)
  docs_df =  docs_df.set_index('doc_id')
  docs_df = docs_df.loc[docs_id]
  docs_df = list(docs_df.to_dict().values())
  return docs_df

