############################################################
# 경주마 1이 실행이 되면 완료될때까지 경주마 2는 실행이 되지 않음.
# 이러한 문제를 해결 하기 위하여 Trhead를 사용을 함.
# 실제적으로는 단일 실행의 방법임.
# 여기서는 QThread 를 사용을 함.
# 출처 : https://ybworld.tistory.com/39?category=929856
############################################################
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# QThread 클래스 선언하기, QThread 클래스 쓰려면 QtCore 모듈을 import 해야함 
# 경주마 1을 위한 스레드
class Thread1(QThread) :
    #초기화 메서드 구현 
    def __init__(self, parent) : # parent는 WindowClass에서 전달하는 self이다
                                 # (WindowClass의 인스턴스) 
        super().__init__(parent) 
        self.parent = parent     # self.parent를 사용하며 WindowClass 위젯을 제어할 수 있다.

    def run(self) :
        self.parent.txtBrowser.append('경주마1이 출발하였습니다.')
        for i in range(20) :
            self.parent.txtBrowser.append('경주마1이'+str(i) + 'km째 달리고 있습니다.')
            time.sleep(2)
        self.parent.txtBrowser.append('경주마1이 결승지에 도착했습니다.')

# QThread 클래스 선언하기, QThread 클래스 쓰려면 QtCore 모듈을 import 해야함 
# 경주마 2를 위한 스레드 
class Thread2(QThread) :
    #초기화 메서드 구현 
    def __init__(self, parent) : # parent는 WindowClass에서 전달하는 self이다
                                 # (WindowClass의 인스턴스) 
        super().__init__(parent) 
        self.parent = parent     # self.parent를 사용하며 WindowClass 위젯을 제어할 수 있다.

    def run(self) :
        self.parent.txtBrowser.append('경주마2가 출발하였습니다.')
        for i in range(20) :
            self.parent.txtBrowser.append('경주마2가'+str(i) + 'km째 달리고 있습니다.')
            time.sleep(2)
        self.parent.txtBrowser.append('경주마2가 결승지에 도착했습니다.')

class WindowClass(QWidget) :
# class WindowClass(QMainWindow) :  # QMainWindow를 상속받으면 setLatout이 되지 않음. 
    def __init__(self) :
        super().__init__()
        self.Init()
    
    def Init(self):
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Thread - race')

        
        # 각 버튼에 대한 함수 연결 
        self.runBtn1 = QPushButton("경주마1 출발", self)
        self.runBtn1.clicked.connect(self.actionFunction1)
        
        self.runBtn2 = QPushButton("경주마2 출발", self)
        self.runBtn2.clicked.connect(self.actionFunction2)
        
        self.txtBrowser = QTextBrowser()
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.runBtn1)
        hbox.addWidget(self.runBtn2)
        vbox.addLayout(hbox)
        vbox.addWidget(self.txtBrowser)
        
        self.setLayout(vbox)
        
    #경주마 1 출발 버튼을 눌렀을 때 실행될 메서드    
    def actionFunction1(self) :
        h1 = Thread1(self)
        h1.start()
    
    #경주마 2 출발 버튼을 눌렀을 때 실행될 메서드    
    def actionFunction2(self) :
        h2 = Thread2(self)
        h2.start()
    
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    