from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import sys
import datetime


client = MongoClient('mongodb://localhost:27017/')
db = client.review_db
reviews = db.reviews

def sentiment(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    if sentiment_dict['compound'] >= 0.05 :
        return "Positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        return "Negative"
    else:
        return "Neutral"

def insert_data(data):
    for item in data['data']:
        review = {
            'review_id': item['id'],
            'user': item['user'],
            'rating': int(item['rating']),
            'date': datetime.datetime.strptime(item['date'], "%d-%m-%Y"),
            'text': item['review'],
            'sentiment': sentiment(item['review']),
            'labels': item['labels']
        }
        reviews.insert_one(review)

if len(sys.argv) == 2:
    f = open(sys.argv[1],)
    data = json.load(f)
    insert_data(data)
else:
    print("Usage: python3 upload.py <json file>")
    exit()

