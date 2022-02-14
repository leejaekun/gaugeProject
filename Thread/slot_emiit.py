import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal

#사용자 정의 시그널 사용을 위한 클래스 정의
# 저기 저 먼곳에서... 계산을 하고 있음.
class CustomSignal(QObject) :
    # 변수의 개수는 상관없음. 타입만 맞으면 되는 듯.
    signal = pyqtSignal(int, str, str) # 반드시 클래스 변수로 선언할 것
    
    def runText(self) :
        # 실제 결과값을 계산하는 부분 (중간 ....)
        # Serial 통신에서 데이타를 받는 부분. 정확인 데이타가 오는 경우, 값이 변경이 됨.
        tempstr = "emit으로 전달"
        addStr = "추가 문자열"
        for i in range(1, 10):
            self.signal.emit(i, tempstr, addStr) #customFunc 메서드 실행시 signal의 emit 메서드 사용
            
class MyWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.Init()
           
    def actionFunction(self) :    
        customsignal = CustomSignal() # Mysignal 클래스의 객체선언
        customsignal.signal.connect(self.funcEmit) #객체에 대한 시스널 및 슬롯 설정
        # 실행 프로그램을 호출하는 부분. 함수 이름은 상관이 없음. 같으면 됨.
        # 처음 실행은 여기서 부터...(시작....)
        customsignal.runText() #객체의 customFunc 메서드 실행
        
    #customFunc에서 emit 메서드 실행시 GUI에서 받음
    @pyqtSlot(int, str, str)
    def funcEmit(self, i, tempstr, addStr):
        # 데이타를 받아서 실행을 하는 부분(최종....)
        self.i = i              #emit을 통해 받은 값을 GUI 객체 변수에 저장
        self.tempstr = tempstr  #emit을 통해 받은 값을 GUI 객체 변수에 저장
        self.addStr = addStr    #emit을 통해 받은 값을 GUI 객체 변수에 저장
        self.txtBrowser.append(str(self.i) + "번째 출력" + self.tempstr + self.addStr) # 출력해보기
        
    def Init(self):
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Slot Signal - Custom Emit')
        
        # 각 버튼에 대한 함수 연결 
        self.runBtn1 = QPushButton("출력", self)
        self.runBtn1.clicked.connect(self.actionFunction)
        
        self.runBtn2 = QPushButton("닫기", self)
        self.runBtn2.clicked.connect(self.close)
        
        self.txtBrowser = QTextBrowser()
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.runBtn1)
        hbox.addWidget(self.runBtn2)
        vbox.addLayout(hbox)
        vbox.addWidget(self.txtBrowser)
        
        self.setLayout(vbox)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()