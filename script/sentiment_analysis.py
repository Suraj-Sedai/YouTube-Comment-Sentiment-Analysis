from textblob import TextBlob

def get_sentiment(comments):
    sentiment_results = []

    for comment in comments:
        analysis = TextBlob(comment).sentiment.polarity

        if analysis > 0:  # Positive sentiment
            sentiment_results.append("Positive")
        elif analysis == 0:  # Neutral sentiment
            sentiment_results.append("Neutral")
        else:  # Negative sentiment
            sentiment_results.append("Negative")
    
    return sentiment_results
