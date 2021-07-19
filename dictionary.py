from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from tkinter import Scrollbar, Text, messagebox, Menu
import ety


class Dictionary():

    def __init__(self, text):
        self.text = text

    def etymology(self):
        entry = messagebox.askyesno("Warning", "This function work only in english\nContinue?")

        if entry == True:
            if self.text.tag_ranges(SEL):
                a = ety.tree(self.text.get(SEL_FIRST, SEL_LAST))
                messagebox.showinfo("etymology of the word", str(a))

            else:
                messagebox.showerror("Error", "No text selected")


def main(root, text, menubar):

    objDictionary = Dictionary(text)
    dictionarymenu = Menu(root, tearoff=False)

    dictionarymenu.add_command(label="Etymology of the word", command=objDictionary.etymology)

    menubar.add_cascade(label=" Dictionary ", menu=dictionarymenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
