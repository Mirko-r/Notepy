from tkinter.constants import Y
from tkinter.filedialog import *
import tkinter as tk
from tkinter import Scrollbar, Text, messagebox, Menu

def saveFileAs():
    new_file = asksaveasfile(mode = 'w', filetypes = (("Text files","*.txt"),("all files","*.*")))
    if new_file is None:
        return
    text = str(entry.get(1.0, tk.END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '*')])
    if file is not None:
        content = file.read()
    entry.insert(tk.INSERT, content)

def showAbout():
    messagebox.showinfo("Notepy", "Notepy\n\nBy Mirko Rovere")

canvas = tk.Tk()
canvas.geometry("600x700")
canvas.config(bg = "white")
canvas.title("Notepy")

top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

scrollbar = Scrollbar(canvas, bg = "grey")
scrollbar.pack( side = "right", fill = "y")

entry = tk.Text(canvas, wrap = tk.WORD, bg = "white", font = ("Colibri", 15))
entry.pack(padx = 10, pady = 5, expand = tk.TRUE, fill = tk.BOTH)
entry.config(yscrollcommand= scrollbar.set)

scrollbar.config(command = entry.yview)

menu = Menu(canvas)

new_item = Menu(menu)
new_item.add_command(label = 'Open', command = openFile)
new_item.add_separator()
new_item.add_command(label = 'Save as', command = saveFileAs)
menu.add_cascade(label ='File', menu = new_item)


menu.add_command(label = 'About', command = showAbout)

menu.add_command(label = 'Exit', command = canvas.destroy)

canvas.config(menu=menu)
canvas.mainloop()