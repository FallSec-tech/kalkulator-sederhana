import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class KalkulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Keren")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        from PIL import Image, ImageTk
          # Load dan tampilkan logo
        logo_img = Image.open("Asset/logo.png")
        logo_img = logo_img.resize((100, 100))  # Ukuran bisa disesuaikan
        logo_photo = ImageTk.PhotoImage(logo_img)
        self.logo_label = ttk.Label(root, image=logo_photo)
        self.logo_label.image = logo_photo  # keep reference
        self.logo_label.pack(pady=(10, 0))


        self.expression = ""

        # Display
        self.display_var = ttk.StringVar()
        self.display = ttk.Entry(root, textvariable=self.display_var, font=('Helvetica', 20), justify='right', bootstyle="success")
        self.display.pack(fill=X, padx=10, pady=15)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for btn in row:
         button = ttk.Button(
           master=frame,
            text=btn,
            bootstyle="dark" if btn not in "=C" else ("danger" if btn == 'C' else "success"),
            command=lambda b=btn: self.button_click(b)
            )
        button.pack(side=LEFT, expand=True, fill=X, padx=3, pady=2)

        # 🔥 Tambahkan hover bind DI SINI (masih di dalam loop)
        button.bind("<Enter>", lambda e, b=button: b.configure(bootstyle="info"))
        button.bind("<Leave>", lambda e, b=button, t=btn: b.configure(
             bootstyle="dark" if t not in "=C" else ("danger" if t == 'C' else "success")
         ))



    def button_click(self, char):
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

# Jalankan Aplikasi
if __name__ == "__main__":
    root = ttk.Window(themename="flatly")  # kamu bisa ganti theme: darkly, flatly, cyborg, etc
    app = KalkulatorApp(root)
    root.iconbitmap("icon.ico")
    root.mainloop()
