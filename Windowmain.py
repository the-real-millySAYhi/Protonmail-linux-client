import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui



raw = open("root file directory.fdir","r")
root = raw.read()

System = open(root + "\OS Data\OStype.info","r")
System = System.read()


class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setWindowIcon(QtGui.QIcon('icon2.png'))
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://protonmail.com/login'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

def WindowsIconPatch():
    myappid = 'org.AlphaLinux.protonmail' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if (System == "Windows"):
    WindowsIconPatch()


    
MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Protonmail Linux client Beta 1.0')
window = Window()
MyApp.exec_()



