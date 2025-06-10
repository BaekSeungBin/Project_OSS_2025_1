import tkinter as tk

MORSE_NUM_DICT = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-'   
}

def convert_number_to_morse(number_str):
    return ' '.join(MORSE_NUM_DICT.get(ch, ch) for ch in number_str)

def convert_morse_to_number(morse_str):
    morse_to_num = {v: k for k, v in MORSE_NUM_DICT.items()}
    parts = morse_str.strip().split(' ')
    result = ""
    for part in parts:
        if part in morse_to_num:
            result += morse_to_num[part]
        elif part in "+-*/":
            result += part
        elif part == "":
            continue
        else:
            result += part
    return result

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

        self.is_morse = False
        self.original_entry_content = ""
        morse_button = tk.Button(
            root,
            text="모스변환",
            font=("Arial", 14),
            command=self.toggle_morse
        )
        morse_button.pack(pady=5)
        self.morse_button = morse_button

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
        if getattr(self, "is_morse", False):
            self.is_morse = False
            self.morse_button.config(text="모스변환")

    def toggle_morse(self):
        if not self.is_morse:
            current_display = self.entry.get()
            if current_display != "에러":
                self.original_entry_content = current_display
                morse = convert_number_to_morse(current_display)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, morse)
                self.is_morse = True
                self.morse_button.config(text="숫자변환")
        else:
            morse_display = self.entry.get()
            restored = convert_morse_to_number(morse_display)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, restored)
            self.is_morse = False
            self.morse_button.config(text="모스변환")
