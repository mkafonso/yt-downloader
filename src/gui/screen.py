import tkinter as tk
from tkinter import messagebox, ttk
from gui.placeholder_entry import PlaceholderEntry

# Classe para a tela inicial
class InitialScreen:
    def __init__(self, app):
        self.app = app
        self.root = app.root

    def show(self):
        # Adicionando título
        self.title_label = tk.Label(self.root, text="Baixador de vídeos do YouTube", font=('Helvetica', 32), fg='#67329B', bg="#F5F0FA")
        self.title_label.pack(pady=(20, 10))

        # Adicionando descrição
        self.desc_label = tk.Label(self.root, text="Baixe qualquer vídeo público do YouTube", font=('Helvetica', 14), fg='#63637E', bg="#F5F0FA")
        self.desc_label.pack(pady=(0, 20))

        # Campo de entrada para a URL
        self.url_entry = PlaceholderEntry(self.root, "Cole aqui a URL de um vídeo do Youtube", width=50)
        self.url_entry.pack(pady=(0, 10))

        # Botão "Download"
        self.download_button = ttk.Button(self.root, text="Download", command=self.validate_url)
        self.download_button.pack(pady=(5, 10), ipadx=20)


    # Método para validar a URL
    def validate_url(self):
        messagebox.showerror("message", "Olá, mundo!")
        return
