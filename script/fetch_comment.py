def fetch_comments(video_url):
    #extract the video id from the url
    video_id = video_url.split('v=')[1]   #split the url by 'v=' and get the second part

    comments = []
    #get comments from YT API
    result = youtube.commentThreads().list(
        part='snippet',                 #get the snippet of the comments
        videoId=video_id,           #video id
        textFormat="plainText",     #get comments in plain text
        maxResults=100      #get 100 comments
        ).execute()     #execute the request
    
    #store comments
    for item in result['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments

video_url = input("Enter the video URL: ")
comments = fetch_comments(video_url)
print(comments[:5])  # Display first 5 comments