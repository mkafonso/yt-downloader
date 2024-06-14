import queue
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from threading import Thread
from utils.downloader import get_video_info, download_stream
from utils.theme import setup_styles

class DownloadScreen:
    def __init__(self, root, url, media_type):
        self.root = root
        self.url = url
        self.media_type = media_type
        self.root.title("Download")
        self.root.geometry("500x300")
        self.root.configure(bg="#F5F0FA")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_styles = setup_styles(self)


        self.title_label = tk.Label(self.root, text="Escolha a resolução:", font=('Helvetica', 32), fg='#67329B', bg="#F5F0FA")
        self.title_label.pack(pady=(20, 10))


        self.streams = self.get_streams()
        self.stream_map = {self.get_stream_label(stream): stream for stream in self.streams}
        self.stream_var = tk.StringVar(value=list(self.stream_map.keys())[0])
        self.stream_menu = tk.OptionMenu(root, self.stream_var, *self.stream_map.keys())
        self.stream_menu.pack()

        self.download_button = tk.Button(root, text="Download", command=self.start_download)
        self.download_button.pack()

        self.progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
        self.progress.pack()

        self.queue = queue.Queue()
        self.root.after(100, self.process_queue)

    def get_streams(self):
        info = get_video_info(self.url)
        if self.media_type == 'video':
            return info['video_streams']
        else:
            return info['audio_streams']

    def get_stream_label(self, stream):
        return f"{stream.resolution or stream.abr}"

    def start_download(self):
        selected_label = self.stream_var.get()
        selected_stream = self.stream_map[selected_label]
        output_path = filedialog.askdirectory()
        if not output_path:
            return

        self.download_thread = Thread(target=self.download, args=(selected_stream, output_path))
        self.download_thread.start()

    def download(self, stream, output_path):
        try:
            download_stream(stream, output_path, self.update_progress)
            self.queue.put(("show_message", ("Download Complete", "Download concluído com sucesso!")))
        except Exception as e:
            self.queue.put(("show_message", ("Error", str(e))))
        finally:
            self.queue.put(("destroy", None))

    def update_progress(self, stream, chunk, file_handle, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.queue.put(("progress_update", percentage))

    def process_queue(self):
        try:
            while True:
                task, args = self.queue.get_nowait()
                if task == "show_message":
                    self.show_message(*args)
                elif task == "progress_update":
                    self.progress_update(args)
                elif task == "destroy":
                    self.root.after(100, self.root.destroy)
        except queue.Empty:
            pass
        self.root.after(100, self.process_queue)

    def progress_update(self, percentage):
        print(f"Updating progress: {percentage:.2f}%")
        self.progress['value'] = percentage
        self.root.update_idletasks()

    def show_message(self, title, message):
        self.root.after(0, messagebox.showinfo, title, message)
