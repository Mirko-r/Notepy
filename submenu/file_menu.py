from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from tkinter import Scrollbar, Text, messagebox, Menu
import os

class File(): ## File menu

    def newFile(self, *args):
        self.filename = "Untitled"
        self.text.delete(0.0, END)
        self.status_bar.config(text = "New file open  ")
        self.root.title("Notepy - " + self.filename)

    def saveFile(self, *args):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
            self.status_bar.config(text = "File saved  ")
        except:
            self.saveAs()

    def saveAs(self, *args):
        f = asksaveasfile(
                    mode="w",
                    initialfile="Untitled.txt",
                    defaultextension=".txt",
                    filetypes=[
                        ("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Aspnetcorerazor", "*.cshtml;*.razor"),
                        ("Batch", "*.bat;*.cmd"),
                        ("C", "*.c;*.i"),
                        ("C#", "*.cs;*.csx;*.cake"),
                        ("C++", "*.cpp;*.cc;*.cxx;*.c++;*.hpp;*.hh;*.hxx;*.h++;*.h;*.ii"),
                        ("Clojure", "*.clj;*.cljs;*.cljc;*.cljx;*.clojure;*.edn"),
                        ("CoffeeScript", "*.coffee;*.cson;;*.iced"),
                        ("CSCS", "*.cscs;*.mqs"),
                        ("CSS", "*.css"),
                        ("CUDA C++", "*.cu;*.cuh"),
                        ("Dart", "*.dart"),
                        ("Diff", "*.diff;*.patch;*.rej"),
                        ("Docker", "*.dockerfile;*.containerfile"),
                        ("F#", "*.fs;*.fsx;*.fsi;*.fsscript"),
                        ("Go", "*.go"),
                        ("Go Checksum File", "*.go.sum"),
                        ("Go Module File", "*.go.mod;*.gopls.mod"),
                        ("Groovy", "*.groovy;*.gvy;*.gradle;*.jenkinsfile;*.nf"),
                        ("Handlebars", "*.handlebars;*.hbs;*.hjs"),
                        ("HLSL", "*.hlsl;*.hlsli;*.fx;*.fxh;*.vsh;*.psh;*.cginc;*.compute"),
                        ("HTML", "*.html;*.htm;*.shtml;*.xhtml;*.xht;*.mdoc;*.jsp;*.asp;*.aspx;*.jshtm"),
                        ("Ignore", "*.gitignore_global;*.gitignore;*.npmignore"),
                        ("Ini", "*.ini"),
                        ("Java", "*.java;*.class;*.jav"),
                        ("JavaScript", "*.js;*.es6;*.*mjs;*.cjs;*.pac"),
                        ("JavaScript React", "*.jsx"),
                        ("Jinja", "*.jinjia2;*.j2"),
                        ("Json", "*.json;*.bowerrc;*.jscsrc;*.webmanifest;*.js.map;*.css.map;*.ts.map;*.har;*.jslintrc;*.jsonld"),
                        ("JSON with Comments", "*.jsonc;*.eslintrc;*.eslintrc.json;*.jsfmtrc;*.jshintrc;*.srcrc;*.hintrc;*.babelrc;*.code-workspace;*.language-configuration.json"),
                        ("Julia", "*.jl"),
                        ("Julia Markdown", "*.jmd"),
                        ("Jupyter", "*.ipynb"),
                        ("Less", "*.less"),
                        ("Log", "*.log;*.log.?"),
                        ("Lua", "*.lua"),     
                    ],
                )
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
            self.status_bar.config(text = "File saved  ")
        except:
            showerror(title="Error", message="Unable to save file...")

    def openFile(self, *args):
        f = askopenfile(
                defaultextension=".txt",
                filetypes=[
                        ("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Aspnetcorerazor", "*.cshtml;*.razor"),
                        ("Batch", "*.bat;*.cmd"),
                        ("C", "*.c;*.i"),
                        ("C#", "*.cs;*.csx;*.cake"),
                        ("C++", "*.cpp;*.cc;*.cxx;*.c++;*.hpp;*.hh;*.hxx;*.h++;*.h;*.ii"),
                        ("Clojure", "*.clj;*.cljs;*.cljc;*.cljx;*.clojure;*.edn"),
                        ("CoffeeScript", "*.coffee;*.cson;;*.iced"),
                        ("CSCS", "*.cscs;*.mqs"),
                        ("CSS", "*.css"),
                        ("CUDA C++", "*.cu;*.cuh"),
                        ("Dart", "*.dart"),
                        ("Diff", "*.diff;*.patch;*.rej"),
                        ("Docker", "*.dockerfile;*.containerfile"),
                        ("F#", "*.fs;*.fsx;*.fsi;*.fsscript"),
                        ("Go", "*.go"),
                        ("Go Checksum File", "*.go.sum"),
                        ("Go Module File", "*.go.mod;*.gopls.mod"),
                        ("Groovy", "*.groovy;*.gvy;*.gradle;*.jenkinsfile;*.nf"),
                        ("Handlebars", "*.handlebars;*.hbs;*.hjs"),
                        ("HLSL", "*.hlsl;*.hlsli;*.fx;*.fxh;*.vsh;*.psh;*.cginc;*.compute"),
                        ("HTML", "*.html;*.htm;*.shtml;*.xhtml;*.xht;*.mdoc;*.jsp;*.asp;*.aspx;*.jshtm"),
                        ("Ignore", "*.gitignore_global;*.gitignore;*.npmignore"),
                    ],
            )
        self.filename, file_extension = os.path.splitext(f.name)
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)
        self.status_bar.config(text = "File opened  extension : "+file_extension)
        self.root.title("Notepy - " + self.filename)
        
    def quit(self, *args):
        entry = askyesno(title="Quit", message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, root, status_bar):
        self.filename = None
        self.text = text
        self.root = root
        self.status_bar = status_bar

def main(root, text, menubar, status_bar):
    filemenu = Menu(menubar, tearoff=False) ## File menu gui
    objFile = File(text, root, status_bar)
    filemenu.add_command(label=" New" , command=objFile.newFile)
    filemenu.add_command(label=" Open ", command=objFile.openFile)
    filemenu.add_command(label=" Save ", command=objFile.saveFile)
    filemenu.add_command(label=" Save As ", command=objFile.saveAs)
    filemenu.add_separator()
    filemenu.add_command(label=" Exit ", command=objFile.quit)
    menubar.add_cascade(label=" File ", menu=filemenu)
    root.config(menu=menubar)

    #File menu keyboard shortcut
    root.bind_all("<Control-n>", objFile.newFile)
    root.bind_all("<Control-o>", objFile.openFile)
    root.bind_all("<Control-s>", objFile.saveFile)
    root.bind_all("<Control-q>", objFile.quit)

if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
