from methods import *
from os.path import exists
main_window = Tk()  # instantiate an instance of a window
main_window.geometry("800x400")
main_window.title("YouTubeDL")
main_window.configure(bg="Black")

main_window.iconbitmap("yt-logo.ico")

# Main Window Widgets
url_label = Label(main_window, text="Video URL", bg="#C20927", font="ComicSansMS", fg="White")
url_frame = Frame(main_window)
url_entry = Entry(url_frame, width=50)

# If you want a scroll bar in your widget, you have to connect the scrollbar widget to the widget being scrolled
stream_frame = Frame(main_window)
stream_label = Label(main_window, text="Select Stream", bg="#C20927", font="ComicSansMS", fg="White")
stream_scrollbar = Scrollbar(stream_frame)
stream_xscrollbar = Scrollbar(main_window, orient="horizontal")
stream_listbox = Listbox(stream_frame, width=120, xscrollcommand=stream_xscrollbar.set,
                         yscrollcommand=stream_scrollbar.set)
stream_xscrollbar.config(command=stream_listbox.xview)
stream_scrollbar.config(command=stream_listbox.yview)

streams_button = Button(url_frame, text="Get Streams", command=lambda: get_streams(url_entry.get(), stream_listbox),
                        bg="Blue", font="ComicSansMS", fg="White")

itag_label = Label(main_window, text="ITAG Number", bg="#C20927", font="ComicSansMS", fg="White")
itag_entry = Entry(main_window)

file_label = Label(main_window, text="Output Path", bg="#C20927", font="ComicSansMS", fg="White")

file_frame = Frame(main_window)

file_entry = Entry(file_frame, width=50)
# We want to load the previous path into the box before showing it to the user
if exists("path.txt"):
    path = load_path()
    file_entry.insert(0, path)

file_button = Button(file_frame, text="Save", command=lambda: save_path(file_entry.get()),
                     bg="Blue", font="ComicSansMS", fg="White")

download_button = Button(main_window, text="Download",
                         command=lambda: download_video(url_entry.get(), itag_entry, file_entry),
                         bg="Blue", font="ComicSansMS", fg="White")
# Packing goes at the end because sometimes we have to initialize widgets in a different order than how they are placed
url_label.pack()
url_frame.pack()
url_entry.pack(side=LEFT)
streams_button.pack(side=LEFT)
stream_label.pack()
stream_frame.pack()
stream_listbox.pack(side=LEFT)
stream_scrollbar.pack(side=LEFT, fill=Y)
stream_xscrollbar.pack(fill=X)
itag_label.pack()
itag_entry.pack()
file_label.pack()
file_frame.pack()
file_entry.pack(side=LEFT)
file_button.pack(side=LEFT)
download_button.pack()

# Opens the main window
main_window.mainloop()
