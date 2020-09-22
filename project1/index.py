from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys


MainUI,_ = loadUiType('index.ui')


class Main(QMainWindow , MainUI):
    def __init__(self , perent=None):
        super(Main,self).__init__(perent)
        QMainWindow.__init__(self)
        self.setupUi(self)

#all the change that you whant to aberr in screen when the appliction start up
    def UI_Chang(self):
        pass

#the connection to the DataBase
    def DB_Connect(self):
        pass

#to handel all the buttons in the application
    def Handel_Buttons(self):
        pass




def main():
    app = QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()