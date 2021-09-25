import sys
import os
from PySide2 import QtCore
from PySide2.QtGui import  QColor
from PySide2.QtWidgets import *
## ==> SPLASH SCREEN
from splash.ui_splash_screen import Ui_SplashScreen
import main

## ==> GLOBALS
counter = 0
        

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)


        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> To Notepy")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> MODULE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            
            # STOP TIMER
            self.timer.stop()

            #CLOSE SPLASH SCREEN
            self.close()

            if "nt" == os.name:
                self.main = main.main()


        # INCREASE COUNTER
        counter += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()

    if "nt" == os.name:
        sys.exit(app.exec_())
    else:
        app.exec_()
        main.main()
