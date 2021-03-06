from tkinter import *
from tkinter import Menu, filedialog
from tkinter import ttk


def open_file():
    Ofile = filedialog.askopenfilename()

    if not Ofile:
        return

    text_edit.delete("1.0", END)
    with open(Ofile, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
    tab_control.add(ttk.Frame(tab_control), text=Ofile)
    tab_control.title(f"Simple Text Editor - {Ofile}")


def save_file():
    pass


def save_as_file():
    Sfile = filedialog.asksaveasfilename(
        filetypes=(("Text", "*.txt"), ("all file", "*.*"))
    )

    if not Sfile:
        return

    with open(Sfile, "w") as output_file:
        text = text_edit.get("1.0", END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {Sfile}")



window = Tk()
#window.geometry("800x600")
window.title("Notebook")

#Notebook
tab_control = ttk.Notebook(window)

tab_control.add(ttk.Frame(tab_control), text="untitled")
tab_control.pack(expand=1, fill="both")

# Menu
menu = Menu()
new_item = Menu(menu, tearoff=0)

new_item.add_command(label="Open file", command=open_file)
new_item.add_command(label="Save file", command=save_file)
new_item.add_command(label="Save as file", command=save_as_file)
new_item.add_command(label="Exit", command=exit)

menu.add_cascade(label="File", menu=new_item)
window.config(menu=menu)

# Text
text_edit = Text()
text_edit.pack()

window.mainloop()
