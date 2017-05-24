import requests
import json
import youtube_dl
from termcolor import colored

API_KEY = #<Enter Your API KEY>
video_urls = []


def main():
    search_term = input('Enter Song Name => ')
    print('Getting Data.....')
    url = 'https://www.googleapis.com/youtube/v3/search?q='+ search_term +'&type=video&part=snippet&key=' + API_KEY
    json_dump = requests.get(url).json()['items']
    
    
    for i, data in enumerate(json_dump):
        print( colored(i + 1, 'red') , end=' => ')
        video_urls.append('https://youtube.com/watch?v=' + data['id']['videoId'])
        print(data['snippet']['title'], end='\n\n')

    download_song = video_urls[int(input('Enter Serial number of song you want to download => ')) - 1]

    print(download_song)
    # Download Song
    ydl_opts = {
        'format': 'bestvideo',
        'noplaylist' : True,        
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([download_song])

    print('Your Song Downloaded!')

if __name__ == '__main__':
    main()
