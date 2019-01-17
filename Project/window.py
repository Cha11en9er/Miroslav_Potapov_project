import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Флаг')
 
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)
 
        self.name_label = QLabel(self)
        self.name_label.setText("Введите кол-во цветов: ")
        self.name_label.move(10, 90)
 
        self.name_input = QLineEdit(self)
        self.name_input.move(130, 90)

        def paintEvent(self, event):
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

 
    def hello(self, qp):
        name = int(self.name_input)
        for i in range(name):
            qp.setBrush(QColor("#%03x" % random.randint(0, 0xFFF)))
            qp.drawRect(30, 30, 120, 30)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())