from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from tkinter.font import Font, families
from tkinter.colorchooser import askcolor
from tkinter.scrolledtext import *
from tkinter import Scrollbar, Text, messagebox, Menu, ttk
import time

class File(): ## File menu
    def newFile(self):
        self.filename = "Untitled"
        self.text.delete(0.0, END)
        self.status_bar.config(text = "New file open  ")
        self.root.title("Notepy - " + self.filename)

    def saveFile(self):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
            self.status_bar.config(text = "File saved  ")
        except:
            self.saveAs()

    def saveAs(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Error", message="Unable to save file...")

    def openFile(self):
        f = askopenfile(mode='r')
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)
        self.status_bar.config(text = "File opened  ")
        self.root.title("Notepy - " + self.filename)

    def quit(self):
        entry = askyesno(title="Quit", message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, root, status_bar):
        self.filename = None
        self.text = text
        self.root = root
        self.status_bar = status_bar

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

    def __init__(self, text, root, status_bar):
        self.clipboard = None
        self.text = text
        self.rightClick = Menu(root)
        self.status_bar = status_bar

class Format():
    def __init__(self, text):
        self.text = text

    def changeBg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(bg=hexstr)

    def changeFg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.text.config(fg=hexstr)

    def bold(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "bold" in current_tags:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.text, self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold", font=bold_font)
        except:
            pass

    def italic(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "italic" in current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except:
            pass

    def underline(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "underline" in current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except:
            pass

    def overstrike(self, *args):  # Works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "overstrike" in current_tags:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.text, self.text.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.text.tag_configure("overstrike", font=overstrike_font)
        except:
            pass

    def addDate(self):
        full_date = time.localtime()
        day = str(full_date.tm_mday)
        month = str(full_date.tm_mon)
        year = str(full_date.tm_year)
        date = day + '/' + month + '/' + year
        self.text.insert(INSERT, date, "a")

def showAbout():
    messagebox.showinfo("About Notepy", "Notepy\n By Mirko Rovere")


root = Tk()

root.title("Notepy")
root.geometry("1200x600")
root.minsize(width=600, height=600)
root.iconbitmap("notepy.ico")

status_bar = Label(root, text = 'Ready   ', anchor = E)
status_bar.pack( fill = "x", side = "bottom", ipady = 4 ) 

scrollbar = Scrollbar(root, bg = "grey")
scrollbar.pack( side = RIGHT, fill = Y)

text = Text(root, state='normal', width=400, height=400, wrap='word', pady=2, padx=3, undo=True, selectbackground = "yellow", selectforeground = "black",)
text.pack(fill=Y, expand=1)
text.config(yscrollcommand= scrollbar.set)
text.focus_set()

scrollbar.config(command = text.yview)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=False) ## File menu gui
objFile = File(text, root, status_bar)
filemenu.add_command(label=" New" , command=objFile.newFile)
filemenu.add_command(label=" Open ", command=objFile.openFile)
filemenu.add_command(label=" Save ", command=objFile.saveFile)
filemenu.add_command(label=" Save As ", command=objFile.saveAs)
filemenu.add_separator()
filemenu.add_command(label=" Exit ", command=objFile.quit)
menubar.add_cascade(label=" File ", menu=filemenu)

editmenu = Menu(menubar, tearoff=False) # Edit menu gui
objEdit = Edit(text, root, status_bar)
editmenu.add_command(label="Copy", command=objEdit.copy, accelerator="Ctrl+C")
editmenu.add_command(label="Cut", command=objEdit.cut, accelerator="Ctrl+X")
editmenu.add_command(label="Paste", command=objEdit.paste, accelerator="Ctrl+V")
editmenu.add_command(label="Undo", command=objEdit.undo, accelerator="Ctrl+Z")
editmenu.add_command(label="Redo", command=objEdit.redo, accelerator="Ctrl+Y")
editmenu.add_command(label="Find", command=objEdit.find, accelerator="Ctrl+F")
editmenu.add_separator()
editmenu.add_command(label="Select All", command=objEdit.selectAll, accelerator="Ctrl+A")
menubar.add_cascade(label="Edit", menu=editmenu)

#Some edit menu keyboard shortcut
root.bind_all("<Control-z>", objEdit.undo)
root.bind_all("<Control-y>", objEdit.redo)
root.bind_all("<Control-f>", objEdit.find)
root.bind_all("Control-a", objEdit.selectAll)

#Show little actions menu on right Click
objEdit.rightClick.add_command(label="Copy", command=objEdit.copy)
objEdit.rightClick.add_command(label="Cut", command=objEdit.cut)
objEdit.rightClick.add_command(label="Paste", command=objEdit.paste)
objEdit.rightClick.add_separator()
objEdit.rightClick.add_command(label="Select All", command=objEdit.selectAll)
objEdit.rightClick.bind("<Control-q>", objEdit.selectAll)

objFormat = Format(text)

fontoptions = families(root)
font = Font(family="Arial", size=10)
text.configure(font=font)

formatMenu = Menu(menubar, tearoff=False)


fsubmenu = Menu(formatMenu, tearoff=False) #Fonts submenu
ssubmenu = Menu(formatMenu, tearoff=False) #Font size submenu

for option in fontoptions:
    fsubmenu.add_command(label=option, command=lambda option=option: font.configure(family=option))
for value in range(1, 31):
    ssubmenu.add_command(label=str(value), command=lambda value=value: font.configure(size=value))


formatMenu.add_command(label="Change Background", command=objFormat.changeBg)
formatMenu.add_command(label="Change Font Color", command=objFormat.changeFg)
formatMenu.add_cascade(label="Font", underline=0, menu=fsubmenu)
formatMenu.add_cascade(label="Size", underline=0, menu=ssubmenu)
formatMenu.add_command(label="Bold", command=objFormat.bold, accelerator="Ctrl+B")
formatMenu.add_command(label="Italic", command=objFormat.italic, accelerator="Ctrl+I")
formatMenu.add_command(label="Underline", command=objFormat.underline, accelerator="Ctrl+U")
formatMenu.add_command(label="Overstrike", command=objFormat.overstrike, accelerator="Ctrl+T")
formatMenu.add_command(label="Add Date", command=objFormat.addDate)
menubar.add_cascade(label="Format", menu=formatMenu)

#Some format menu keyboard shortcut
root.bind_all("<Control-b>", objFormat.bold)
root.bind_all("<Control-i>", objFormat.italic)
root.bind_all("<Control-u>", objFormat.underline)
root.bind_all("<Control-T>", objFormat.overstrike)

root.grid_columnconfigure(0, weight=1)
root.resizable(True, True)

helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label = 'About', command = showAbout)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
