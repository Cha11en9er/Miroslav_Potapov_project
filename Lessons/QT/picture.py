import sys
  
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
  
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Тест'
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 300
        self.initUI()
  
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
  
        pixmap = QPixmap('redrock.png')
  
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
  
        self.resize(pixmap.width(), pixmap.height())
        self.show()
  
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
