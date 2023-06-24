import tweepy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from textblob import TextBlob
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import scrolledtext
import config

# Twitter API credentials
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = []

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    return 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'

def scrape_twitter_feeds(topic, count):
    global tweets
    tweets = api.search_tweets(q=topic, count=count, lang='en')  # Filter tweets by language

    positive_tweets = 0
    negative_tweets = 0
    neutral_tweets = 0

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet.text)

        if sentiment == 'positive':
            positive_tweets += 1
        elif sentiment == 'negative':
            negative_tweets += 1
        else:
            neutral_tweets += 1

    return positive_tweets, negative_tweets, neutral_tweets


def visualize_sentiment_analysis(positive, negative, neutral):
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive, negative, neutral]
    colors = ['#00ff00', '#ff0000', '#808080']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Sentiment Analysis of ' + topic + ' Twitter Feeds\n')

    # Display the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


# Hard-coded topic and count of tweets
topic = input("What topic would you like to research: ")
tweet_count = input("How many Tweets would you like to analyze: ")

# Scrape Twitter feeds and perform sentiment analysis
positive_count, negative_count, neutral_count = scrape_twitter_feeds(topic, tweet_count)

# Create a tkinter window
window = tk.Tk()
window.title("Sentiment Analysis")
window.geometry("1000x1000")

# Create a scrolled text area to display the results
text_area = scrolledtext.ScrolledText(window, width=60, height=20)
text_area.pack(pady=10)

# Perform sentiment analysis on tweets and display them in the scrolled text area
for tweet in tweets:
    text = tweet.text
    sentiment = analyze_sentiment(text)
    result = f'Tweet: {text}\nSentiment: {sentiment}\n\n'
    text_area.insert(tk.END, result)

# Visualize the sentiment analysis
visualize_sentiment_analysis(positive_count, negative_count, neutral_count)

# Start the tkinter event loop
window.mainloop()
