from textblob import TextBlob
from matplotlib import pyplot as plt
import pandas as pd

#function to visualize the sentiment distribution
def visualize_sentiments(sentiment_results):
    #count the number of each sentiment
    
    sentiment_count = pd.Series(sentiment_results).value_counts()
    
    #plot the sentiment distribution
    sentiment_count.plot(kind='bar', color=['red', 'blue', 'green'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

visualize_sentiments(sentiment_results)