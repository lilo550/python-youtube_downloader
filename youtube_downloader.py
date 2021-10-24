from tkinter import*
from pytube import*

class YoutubeDownloader:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("YouTube_Downloader")
        self.window.geometry('1000x450')
        self.window.minsize(1000, 450)
        self.window.config(bg='#181818')
        self.window.iconbitmap('logo.ico')
        self.window.iconphoto(False, PhotoImage(file='logo.png'))

        # component initialization
        self.url = StringVar()
        self.frame = Frame(self.window, bg='white')

        # component creation
        self.create_widgets()

        # frame packaging
        self.frame.pack()

    def create_widgets(self):
        self.create_title()
        self.create_entry()
        self.create_button()

    def create_title(self):
        label_title = Label(self.window, width=35, text="YouTube_Downloader", font=('Courrier', 32), bg='white', fg='black')
        label_title.pack(pady=20)
        label_title_entry = Label(self.frame, width=35, text="Link", font=('Courrier', 22), bg='white', fg='black')
        label_title_entry.pack()

    def create_entry(self):
        self.url = StringVar()
        url_entry = Entry(self.frame, text=self.url, font=('Courrier', 27), bg='white', fg='black', relief='solid', width = 22)
        url_entry.pack(pady=15)

    def create_button(self):
        download_button = Button(self.frame, text="Download", font=('Courrier', 27), width = 13, command=self.download_youtube_video)
        download_button.pack(pady=15)

    def download_youtube_video(self):
        youtube = YouTube(self.url.get())
        video = youtube.streams.get_highest_resolution()
        video.download()
        

# Display
yt = YoutubeDownloader()
yt.window.mainloop()

