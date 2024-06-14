import tkinter as tk

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
