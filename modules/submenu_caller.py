__author__='Mirko Rovere'

from submenu import file_menu, format_menu, edit_menu, revision_menu, code_menu, help_menu, rightmenu, run_menu

def main(root, text, menubar, status_bar):
    file_menu.main(root, text, menubar, status_bar)

    edit_menu.main(root, text, menubar, status_bar)

    format_menu.main(root, text, menubar, status_bar)

    revision_menu.main(root, text, menubar, status_bar)

    code_menu.main(root, text, menubar, status_bar)
    
    rightmenu.main(root, text, menubar, status_bar)
    
    help_menu.main(root, menubar)

    run_menu.main(root, menubar)
