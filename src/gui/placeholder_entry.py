import tkinter as tk
from tkinter import ttk

# Classe personalizada para Entry com placeholder
class PlaceholderEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", placeholder_color='#ddd', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.default_fg_color = self['foreground']
        self.default_bg_color = self['background']
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        self._add_placeholder()

    # Método para limpar o placeholder quando o campo recebe foco
    def _clear_placeholder(self, e):
        if self['foreground'] == self.placeholder_color:
            self.delete(0, tk.END)
            self['foreground'] = 'black'

    # Método para adicionar o placeholder quando o campo perde foco
    def _add_placeholder(self, e=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['foreground'] = self.placeholder_color
