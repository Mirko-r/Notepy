from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from idlelib.percolator import Percolator
from idlelib.colorizer import ColorDelegator
from submenu import file_menu, format_menu, edit_menu, revision_menu, help_menu

root = Tk()

root.title("Notepy")
root.geometry("1200x600")
root.minsize(width=600, height=600)
root.iconbitmap("notepy.ico")
status_bar = Label(root, text = 'Ready   ', anchor = E)
status_bar.pack( fill = "x", side = "bottom", ipady = 4 ) 

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y)

text = Text(root, state='normal', width=400, height=400, wrap='word', pady=2, padx=3, undo=True, selectbackground = "yellow", selectforeground = "black",)
text.pack(fill=Y, expand=1)
text.config(yscrollcommand= scrollbar.set)
text.focus_set()
scrollbar.config(command = text.yview)

menubar = Menu(root)

file_menu.main(root, text, menubar, status_bar)
objFile = file_menu.File(text, root, status_bar)

edit_menu.main(root, text, menubar, status_bar)
objEdit = edit_menu.Edit(text, root, status_bar)

format_menu.main(root, text, menubar, status_bar)
objFormat = format_menu.Format(text)

revision_menu.main(root, text, menubar, status_bar)
objRevision = revision_menu.Revision(text, status_bar)

help_menu.main(root, text, menubar)

Percolator(text).insertfilter(ColorDelegator())
root.grid_columnconfigure(0, weight=1)
root.resizable(True, True)

m = Menu(root, tearoff = 0) #menu rightclick
m.add_command(label ="Cut", command=objEdit.cut)
m.add_command(label ="Copy", command=objEdit.copy)
m.add_command(label ="Paste", command=objEdit.paste)
m.add_command(label="Find", command=objEdit.find)
m.add_command(label="Add Date", command=objFormat.addDate)
m.add_command(label="Add Hour", command=objFormat.addHour)
m.add_command(label="Search on internet", command=objRevision.open_webb)

def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

text.bind("<Button-3>", do_popup)

#Format menu keyboard shortcut
root.bind_all("<Control-b>", objFormat.bold)
root.bind_all("<Control-i>", objFormat.italic)
root.bind_all("<Control-u>", objFormat.underline)
root.bind_all("<Control-t>", objFormat.overstrike)

#Edit menu keyboard shortcut
root.bind_all("<Control-y>", objEdit.undo)
root.bind_all("<Control-z>", objEdit.redo)
root.bind_all("<Control-f>", objEdit.find)
root.bind_all("Control-a", objEdit.selectAll)
root.bind_all("<Control-d>", objEdit.delete_all)

#File menu keyboard shortcut
root.bind_all("<Control-n>", objFile.newFile)
root.bind_all("<Control-o>", objFile.openFile)
root.bind_all("<Control-s>", objFile.saveFile)
root.bind_all("<Control-q>", objFile.quit)

root.mainloop()
