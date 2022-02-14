"""
ZetCode PyQt5 tutorial

In this example, we show how to
emit a custom signal.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Communicate(QObject):

    closeApp = pyqtSignal()
    
    btnClick = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.printSignal)
        self.c.btnClick.connect(self.printBtnSignal)
        # self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Emit signal')
        
        btn = QPushButton("Push", self)
        btn.clicked.connect(self.eventCall)
        
        self.show()

    def eventCall(self):
        self.c.btnClick.emit()        

    def mousePressEvent(self, event):
        self.c.closeApp.emit()
    
    def printSignal(self):
        print("signal....emitted")

    def printBtnSignal(self):
        print("signal....button...emitted")
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()