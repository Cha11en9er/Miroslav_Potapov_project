from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QWidget
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtCore import Qt, QPoint
import sys



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI
    
    def initUI(self):
        self.setGeometry(400, 400, 800, 600)
        self.setWindowIcon("Paint Application")

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushMenu = mainMenu.addMenu("Brush Size")
        brushColor = mainMenu.addMenu("Brush Color")

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        threepxAction = QAction(QIcon("icons/treepx.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(threepxAction)

        fivepxAction = QAction(QIcon("icons/fivepx.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        brushMenu.addAction(fivepxAction)

        sevenpxAction = QAction(QIcon("icons/sevenpx.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+S")
        brushMenu.addAction(sevenpxAction)

        ninepxAction = QAction(QIcon("icons/ninepx.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+N")
        brushMenu.addAction(ninepxAction)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
