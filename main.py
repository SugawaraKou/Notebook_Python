from tkinter import *
from tkinter import Menu, filedialog, messagebox
import tkinter as tk
from tkinter.ttk import Combobox
import tkinter.font as tkFont


def open_file():
    Ofile = filedialog.askopenfilename()

    if not Ofile:
        messagebox.showerror("Error", "Error Open File")
        return

    text_edit.delete("1.0", tk.END)
    with open(Ofile, "r") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)
    window.title(Ofile)


def save_file():
    with open(window.title(), "w") as out:
        text = text_edit.get("1.0", END)
        out.write(text)


def save_as_file():
    Sfile = filedialog.asksaveasfilename(
        filetypes=(("Text", "*.txt"), ("all file", "*.*"))
    )

    if not Sfile:
        messagebox.showerror("Error", "Error Save File")
        return

    with open(Sfile, "w") as output_file:
        text = text_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(Sfile)


def settings_background_change():
    text_edit.config(bg=combo.get(), fg=combo2.get())
    fontExample = tkFont.Font(family=combo3.get(), size=spin.get())
    text_edit.configure(font=fontExample)


def settings():
    set = Tk()
    set.title("Settings")

    lbl = Label(set, text="Background color:")
    lbl.grid(column=0, row=0)

    global combo
    combo = Combobox(set)
    combo["values"] = ["Black", "White"]
    combo.current(0)
    combo.grid(column=1, row=0)

    lbl = Label(set, text="Text color:")
    lbl.grid(column=0, row=1)

    global combo2
    combo2 = Combobox(set)
    combo2["values"] = ["Black", "White", "Grey", "Red", "Green", "Purple"]
    combo2.current(1)
    combo2.grid(column=1, row=1)

    lbl = Label(set, text="Font size:")
    lbl.grid(column=0, row=2)

    global spin
    spin = Spinbox(set, from_=10, to=100, width=10, textvariable=100)
    spin.grid(column=1, row=2)

    lbl = Label(set, text="Font:")
    lbl.grid(column=0, row=3)

    global combo3
    combo3 = Combobox(set)
    combo3["values"] = ["Arial", "Calibri", "Times New Roman", "Ubuntu", "System", "Terminal", "Segoe Script"]
    combo3.current(1)
    combo3.grid(column=1, row=3)

    btn = Button(set, text="To apply", command=settings_background_change)
    btn.grid(column=0, row=4)

    set.mainloop()


window = Tk()
window.geometry("600x400")
window.title("Notebook")

"""
#Notebook
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text="untitled")
tab_control.pack(expand=1, fill="both")
"""

# Menu
menu = Menu()
new_item = Menu(menu, tearoff=0)

new_item.add_command(label="Open file", command=open_file)
new_item.add_command(label="Save file", command=save_file)
new_item.add_command(label="Save as file", command=save_as_file)
new_item.add_command(label="Settings", command=settings)
new_item.add_command(label="Exit", command=exit)

menu.add_cascade(label="File", menu=new_item)
window.config(menu=menu)

# Text
text_edit = Text(bg="black", fg="white")
text_edit.pack()

window.mainloop()
