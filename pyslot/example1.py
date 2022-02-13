"""
    1. custom signal & custom slot
    출처: https://freeprog.tistory.com/328 [취미로 하는 프로그래밍 !!!]
"""


from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

class PunchingBag(QObject):
    """
    QObject 를 상속받으면, custom signal을 만들수있다.
    """
    punched = pyqtSignal()  # custom signal

    def __init__(self):
        # Initialize the PunchingBag as a QObject
        super().__init__()

    def punch(self):
        self.punched.emit()


@pyqtSlot()
def say_punched():
    print('Bag was punched.')


if __name__ == "__main__":
    bag = PunchingBag()
    # Connect the bag's punched signal to the say_punched slot
    bag.punched.connect(say_punched)

    # Punch the bag 10 times
    for i in range(5):
        bag.punch()