from pytube import YouTube
import tkinter as tk 
from tkinter import filedialog

def download_youtube_video( url, save_path):
    try:
       yt =YouTube(url)
       stream =  yt.filter(progressive = True ,file_extension = "mp4") 
       highest_res_stream = stream.get_highest_resolution()
       highest_res_stream.download(output_path=save_path)
       print ("video download successully")
    except Exception as e:
       print(e)

url = "https://www.youtube.com/watch?v=H2-lXGKTE60"
save_path = "downloads"

download_youtube_video( url, save_path)