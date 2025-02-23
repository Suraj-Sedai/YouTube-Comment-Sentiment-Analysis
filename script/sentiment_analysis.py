from textblob import TextBlob
#function to get the sentiment of the comments
def get_sentiment(comments):
    sentiment_results = []

    for comment in comments:
        analysis = TextBlob(comment).sentiment.polarity

        if analysis > 0:  # Check the polarity of the sentiment
            sentiment_results.append("Positive")
        elif analysis == 0:
            sentiment_results.append("Neutral")
        else:
            sentiment_results.append("Negative")
    
    return sentiment_results
    
#analyze the sentiment of the comments
sentiment_results = get_sentiment(comments)