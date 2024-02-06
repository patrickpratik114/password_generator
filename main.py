import tkinter as tk
import random
import string


def generate_password():
    length = int(length_entry.get())
    characters = ""
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    password = "".join(random.choice(characters) for i in range(length))
    password_label.config(text=password)


root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

lowercase_var = tk.IntVar()
lowercase_checkbox = tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var)
lowercase_checkbox.grid(row=1, column=0)

uppercase_var = tk.IntVar()
uppercase_checkbox = tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=1)

numbers_var = tk.IntVar()
numbers_checkbox = tk.Checkbutton(root, text="Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0)

symbols_var = tk.IntVar()
symbols_checkbox = tk.Checkbutton(root, text="Symbols", variable=symbols_var)
symbols_checkbox.grid(row=2, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2)

password_label = tk.Label(root, text="")
password_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
