import moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip("D:\Luan\Videos\MORE-KDA.mp4")
audio = video.audio
audio.write_audiofile('audio.mp3')