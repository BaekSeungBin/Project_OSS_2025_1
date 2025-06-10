import tkinter as tk
import qrcode
from PIL import Image, ImageTk
import io

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        qr_button = tk.Button(
            root,
            text="QR코드",
            font=("Arial", 14),
            command=self.show_qr
        )
        qr_button.pack(pady=5)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def show_qr(self):
        data = self.entry.get()
        if not data or data == "에러":
            return
        qr_img = qrcode.make(data)
        with io.BytesIO() as output:
            qr_img.save(output, format="PNG")
            img_data = output.getvalue()
        top = tk.Toplevel(self.root)
        top.title("QR 코드")
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(img)
        label = tk.Label(top, image=tk_img)
        label.image = tk_img
        label.pack(padx=10, pady=10)

