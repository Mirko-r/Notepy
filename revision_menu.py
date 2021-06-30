from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from tkinter import Scrollbar, Text, messagebox, Menu
from textblob import TextBlob
import readtime
import webbrowser

class Revision(): # Revision menu
    def __init__(self, text, status_bar):
        self.text = text
        self.status_bar = status_bar

    def words_count(self):
        t = self.text.get(0.0, END)
        words = [w for w in t.split(' ') if w!='\n']
        word_count = len(words)
        messagebox.showinfo("Word Count", "word count: {:,d}".format(word_count))
    
    def chars_count(self):
        text_var = self.text.get(1.0, END)
        word_list = text_var.split('\n')
        count = 0
        for x in word_list:
            if x != "":
                count += len(x)
        messagebox.showinfo("Character Count ", "characters count: {:,d}".format(count))

    def readtime(self):
        result = str(readtime.of_text(self.text.get(0.0, END)))
        messagebox.showinfo("Read Time", "Time :" + result)
    
    def correct(self):
        entry = askyesno(title="Correct text", message="This function work only in english\nThis function is a beta\nContinue aniway?")
        if entry == True:
            a = self.text.get(SEL_FIRST, SEL_LAST)
            if self.text.tag_ranges(SEL):
                b = TextBlob(a)
                corrected_text = str(b.correct())
                entry = askyesno(title="Correction", message="Suggest corrections :\n\n" + corrected_text + "\n\nContinue?")
                if entry == True:
                    self.text.delete(1.0, END)
                    self.text.insert(1.0, corrected_text)
                    self.status_bar.config(text = "Text corrected  ")
            else:
                messagebox.showerror("Error", "No text selected")

    def open_webb(self):
        op = self.text.get(SEL_FIRST, SEL_LAST)
        if self.text.tag_ranges(SEL):
            webbrowser.open(op)
        else:
            messagebox.showerror("Error", "No text selected")

def main(root, text, menubar, status_bar):
    revisionmenu = Menu(menubar, tearoff=False) ## Revision menu gui
    objRevision = Revision(text, status_bar)
    revisionmenu.add_command(label="Count Words", command=objRevision.words_count)
    revisionmenu.add_command(label="Count Characters", command=objRevision.chars_count)
    revisionmenu.add_command(label="Calculate read time", command=objRevision.readtime)
    revisionmenu.add_command(label="Search on Internet", command=objRevision.open_webb)
    revisionmenu.add_command(label="Correct text", command=objRevision.correct)
    menubar.add_cascade(label=" Revision ", menu=revisionmenu)
    root.config(menu=menubar)


if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
