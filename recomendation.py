import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

# loading the scraped data
file_path = 'scraped_news.csv'
news_data = pd.read_csv(file_path)

# preprocessing steps (lowercasing, removing stopwords, and stemming)
stop_words = set(stopwords.words('english'))
porter = PorterStemmer()

def preprocess_text(text):
    # convert text to lowercase
    text = text.lower()
    # tokenize the text
    tokens = word_tokenize(text)
    # remove punctuation and stopwords, and apply stemming
    tokens = [porter.stem(token) for token in tokens if token not in stop_words and token not in string.punctuation]
    # join tokens back into a single string
    return ' '.join(tokens)

# preprocess the article titles
news_data['processed_title'] = news_data['title'].apply(preprocess_text)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(news_data['processed_title'])

# function to get recommendations based on input keywords
def get_recommendations_based_on_keywords(input_keywords, tfidf_matrix=tfidf_matrix, news_data=news_data):
    # preprocess input keywords
    input_keywords = preprocess_text(input_keywords)
    # Vectorize the input keywords
    input_keywords_vec = tfidf_vectorizer.transform([input_keywords])
    # cosine similarity 
    cosine_similarities = cosine_similarity(input_keywords_vec, tfidf_matrix).flatten()
    # indices of top 5 most similar articles
    similar_indices = cosine_similarities.argsort()[:-6:-1]
    # top 5 most similar articles
    return news_data.iloc[similar_indices][['title', 'link']]


# input_keywords = "intense fighting in Rafah"
input_keywords = input("Enter the text:")
recommendations = get_recommendations_based_on_keywords(input_keywords)
print(recommendations)
