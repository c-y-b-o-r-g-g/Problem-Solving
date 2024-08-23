import requests

# Function to search for song lyrics
def search_lyrics(song_name):
    base_url = "https://api.lyrics.ovh/v1/"
    response = requests.get(base_url + song_name)
    if response.status_code == 200:
        data = response.json()
        lyrics = data['lyrics']
        print("\nLyrics:\n")
        print(lyrics)
    else:
        print("\nLyrics not found.")

# Function to search for song on YouTube and display available versions
def search_youtube(song_name):
    api_key = "your_youtube_api_key"  # Replace with your YouTube Data API key
    base_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": song_name,
        "key": api_key,
        "type": "video",
        "maxResults": 5  # Increase or decrease as needed
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("\nAvailable versions on YouTube:\n")
        for idx, item in enumerate(data['items']):
            video_title = item['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            print(f"{idx + 1}. {video_title} - {video_url}")
    else:
        print("\nError searching YouTube.")

# Main function
def main():
    song_name = input("Enter the name of the song: ")
    search_lyrics(song_name)
    search_youtube(song_name)

if __name__ == "__main__":
    main()
