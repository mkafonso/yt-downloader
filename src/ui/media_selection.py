import tkinter as tk
from tkinter import ttk
from utils.downloader import get_video_info
from ui.download import DownloadScreen
from utils.theme import setup_styles

class MediaSelectionScreen:
    def __init__(self, root, url):
        self.root = root
        self.root.title("Selecione o tipo de mídia")
        self.root.geometry("500x300")
        self.root.configure(bg="#F5F0FA")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_styles = setup_styles(self)

        self.url = url
        self.video_info = get_video_info(url)

        # Adicionando título
        self.title_label = tk.Label(root, text="Selecione o tipo de mídia", font=('Helvetica', 32), fg='#67329B', bg="#F5F0FA")
        self.title_label.pack(pady=(20, 10))

        self.video_button = tk.Button(root, text="Video (mp4)", command=self.select_video)
        self.video_button.pack(pady=(5, 10), ipadx=20)

        self.audio_button = tk.Button(root, text="Audio (mp3)", command=self.select_audio)
        self.audio_button.pack(pady=(5, 10), ipadx=20)

    def select_video(self):
        self.root.destroy()
        DownloadScreen(tk.Tk(), self.url, 'video')

    def select_audio(self):
        self.root.destroy()
        DownloadScreen(tk.Tk(), self.url, 'audio')
