from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=7XlqcS6B7WA')

yt.streams.get_audio_only().download()