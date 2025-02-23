import pandas as pd
import matplotlib.pyplot as plt
from sentiment_analysis import get_sentiment
from fetch_comments import fetch_comments


# Input video URL
video_url = input("Enter the video URL: ")

# Fetch comments from YouTube
comments = fetch_comments(video_url)

# Analyze the sentiment of the comments
sentiment_results = get_sentiment(comments)

# Function to visualize the sentiment distribution
def visualize_sentiments(sentiment_results):
    # Count the number of each sentiment
    sentiment_count = pd.Series(sentiment_results).value_counts()

    # Plot the sentiment distribution
    sentiment_count.plot(kind='bar', color=['red', 'blue', 'green'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

# Visualize sentiment distribution
visualize_sentiments(sentiment_results)
