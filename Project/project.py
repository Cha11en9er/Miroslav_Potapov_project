from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
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

        # saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        # saveAction.setShortcut("Ctrl+S")
        # fileMenu.addAction(saveAction)
        # saveAction.triggered.connect(self.save)

        # clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        # clearAction.setShortcut("Ctrl+C")
        # fileMenu.addAction(clearAction)
        # clearAction.triggered.connect(self.clear)

        # threepxAction = QAction(QIcon("icons/treepx.png"), "3px", self)
        # threepxAction.setShortcut("Ctrl+T")
        # brushMenu.addAction(threepxAction)

        # fivepxAction = QAction(QIcon("icons/fivepx.png"), "5px", self)
        # fivepxAction.setShortcut("Ctrl+F")
        # brushMenu.addAction(fivepxAction)

        # sevenpxAction = QAction(QIcon("icons/sevenpx.png"), "7px", self)
        # sevenpxAction.setShortcut("Ctrl+Т")
        # brushMenu.addAction(sevenpxAction)

        # ninepxAction = QAction(QIcon("icons/ninepx.png"), "9px", self)
        # ninepxAction.setShortcut("Ctrl+N")
        # brushMenu.addAction(ninepxAction)

        # blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        # blackAction.setShortcut("Ctrl+B")
        # brushColor.addAction(blackAction)
        
        # redAction = QAction(QIcon("icons/red.png"), "Red", self)
        # blackAction.setShortcut("Ctrl+W")
        # brushColor.addAction(blackAction)

        # greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        # blackAction.setShortcut("Ctrl+G")
        # brushColor.addAction(blackAction)

        # yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        # blackAction.setShortcut("Ctrl+G")
        # brushColor.addAction(blackAction)

    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundJoin, Qt.RoundCap))
            painter.drawImage(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    
    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False


    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())


    def save(self):
        filePath, _= QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    
    def clear(self):
        self.image.fill(Qt.white)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
