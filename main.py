
from decimal import localcontext
import os
import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QHBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase

# ################################################################################################
# # Convert UI to PyQt5 py file
# ################################################################################################
# os.system("pyuic5 -o interfaceWidget__ui.py interfaceWidget.ui")
# os.system("pyuic5 -o analoggaugewidget_demo_ui.py analoggaugewidget_demo.ui.oQCkCR")

################################################################################################
# Import UI file
################################################################################################
from interfaceWidget import *

################################################################################################
# MAIN WINDOW CLASS
################################################################################################


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.setWindowTitle('My First Gauge Application')
        self.move(300, 300)

        # gauge 크기를 재배치함. 대충.
        width = 320   
        height = 300   
        
        #gauge 크기에 따라서... 전체 화면 크기 조정을 함
        self.resize(width*4.2, height*2)  

        # 인스턴스 생성 
        self.ui = Ui_Form(width, height)

        # gauge 생성 (Theme : 0 ~ 24)
        self.ui.gaugeForm1(self, 5)
        self.ui.gaugeForm2(self, 3)
        self.ui.gaugeForm3(self, 5)
        self.ui.gaugeForm4(self, 3)

        ################################################################################################
        # Show window
        ################################################################################################
        self.show()


########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    ##
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################
