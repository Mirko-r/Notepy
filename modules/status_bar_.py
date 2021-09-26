__author__='Mirko Rovere'

from tkinter import *

def main(text, status_bar):

    def get_position(event ):
        """get the line and column number of the text insertion point"""
        line, column = text.index('insert').split('.')
        s = "line=%s" % (line)
        status_bar.config(text = s + "  ")

    text.bind("<KeyRelease>", get_position)

