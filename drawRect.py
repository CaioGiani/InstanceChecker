from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QFileDialog, QSlider
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PIL import Image, ImageQt
import os


class Drawing(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw a rectangle')
        self.btn = QPushButton('Draw', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.draw)
        self.label = QLabel(self)
        self.label.setGeometry(10, 40, 200, 200)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw a rectangle')
        self.show()
        
    def draw(self):
        print('draw')
        im = Image.open('images/1.jpg')
        im = im.resize((640, 640))
        self.label.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(im)))
        
        self.label.setText('draw')

if __name__ == '__main__':
    app = QApplication([])
    ex = Drawing()
    app.exec()