from tkinter import Menu, messagebox
from submenu import format_menu, edit_menu, revision_menu

def main(root, text, menubar, status_bar):

    objEdit = edit_menu.Edit(text, root, status_bar)
    objFormat = format_menu.Format(text)
    objRevision = revision_menu.Revision(text, status_bar)

    m = Menu(root, tearoff = 0) #menu rightclick
    m.add_command(label ="Cut", command=objEdit.cut)
    m.add_command(label ="Copy", command=objEdit.copy)
    m.add_command(label ="Paste", command=objEdit.paste)
    m.add_command(label="Find", command=objEdit.find)
    m.add_command(label="Add Date", command=objFormat.addDate)
    m.add_command(label="Add Hour", command=objFormat.addHour)
    m.add_command(label="Search on internet", command=objRevision.open_webb)
    m.add_command(label="Num to words", command=objRevision.numtowords)

    def do_popup(event):
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()

    text.bind("<Button-3>", do_popup)

if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
