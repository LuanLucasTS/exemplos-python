from pytube import YouTube

link = "https://www.youtube.com/watch?v=RkID8_gnTxw"
yt = YouTube(link)
yt.streams.get_highest_resolution().download()