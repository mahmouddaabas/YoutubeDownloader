import youtube_dl


def download_video(video):
    while True:
        video = video.strip()
        ydl = youtube_dl.YoutubeDL()
        try:
            ydl.download([video])
            break;
        except:
            print("Invalid URL!")
            break;

        # link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ")
        # video = link_of_the_video.strip()

        download_video(video)