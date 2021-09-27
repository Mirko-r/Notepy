__author__='Mirko Rovere'

from tkinter import *

def main(text, status_bar):

    def update(event ):

        try:
            line, column = text.index('insert').split('.')
        except:
            pass

        try:
            t = text.get(0.0, END)
            words = [w for w in t.split(' ') if w!='\n']
            word_count = len(words)
        except:
            pass

        try:
            text_var = text.get(1.0, END)
            word_list = text_var.split('\n')
            count = 0
            for x in word_list:
                if x != "":
                    count += len(x)
        except:
            pass

        s = "| chars=%s | words=%s | line=%s  " % (count, word_count, line)
        status_bar.config(text = s)

    text.bind("<KeyRelease>", update)
