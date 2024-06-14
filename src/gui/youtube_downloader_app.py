import tkinter as tk
from tkinter import ttk
from gui.screen import InitialScreen

# Classe principal do aplicativo
class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Baixador de vídeos do YouTube")
        self.root.geometry("500x300")
        self.root.configure(bg="#F5F0FA")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_styles()

        self.initial_screen = InitialScreen(self)
        self.initial_screen.show()

    # Método para configurar os estilos dos widgets
    def setup_styles(self):
        self.style.configure("TButton", padding=6, relief="flat", background="#67329B", foreground="#F5F0FA", font=('Helvetica', 12))
        self.style.map("TButton", background=[("active", "#573088")], foreground=[("active", "#F5F0FA")])
        self.style.configure(
            "TEntry",
            padding=6,
            font=('Helvetica', 12),
            fieldbackground="#F5F0FA",
            bordercolor="#dddddd",
            highlightbackground="white",
            highlightcolor="white",
            highlightthickness=2,
            fieldforeground="black",
            relief=tk.FLAT,
            borderwidth=0,
        )

