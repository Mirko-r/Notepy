from tkinter.messagebox import *
from tkinter import messagebox, Menu
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from idlelib.percolator import Percolator
from idlelib.colorizer import ColorDelegator
import re


class Code():
    def __init__(self, text, root, status_bar):
        self.text = text
        self.root = root
        self.status_bar = status_bar

    def get_c_function_list(self):
        """
        Parse the text and return all C functions as a list.
        Made as simple as possible.
        The text must be valid C code.
        """
        # Store the text
        text = self.text.get(1.0, END)
        # Initialize state variables
        curly_count = 0
        parenthesis_count = 0
        singleline_commenting = False
        multiline_commenting = False
        typedefing = False
        stringing = False
        previous_token = ""
        last_found_function = ""
        last_line = 0
        current_line = 1
        function_list = []
        # Tokenize the text and remove the space characters
        splitter = re.compile(r"(\#\w+|\'|\"|\n|\s+|\w+|\W)")
        tokens = [token for token in splitter.findall(text)]
        # Main Loop for filtering tokens
        for i, token in enumerate(tokens):
            stripped_token = token.strip()
            if "\n" in token:
                newline_count = token.count("\n")
                current_line += newline_count
                # Reset the single line comment flag
                singleline_commenting = False
            if stripped_token == "":
                continue
            # Check for function definitions
            if curly_count == 0:
                if multiline_commenting == False and singleline_commenting == False:
                    if token == "{" and previous_token == ")":
                        # The function has passed the filter, add it to the list
                        function_list.append((last_found_function, last_line))
                    elif token == "(" and re.match(r"\w", previous_token) and parenthesis_count == 0:
                        last_found_function = previous_token
                        last_line = current_line
            if token == "typedef":
                typedefing = True
            # Check for various state changes
            if (multiline_commenting == False and singleline_commenting == False and
                    stringing == False):
                if token == "{":
                    curly_count += 1
                elif token == "}":
                    curly_count -= 1
                elif token == "(":
                    parenthesis_count += 1
                elif token == ")":
                    parenthesis_count -= 1
                elif token == "*" and previous_token == "/":
                    multiline_commenting = True
                elif token == "/" and previous_token == "/":
                    singleline_commenting = True
            else:
                if token == "/" and previous_token == "*":
                    multiline_commenting = False
            # Store the previous token
            if stripped_token != "":
                previous_token = token
        # Sort the functions alphabetically

        def compare_function(item):
            return item[0].lower()
        function_list = sorted(function_list, key=compare_function)
        # Return the function list
        list = ''.join([str(item) for item in function_list])
        messagebox.showinfo("Functions list", list)

    def sintax_highlight(self):
       Percolator(self.text).insertfilter(ColorDelegator())



def main(root, text, menubar, status_bar):

    codemenu = Menu(menubar, tearoff=False)
    objCode = Code(text, root, status_bar)

    # Specific C functions
    csubmenu = Menu(codemenu, tearoff=False)
    csubmenu.add_command(label="Get program functions list", command=objCode.get_c_function_list)
    codemenu.add_cascade(label="C", underline=0, menu=csubmenu)

    codemenu.add_command(label="Highlight syntax", command=objCode.sintax_highlight)

    menubar.add_cascade(label="Code", menu=codemenu)
    root.config(menu=menubar)


if __name__ == "__main__":
    messagebox.showerror("Error", "Please run main.py")
