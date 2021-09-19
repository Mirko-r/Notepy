from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from tkinter import Scrollbar, Text, messagebox, Menu

class Edit(): # Edit menu

    def copy(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel
        self.status_bar.config(text = "Copied to clipboard  ")

    def cut(self, *args):
        sel = self.text.selection_get()
        self.clipboard = sel
        self.text.delete(SEL_FIRST, SEL_LAST)
        self.status_bar.config(text = "Cutted  ")

    def paste(self, *args):
        self.text.insert(INSERT, self.clipboard)
        self.status_bar.config(text = "Ready  ")

    def selectAll(self, *args):
        self.text.tag_add(SEL, "1.0", END)
        self.text.mark_set(0.0, END)
        self.text.see(INSERT)
        self.status_bar.config(text = "Ready  ")

    def delete_all(self, *args):
	    self.text.delete(1.0, END)

    def undo(self, *args):
        self.text.edit_undo()
        self.status_bar.config(text = "Undo  ")

    def redo(self, *args):
        self.text.edit_redo()
        self.status_bar.config(text = "Redo  ")

    def find(self, *args):
        self.text.tag_remove('found', '1.0', END)
        target = askstring('Find', 'Search String:')
        if target:
            idx = '1.0'
            while 1:
                idx = self.text.search(target, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(target))
                self.text.tag_add('found', idx, lastidx)
                idx = lastidx
            self.text.tag_config('found', foreground='white', background='blue')
            self.status_bar.config(text = "Matched search in blue  ")

    def uppercase(self, *args):
        if self.text.tag_ranges(SEL):
            a = self.text.get(SEL_FIRST, SEL_LAST)
            self.text.delete(SEL_FIRST, SEL_LAST)
            a = a.upper()
            self.text.insert(INSERT, a)
            self.status_bar.config(text = "Uppercase  ")
        else:
            messagebox.showerror("Uppercase", "no text selected")

    def capitalize(self):
        if self.text.tag_ranges(SEL):
            a = self.text.get(SEL_FIRST, SEL_LAST)
            self.text.delete(SEL_FIRST, SEL_LAST)
            a = a.capitalize()
            self.text.insert(INSERT, a)
            self.status_bar.config(text = "Capitalized  ")
        else:
            messagebox.showerror("Capitalize", "no text selected")

    def lowercase(self):
        if self.text.tag_ranges(SEL):
            a = self.text.get(SEL_FIRST, SEL_LAST)
            self.text.delete(SEL_FIRST, SEL_LAST)
            a = a.lower()
            self.text.insert(INSERT, a)
            self.status_bar.config(text = "Lowercase  ")
        else:
            messagebox.showerror("Lowercase", "no text selected")

    def reverse(self):
        if self.text.tag_ranges(SEL):
            rtext = self.text.get(SEL_FIRST, SEL_LAST)[::-1]
            rtext.replace('\0', '', 1)
            self.text.delete(SEL_FIRST, SEL_LAST)
            self.text.insert(INSERT, rtext)
            self.status_bar.config(text = "Reversed  ")
        else:
            messagebox.showerror("Reverse", "no text selected")

    def __init__(self, text, root, status_bar):
        self.clipboard = None
        self.text = text
        self.rightClick = Menu(root)
        self.status_bar = status_bar

def main(root, text, menubar, status_bar):
    editmenu = Menu(menubar, tearoff=False) # Edit menu gui
    objEdit = Edit(text, root, status_bar)
    editmenu.add_command(label="Copy", command=objEdit.copy)
    editmenu.add_command(label="Cut", command=objEdit.cut)
    editmenu.add_command(label="Paste", command=objEdit.paste)
    editmenu.add_separator()
    editmenu.add_command(label="Undo", command=objEdit.undo)
    editmenu.add_command(label="Redo", command=objEdit.redo)
    editmenu.add_command(label="Find", command=objEdit.find)
    editmenu.add_separator()
    editmenu.add_command(label="Uppercase", command=objEdit.uppercase)
    editmenu.add_command(label="Lowercase", command=objEdit.lowercase)
    editmenu.add_command(label="Capitalize", command=objEdit.capitalize)
    editmenu.add_separator()
    editmenu.add_command(label="Select All", command=objEdit.selectAll)
    editmenu.add_command(label="Delete All", command=objEdit.delete_all)
    editmenu.add_separator()
    editmenu.add_command(label="Reverse", command=objEdit.reverse)
    menubar.add_cascade(label="Edit", menu=editmenu)
    root.config(menu=menubar)

    #Edit menu keyboard shortcut
    root.bind_all("<Control-y>", objEdit.undo)
    root.bind_all("<Control-z>", objEdit.redo)
    root.bind_all("<Control-f>", objEdit.find)
    root.bind_all("Control-a", objEdit.selectAll)
    root.bind_all("<Control-d>", objEdit.delete_all)
    root.bind_all("<Control-Shift-KeyPress-U>", objEdit.uppercase)

if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
