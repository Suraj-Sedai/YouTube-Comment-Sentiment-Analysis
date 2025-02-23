from googleapiclient.discovery import build

# Setup YouTube API client
api_key = 'AIzaSyDmCC1ksrejVm7oZCOe09ASVOYzrUTRhSs'
youtube = build('youtube', 'v3', developerKey=api_key)

def fetch_comments(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split('v=')[1]  # Split the URL by 'v=' and get the second part

    comments = []
    # Get comments from YouTube API
    result = youtube.commentThreads().list(
        part='snippet',  # Get the snippet of the comments
        videoId=video_id,  # Video ID
        textFormat="plainText",  # Get comments in plain text
        maxResults=100  # Get 100 comments
    ).execute()  # Execute the request

    # Store comments
    for item in result['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments
