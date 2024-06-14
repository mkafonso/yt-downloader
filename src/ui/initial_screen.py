import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ui.media_selection import MediaSelectionScreen
from utils.validation import is_valid_youtube_url
from utils.theme import setup_styles

class InitialScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Baixador de vídeos do YouTube")
        self.root.geometry("500x300")
        self.root.configure(bg="#F5F0FA")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_styles = setup_styles(self)

        # Adicionando título
        self.title_label = tk.Label(self.root, text="Baixador de vídeos do YouTube", font=('Helvetica', 32), fg='#67329B', bg="#F5F0FA")
        self.title_label.pack(pady=(20, 10))

        # Adicionando descrição
        self.desc_label = tk.Label(self.root, text="Cole aqui a URL de um vídeo do Youtube", font=('Helvetica', 14), fg='#63637E', bg="#F5F0FA")
        self.desc_label.pack(pady=(0, 20))

        # Campo de entrada para a URL
        self.url_entry = tk.Entry(root, width=50, bg="white", fg="black")
        self.url_entry.insert(0, "")
        self.url_entry.pack()

        # Botão "Download"
        self.download_button = ttk.Button(self.root, text="Download", command=self.validate_url)
        self.download_button.pack(pady=(5, 10), ipadx=20)


    def validate_url(self):
        url = self.url_entry.get()
        if is_valid_youtube_url(url):
            self.root.destroy()
            MediaSelectionScreen(tk.Tk(), url)
        else:
            messagebox.showerror("Error", "Adicione uma URL válida")
