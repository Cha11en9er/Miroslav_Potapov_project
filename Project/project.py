from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog, QColorDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys



class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        top = 300 
        left = 300
        width = 800
        height = 600
        
        icon = "icons/pain.PNG"

        self.setWindowTitle("Paint Application")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

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
        #setting up File menu
        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/clear.PNG"), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        openAction = QAction(QIcon("icons/save.PNG"), "Open", self)
        openAction.setShortcut("Ctrl+O")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.openfile)

        #setting up File menu Brush Size menu
        threepxAction = QAction(QIcon("icons/threepx.PNG"), "3px", self)
        threepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        eraserAction = QAction(QIcon("icons/eraser.PNG"), "Eraser", self)
        eraserAction.setShortcut("Ctrl+O")
        brushColor.addAction(eraserAction)
        eraserAction.triggered.connect(self.eraser)

        fivepxAction = QAction(QIcon("icons/fivepx.PNG"), "5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction(QIcon("icons/sevenpx.PNG"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+Т")
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction(QIcon("icons/ninepx.PNG"), "9px", self)
        ninepxAction.setShortcut("Ctrl+N")
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        blackAction = QAction(QIcon("icons/black.PNG"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColo)
        
        redAction = QAction(QIcon("icons/red.PNG"), "Red", self)
        redAction.setShortcut("Ctrl+W")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColo)

        greenAction = QAction(QIcon("icons/green.PNG"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColo)

        palitraAction = QAction(QIcon("icons/palitra.PNG"), "Palitra", self)
        palitraAction.setShortcut("Ctrl+I")
        brushColor.addAction(palitraAction)
        palitraAction.triggered.connect(self.palitraColor)

        yellowAction = QAction(QIcon("icons/yellow.PNG"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+L")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColo)

    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
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

    #TODO
    def openfile(self):
        filePath, _= QFileDialog.getOpenFileName(self, "Open Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.load(filePath) 
        self.update()       

    
    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    
    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def  blackColo(self):
        self.brushColor = Qt.black

    def  redColo(self):
        self.brushColor = Qt.red

    def  greenColo(self):
        self.brushColor = Qt.green
    
    def  yellowColo(self):
        self.brushColor = Qt.yellow

    def palitraColor(self):
        selectedcolor = QColorDialog.getColor()
        self.brushColor = selectedcolor

    def  eraser(self):
        self.brushColor = Qt.white
        self.brushSize = 5

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()