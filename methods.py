import pickle
from tkinter import *

from pytube import YouTube


# YouTubeDL will allow the user to download videos from YouTube to their computer and will offer customization settings
# to meet the needs of the user.

# Gets the information of the YouTube video the user wants to download
# yt = YouTube(input("Video address:"))

# print(yt.streams)

# Selects the version of the video the user wants to download
# stream = yt.streams.get_by_itag(int(input("Itag for desired stream:")))
# Directs the video file to the proper folder
# file_path = input("File Path:")
# stream.download(file_path)

# print("Video downloaded!")


def save_path(path):
    with open("path.txt", "wb") as file:
        pickle.dump(path, file)
        file.close()
    print("Path pickled!")


def load_path():
    with open("path.txt", "rb") as file:
        path = pickle.load(file)
        file.close()
    print("Path loaded!")
    return path


def get_streams(url, listbox: Listbox):
    yt = YouTube(url)
    streams = yt.streams.filter()

    for stream in streams:
        length = listbox.size()
        listbox.insert(length, stream)

    print("Streams gathered!")


def download_video(url, itag_box: Entry, path_entry: Entry):
    yt = YouTube(url)
    itag = int(itag_box.get())
    stream = yt.streams.get_by_itag(itag)
    stream.download(path_entry.get())
    print("Video downloaded!")
