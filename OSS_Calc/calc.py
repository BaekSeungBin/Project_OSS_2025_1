import tkinter as tk

def add_commas(number_str):
    try:
        if "." in number_str:
            integer, dot, decimal = number_str.partition(".")
            num = int(integer.replace(",", ""))
            formatted = "{:,}".format(num)
            return formatted + dot + decimal
        else:
            num = int(number_str.replace(",", ""))
            return "{:,}".format(num)
    except:
        return number_str

def remove_commas(number_str):
    return number_str.replace(",", "")

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

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                result = str(eval(remove_commas(self.expression)))
                self.expression = add_commas(result)
            except Exception:
                self.expression = "에러"
        else:
            temp = remove_commas(self.expression)
            temp += str(char)
            if char in '+-*/.':
                self.expression = temp
            else:
                parts = []
                num = ''
                for c in temp:
                    if c in '+-*/':
                        if num:
                            parts.append(add_commas(num))
                            num = ''
                        parts.append(c)
                    else:
                        num += c
                if num:
                    parts.append(add_commas(num))
                self.expression = ''.join(parts)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
