############################################################
# 경주마 1이 실행이 되면 완료될때까지 경주마 2는 실행이 되지 않음.
# 이러한 문제를 해결 하기 위하여 Trhead를 사용을 함.
# 실제적으로는 단일 실행의 방법임.
# 출처 : https://ybworld.tistory.com/38
############################################################
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class WindowClass(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.Init()
    
    def Init(self):
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Thread - race')
        
        # 각 버튼에 대한 함수 연결 
        self.runBtn1 = QPushButton("경주마1 출발", self)
        self.runBtn1.clicked.connect(self.actionFunction1)
        self.runBtn1.move(50, 50)
        self.runBtn1.resize(150,40)
        
        self.runBtn2 = QPushButton("경주마2 출발", self)
        self.runBtn2.clicked.connect(self.actionFunction2)
        self.runBtn2.move(200, 50)
        self.runBtn2.resize(150,40)
    
    #경주마 1 출발 버튼을 눌렀을 때 실행될 메서드    
    def actionFunction1(self) :
        print('경주마1이 출발하였습니다.')
        for i in range(20) :
            print('경주마1이'+str(i) + 'km째 달리고 있습니다.')
            time.sleep(1)
        print('경주마1이 결승지에 도착했습니다.')
    
    #경주마 2 출발 버튼을 눌렀을 때 실행될 메서드    
    def actionFunction2(self) :
        print('경주마2이 출발하였습니다.')
        for i in range(20) :
            print('경주마2이'+str(i) + 'km째 달리고 있습니다.')
            time.sleep(1)
        print('경주마2이 결승지에 도착했습니다.')
    
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    