import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import pygame
import os

class KalkulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Keren")
        self.root.geometry("400x560")
        self.root.resizable(False, False)

        # Init pygame untuk suara
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("Asset/click.mp3")

        # Simbol yang ditampilkan vs simbol asli
        self.symbol_map = {'×': '*', ':': '/'}

        # Logo
        logo_img = Image.open("Asset/logo.png").resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_img)
        self.logo_label = ttk.Label(root, image=logo_photo)
        self.logo_label.image = logo_photo
        self.logo_label.pack(pady=(10, 0))

        # Tombol dark mode toggle
        self.theme = "darkly"
        self.toggle_btn = ttk.Button(root, text="🌙 Dark Mode", bootstyle="secondary", command=self.toggle_theme)
        self.toggle_btn.pack(pady=(5, 10))

        self.expression = ""
        self.display_var = ttk.StringVar()

        self.display = ttk.Entry(
            root, textvariable=self.display_var,
            font=("Helvetica", 24), justify='right',
            bootstyle="success"
        )
        self.display.pack(fill=X, padx=15, pady=15, ipady=10)

        # Tombol-tombol kalkulator
        buttons = [
            ['7', '8', '9', ':'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '-'],
            ['0', '.', '⌫', '+'],
            ['C', '=']
        ]

        for row in buttons:
            frame = ttk.Frame(root)
            frame.pack(fill=X, padx=10)
            for btn in row:
                style = "dark"
                if btn == 'C':
                    style = "danger"
                elif btn == '=':
                    style = "success"
                elif btn == '⌫':
                    style = "warning"

                button = ttk.Button(
                    frame, text=btn, width=8,
                    bootstyle=style,
                    command=lambda b=btn: self.button_click(b)
                )
                button.pack(side=LEFT, expand=True, fill=X, padx=3, pady=5)

                # Hover efek
                button.bind("<Enter>", lambda e, b=button: b.configure(bootstyle="info"))
                button.bind("<Leave>", lambda e, b=button, t=btn: b.configure(
                    bootstyle="dark" if t not in "=C⌫" else (
                        "danger" if t == 'C' else
                        "success" if t == '=' else
                        "warning"
                    )
                ))

        # Label Pembuat
        credit_label = ttk.Label(
            root,
            text="Dibuat oleh Faiq Naufal | FallSec-tech © 2025",
            font=("Helvetica", 9, "italic"),
            bootstyle="secondary"
        )
        credit_label.pack(pady=(5, 10))

    def toggle_theme(self):
        if self.theme == "darkly":
            self.theme = "flatly"
            self.toggle_btn.config(text="☀️ Light Mode")
        else:
            self.theme = "darkly"
            self.toggle_btn.config(text="🌙 Dark Mode")

        self.root.style.theme_use(self.theme)

    def button_click(self, char):
        self.play_sound()

        if char in self.symbol_map:
            char = self.symbol_map[char]

        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
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

# Run App
if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = KalkulatorApp(root)
    if os.path.exists("icon.ico"):
        root.iconbitmap("icon.ico")
    root.mainloop()
