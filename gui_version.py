import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # To copy the password to the clipboard

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text="Password Length:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.length_var).pack(pady=5)

        tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.uppercase_var).pack(pady=5)
        tk.Checkbutton(self.root, text="Include Numbers", variable=self.numbers_var).pack(pady=5)
        tk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var).pack(pady=5)

        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)

        self.password_display = tk.Entry(self.root, font=("Arial", 14), width=30, justify='center')
        self.password_display.pack(pady=10)

        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        include_uppercase = self.uppercase_var.get()
        include_numbers = self.numbers_var.get()
        include_symbols = self.symbols_var.get()

        password = self.create_password(length, include_uppercase, include_numbers, include_symbols)
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

        # Clear the input field and reset checkboxes
        self.length_var.set(12)  # Reset to default length
        self.uppercase_var.set(True)
        self.numbers_var.set(True)
        self.symbols_var.set(True)

    def create_password(self, length, include_uppercase, include_numbers, include_symbols):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if include_uppercase else ''
        numbers = string.digits if include_numbers else ''
        symbols = string.punctuation if include_symbols else ''

        all_characters = lower + upper + numbers + symbols

        if not all_characters:
            return "Error: No character types selected!"

        return ''.join(random.choice(all_characters) for _ in range(length))

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
