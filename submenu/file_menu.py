from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import messagebox
from fpdf import FPDF
import os


class File():  # File menu

    def newFile(self, *args):
        if self.saved == 1:
            entry = askyesnocancel('File not saved', "You want to save?")
            if entry == True:
                self.saveFile()
            elif entry == False:
                pass
            else:
                return None
        self.filename = "Untitled"
        self.text.delete(0.0, END)
        self.status_bar.config(text="New file open  ")
        self.root.title("Notepy - " + self.filename)
        self.saved = 0

    def saveFile(self, *args):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
            self.status_bar.config(text="File saved  ")
            self.saved = 0
            self.root.title("Notepy - " + self.filename)
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
                        ("Makefile", "*.mak;*.mk"),
                        ("Markdown", "*.md;*.mkd;*.mdwn;*.mdown;*.markdown;*.markdn;*.mdtxt;*.mdtext;*.workbook"),
                        ("Objective-C", "*.m"),
                        ("Objective-C++", "*.mm"),
                        ("Perl", "*.pl;*.pm;*.pod;*.t;*.PL;*.psgi"),
                        ("Perl 6", "*.p6;*.pl6;*.pm6;*.nqp"),
                        ("PHP", "*.php;*.php4;*.php5;*.phtml;*.ctp"),
                        ("Powershell", "*.ps1;*.psm1;*.psd1;*.pssc;*.psrc"),
                        ("Properties", "*.properties;*.cfg;*.conf;*.directory;*.gitattributes;*.gitconfig;*.gitmodules;*.editorconfig;*.npmrc"),
                        ("Pug", "*.pug;*.jade"),
                        ("Python", "*.py;*.rpy;*.pyw;*.cpy;*.gyp;*.gypi;.*pyi;*.ipy"),
                        ("R", "*.r;*.rhistory;*.rprofile;*.rt"),
                        ("Razor", ".cshtml"),
                        ("Ribbon", "*.xml;*.xsd;*.ascx;*.atom;*.axml;*.axaml;*.bpmn;*.cpt;*.csl;*.csproj"),
                        ("Ruby", "*.rb;*.rbx;*.rjs;*.gemspec;*.rake;*.ru;*.erb;*.podspec;*.rbi"),
                        ("Rust", "*.rs"),
                        ("SCSS", "*.scss"),
                        ("Search Result", "*.code-search"),
                        ("ShaderLab", "*.shader"),
                        ("Shell Script", "*.sh;*.bash;*.bashrc;*.bash_aliases;*.bash_profile;*.bash_login;*.ebuild;*.profile;*.bash_logout;*.xprofile"),
                        ("SQL", "*.sql;*.dsql"),
                        ("Swift", "*.swift"),
                        ("TypeScript", "*.ts"),
                        ("TypeScript React", "*.tsx"),
                        ("vba", "*.bas;*.cls;*.frm;*.sht;*.wbk"),
                        ("VBScript", "*.vbs;*.vba;*.bas;*.vbe;*.wsf;*.wsc;*.acm;*.acr;*.acf"),
                        ("Visual Basic Application",
                         "*.cls;*.frm;*.bas;*.vbs;*.vb;*.brs"),
                        ("XSL", "*.xsl;*.xslt"),
                        ("YAML", "*.yml;*.eyaml;*.eyml;*.yaml"),
                        ("No Extension", "*."),
            ],
        )
        t = self.text.get(0.0, END)
        self.filename, file_extension = os.path.splitext(f.name)
        self.filename = f.name
        self.root.title("Notepy - " + self.filename)
        self.saved = 0
        language_name = file_extension
        if language_name == ".py":
            icon = PhotoImage(file='icons/language_icons/logo_python.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".c" or language_name == ".i":
            icon = PhotoImage(file='icons/language_icons/logo_c.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".cpp" or language_name == ".cc" or language_name == ".cxx" or language_name == ".c++" or language_name == ".hpp" or language_name == ".hh" or language_name == ".hxx" or language_name == ".h++" or language_name == ".h" or language_name == ".ii":
            icon = PhotoImage(file='icons/language_icons/logo_cpp.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".css":
            icon = PhotoImage(file='icons/language_icons/logo_css.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".html":
            icon = PhotoImage(file='icons/language_icons/logo_html.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".json" or language_name == ".jsonc":
            icon = PhotoImage(file='icons/language_icons/logo_json.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".lua":
            icon = PhotoImage(file='icons/language_icons/logo_lua.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".pl" or language_name == ".pm" or language_name == ".pod" or language_name == ".t" or language_name == ".PL" or language_name == ".psgi":
            icon = PhotoImage(file='icons/language_icons/logo_perl.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".rb" or language_name == ".rbx" or language_name == ".rjs" or language_name == "*.gemspec" or language_name == ".rake" or language_name == ".ru" or language_name == ".erb" or language_name == ".podspec" or language_name == ".rbi":
            icon = PhotoImage(file='icons/language_icons/logo_ruby.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".sh" or language_name == ".bash" or language_name == ".bashrc" or language_name == ".bash_aliases" or language_name == ".bash_profile" or language_name == ".bash_login" or language_name == ".ebuild" or language_name == ".profile" or language_name == ".bash_logout" or language_name == ".xprofile":
            icon = PhotoImage(file='icons/language_icons/logo_bash.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".bat" or language_name == ".cmd":
            icon = PhotoImage(file='icons/language_icons/logo_batch.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".coffee" or language_name == ".cson" or language_name == ".iced":
            icon = PhotoImage(
                file='icons/language_icons/logo_coffeescript.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".cs" or language_name == ".csx" or language_name == ".cake":
            icon = PhotoImage(file='icons/language_icons/logo_csharp.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".java" or language_name == ".class" or language_name == ".jav":
            icon = PhotoImage(file='icons/language_icons/logo_java.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".js" or language_name == ".cs6" or language_name == ".mjs" or language_name == ".cjs" or language_name == ".pac":
            icon = PhotoImage(file='icons/language_icons/logo_javascript.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".sql" or language_name == ".dsql":
            icon = PhotoImage(file='icons/language_icons/logo_sql.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".yml" or language_name == ".eyaml" or language_name == ".eyml" or language_name == ".yaml":
            icon = PhotoImage(file='icons/language_icons/logo_yaml.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        try:
            f.write(t.rstrip())
            self.status_bar.config(text="File saved " + self.filename + "  ")
        except:
            showerror(title="Error", message="Unable to save file...")

    def openFile(self, *args):
        if self.saved == 1:
            entry = askyesnocancel('File not saved', "You want to save?")
            if entry == True:
                self.saveFile()
            elif entry == False:
                pass
            else:
                return None
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
                ("Makefile", "*.mak;*.mk"),
                ("Markdown", "*.md;*.mkd;*.mdwn;*.mdown;*.markdown;*.markdn;*.mdtxt;*.mdtext;*.workbook"),
                ("Objective-C", "*.m"),
                ("Objective-C++", "*.mm"),
                ("Perl", "*.pl;*.pm;*.pod;*.t;*.PL;*.psgi"),
                ("Perl 6", "*.p6;*.pl6;*.pm6;*.nqp"),
                ("PHP", "*.php;*.php4;*.php5;*.phtml;*.ctp"),
                ("Powershell", "*.ps1;*.psm1;*.psd1;*.pssc;*.psrc"),
                ("Properties", "*.properties;*.cfg;*.conf;*.directory;*.gitattributes;*.gitconfig;*.gitmodules;*.editorconfig;*.npmrc"),
                ("Pug", "*.pug;*.jade"),
                ("Python", "*.py;*.rpy;*.pyw;*.cpy;*.gyp;*.gypi;.*pyi;*.ipy"),
                ("R", "*.r;*.rhistory;*.rprofile;*.rt"),
                ("Razor", ".cshtml"),
                ("Ribbon", "*.xml;*.xsd;*.ascx;*.atom;*.axml;*.axaml;*.bpmn;*.cpt;*.csl;*.csproj"),
                ("Ruby", "*.rb;*.rbx;*.rjs;*.gemspec;*.rake;*.ru;*.erb;*.podspec;*.rbi"),
                ("Rust", "*.rs"),
                ("SCSS", "*.scss"),
                ("Search Result", "*.code-search"),
                ("ShaderLab", "*.shader"),
                ("Shell Script", "*.sh;*.bash;*.bashrc;*.bash_aliases;*.bash_profile;*.bash_login;*.ebuild;*.profile;*.bash_logout;*.xprofile"),
                ("SQL", "*.sql;*.dsql"),
                ("Swift", "*.swift"),
                ("TypeScript", "*.ts"),
                ("TypeScript React", "*.tsx"),
                ("vba", "*.bas;*.cls;*.frm;*.sht;*.wbk"),
                ("VBScript", "*.vbs;*.vba;*.bas;*.vbe;*.wsf;*.wsc;*.acm;*.acr;*.acf"),
                ("Visual Basic Application", "*.cls;*.frm;*.bas;*.vbs;*.vb;*.brs"),
                ("XSL", "*.xsl;*.xslt"),
                ("YAML", "*.yml;*.eyaml;*.eyml;*.yaml"),
                ("No Extension", "*."),
            ],
        )
        self.filename, file_extension = os.path.splitext(f.name)
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)
        self.status_bar.config(text="File opened  extension : "+file_extension)
        self.root.title("Notepy - " + self.filename)
        self.saved = 0
        language_name = file_extension
        if language_name == ".py":
            icon = PhotoImage(file='icons/language_icons/logo_python.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".c" or language_name == ".i":
            icon = PhotoImage(file='icons/language_icons/logo_c.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".cpp" or language_name == ".cc" or language_name == ".cxx" or language_name == ".c++" or language_name == ".hpp" or language_name == ".hh" or language_name == ".hxx" or language_name == ".h++" or language_name == ".h" or language_name == ".ii":
            icon = PhotoImage(file='icons/language_icons/logo_cpp.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".css":
            icon = PhotoImage(file='icons/language_icons/logo_css.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".html":
            icon = PhotoImage(file='icons/language_icons/logo_html.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".json" or language_name == ".jsonc":
            icon = PhotoImage(file='icons/language_icons/logo_json.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".lua":
            icon = PhotoImage(file='icons/language_icons/logo_lua.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".pl" or language_name == ".pm" or language_name == ".pod" or language_name == ".t" or language_name == ".PL" or language_name == ".psgi":
            icon = PhotoImage(file='icons/language_icons/logo_perl.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".rb" or language_name == ".rbx" or language_name == ".rjs" or language_name == "*.gemspec" or language_name == ".rake" or language_name == ".ru" or language_name == ".erb" or language_name == ".podspec" or language_name == ".rbi":
            icon = PhotoImage(file='icons/language_icons/logo_ruby.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".sh" or language_name == ".bash" or language_name == ".bashrc" or language_name == ".bash_aliases" or language_name == ".bash_profile" or language_name == ".bash_login" or language_name == ".ebuild" or language_name == ".profile" or language_name == ".bash_logout" or language_name == ".xprofile":
            icon = PhotoImage(file='icons/language_icons/logo_bash.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".bat" or language_name == ".cmd":
            icon = PhotoImage(file='icons/language_icons/logo_batch.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".coffee" or language_name == ".cson" or language_name == ".iced":
            icon = PhotoImage(
                file='icons/language_icons/logo_coffeescript.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".cs" or language_name == ".csx" or language_name == ".cake":
            icon = PhotoImage(file='icons/language_icons/logo_csharp.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".java" or language_name == ".class" or language_name == ".jav":
            icon = PhotoImage(file='icons/language_icons/logo_java.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".js" or language_name == ".cs6" or language_name == ".mjs" or language_name == ".cjs" or language_name == ".pac":
            icon = PhotoImage(file='icons/language_icons/logo_javascript.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".sql" or language_name == ".dsql":
            icon = PhotoImage(file='icons/language_icons/logo_sql.png')
            self.root.call('wm', 'iconphoto', self.root, icon)
        elif language_name == ".yml" or language_name == ".eyaml" or language_name == ".eyml" or language_name == ".yaml":
            icon = PhotoImage(file='icons/language_icons/logo_yaml.png')
            self.root.call('wm', 'iconphoto', self.root, icon)

    def exp_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "", 16)
        content = self.text.get(0.0, END)
        pdf.multi_cell(0, 5, content)
        pdf.ln()
        pdf.output(asksaveasfilename(defaultextension=".pdf",
                   filetypes=[("PDF file", "*.pdf")]), "F")

    def quit(self, *args):
        if self.saved == 1:
            entry = askyesnocancel('File not saved', "You want to save?")
            if entry == True:
                self.saveFile()
            elif entry == False:
                self.root.destroy()
            else:
                pass
        else:
            entry = askokcancel('Confirm exit', "Sure you want to Quit?")
            if entry == True:
                self.root.destroy()

    def __init__(self, text, root, status_bar):
        self.filename = None
        self.text = text
        self.root = root
        self.saved = 0
        self.status_bar = status_bar

    def changed(self, *args):
        self.saved = 1
        self.root.title("Notepy - " + self.filename + "*")


def main(root, text, menubar, status_bar):

    filemenu = Menu(menubar, tearoff=False)  # File menu gui
    objFile = File(text, root, status_bar)

    filemenu.add_command(label=" New", command=objFile.newFile)
    filemenu.add_command(label=" Open ", command=objFile.openFile)
    filemenu.add_command(label=" Save ", command=objFile.saveFile)
    filemenu.add_command(label=" Save As ", command=objFile.saveAs)

    filemenu.add_separator()

    filemenu.add_command(label=" Export to PDF", command=objFile.exp_pdf)

    filemenu.add_separator()

    filemenu.add_command(label=" Exit ", command=objFile.quit)

    menubar.add_cascade(label=" File ", menu=filemenu)
    root.config(menu=menubar)

    # File menu keyboard shortcut
    root.bind_all("<Control-n>", objFile.newFile)
    root.bind_all("<Control-o>", objFile.openFile)
    root.bind_all("<Control-s>", objFile.saveFile)
    root.bind_all("<Control-q>", objFile.quit)

    text.bind("<<Modified>>", objFile.changed)

    root.protocol("WM_DELETE_WINDOW", objFile.quit)

if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")

