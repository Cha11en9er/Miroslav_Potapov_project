import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Шестая программа')
 
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)
 
        self.name_label = QLabel(self)
        self.name_label.setText("Введите имя картинки: ")
        self.name_label.move(40, 90)
 
        self.name_input = QLineEdit(self)
        self.name_input.move(130, 90)
 
    def hello(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap(self.name_input.text())

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)


 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())