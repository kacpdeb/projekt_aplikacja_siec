import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.models import model_from_json
from keras.models import load_model
from keras.datasets import mnist 
from keras.utils import np_utils 
from keras import layers 
from keras import models 
from keras.utils import to_categorical
from matplotlib.image import imread
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QTextEdit, QMainWindow, QMenu, QMenuBar, QAction, QFileDialog, QMessageBox
import sys
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
import sys
import pathlib
import imutils
import cv2


def resize_image(image, width, height):
    (h, w) = image.shape[:2]
    
    if w > h:
        image = imutils.resize(image, width=width)

    else:
        image = imutils.resize(image, height=height)

    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)

    image = cv2.copyMakeBorder(image, padH, padH, padW, padW,
        cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))

    return image


 
class Window(QMainWindow):
    def __init__(self):

        super().__init__()
        title = "Podaj liczbe do odczytania"
        top = 400
        left = 200
        width = 1000
        height = 800

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.black)
        self.drawing = False
        self.brushSize = 80
        self.brushColor = Qt.white
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("Plik")
        saveAction = QAction(QIcon(), "Zbadaj[E]",self)
        saveAction.setShortcut("E")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        clearAction = QAction(QIcon(), "wyczysc[W]", self)
        clearAction.setShortcut("W")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)
 
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
 
    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
 
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
 
    def paintEvent(self, event):
        canvasPainter  = QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect() )

    def save(self):
       



















    def clear(self):
        self.image.fill(Qt.black)
        self.update()
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()