from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        top = 400
        left = 400
        width = 800
        height = 600

        self.setWindowTitle('Lab8 Paint')
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        brushSize = mainMenu.addMenu('Brush Size')
        brushColor = mainMenu.addMenu('Brush Color')

        saveAction = QAction(QIcon('icons/icon_save.png'), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon('icons/icon_clean.png'), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        threePxAction = QAction(QIcon('icons/icon_brushSize.png'), "3px", self)
        threePxAction.setShortcut("Ctrl+3")
        brushSize.addAction(threePxAction)
        threePxAction.triggered.connect(self.px_3)

        sixPxAction = QAction(QIcon('icons/icon_brushSize.png'), "6px", self)
        sixPxAction.setShortcut("Ctrl+6")
        brushSize.addAction(sixPxAction)
        sixPxAction.triggered.connect(self.px_6)

        ninePxAction = QAction(QIcon('icons/icon_brushSize.png'), "9px", self)
        ninePxAction.setShortcut("Ctrl+9")
        brushSize.addAction(ninePxAction)
        ninePxAction.triggered.connect(self.px_9)

        twelvePxAction = QAction(QIcon('icons/icon_brushSize.png'), "12px", self)
        twelvePxAction.setShortcut("Ctrl+0")
        brushSize.addAction(twelvePxAction)
        twelvePxAction.triggered.connect(self.px_12)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+K")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.black)

        whiteAction = QAction(QIcon("icons/white.png"), "White", self)
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.white)

        yellowAction = QAction(QIcon('icons/yellow.png'), "Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellow)

        redAction = QAction(QIcon('icons/red.png'), "Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.red)

        greenAction = QAction(QIcon('icons/green.png'), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.green)

        blueAction = QAction(QIcon('icons/blue.png'), 'Blue', self)
        blueAction.setShortcut("Ctrl+B")
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.blue)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

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
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def px_3(self):
        self.brushSize = 3

    def px_6(self):
        self.brushSize = 6

    def px_9(self):
        self.brushSize = 9

    def px_12(self):
        self.brushSize = 12

    def black(self):
        self.brushColor = Qt.black

    def white(self):
        self.brushColor = Qt.white

    def yellow(self):
        self.brushColor = Qt.yellow

    def red(self):
        self.brushColor = Qt.red

    def green(self):
        self.brushColor = Qt.green

    def blue(self):
        self.brushColor = Qt.blue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
