import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import pygame
import os

class KalkulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # Label Pembuat (Credit)
        credit_label = ttk.Label(
        root,
        text="By FallSec-Tech",
        font=("Helvetica", 5, "italic"),
        anchor="center",
        bootstyle="secondary"
    )
        credit_label.pack(pady=(5, 10))


        # Inisialisasi pygame mixer
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("Asset/click.mp3")

        # Logo
        logo_img = Image.open("Asset/logo.png").resize((120, 120))
        logo_photo = ImageTk.PhotoImage(logo_img)
        self.logo_label = ttk.Label(root, image=logo_photo)
        self.logo_label.image = logo_photo
        self.logo_label.pack(pady=(10, 0))

        # Mode gelap / terang
        self.theme = "darkly"
        self.toggle_button = ttk.Button(
            root, text="🌙 Dark Mode", bootstyle="secondary", command=self.toggle_theme
        )
        self.toggle_button.pack(pady=(0, 10))

        self.expression = ""
        self.display_var = ttk.StringVar()
        self.display = ttk.Entry(
            root, textvariable=self.display_var,
            font=('Helvetica', 24), justify='right',
            bootstyle="success"
        )
        self.display.pack(fill=X, padx=15, pady=15)

        # Tombol
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = ttk.Frame(root)
            frame.pack(fill=X, padx=10)
            for btn in row:
                button = ttk.Button(
                    frame, text=btn,
                    width=8, bootstyle="dark" if btn not in "=C" else ("danger" if btn == 'C' else "success"),
                    command=lambda b=btn: self.button_click(b)
                )
                button.pack(side=LEFT, expand=True, fill=X, padx=3, pady=3)

                # Hover animasi
                button.bind("<Enter>", lambda e, b=button: b.configure(bootstyle="info"))
                button.bind("<Leave>", lambda e, b=button, t=btn: b.configure(
                    bootstyle="dark" if t not in "=C" else ("danger" if t == 'C' else "success")
                ))

    def toggle_theme(self):
        # Toggle antara light dan dark mode
        if self.theme == "darkly":
            self.theme = "flatly"
            self.root.style.theme_use("flatly")
            self.toggle_button.config(text="☀️ Light Mode")
        else:
            self.theme = "darkly"
            self.root.style.theme_use("darkly")
            self.toggle_button.config(text="🌙 Dark Mode")

    def button_click(self, char):
        self.play_sound()

        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
            except:
                self.expression = "ERROR"
        else:
            self.expression += str(char)

        self.display_var.set(self.expression)

    def play_sound(self):
        try:
            self.click_sound.play()
        except:
            pass

# Run
if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = KalkulatorApp(root)
    #root.iconbitmap("icon.ico")  # pastikan file ada
    root.mainloop()
