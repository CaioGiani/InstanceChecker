from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QFileDialog, QLabel, QPushButton
from PIL import Image, ImageFilter, ImageQt
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton('open image')
        self.btn.clicked.connect(self.openImage)


        self.lbShowImg = QLabel()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0,20)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(3)
        self.slider.valueChanged.connect(self.sliderValueChange)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.lbShowImg)
        self.mainLayout.addWidget(self.slider)
        self.setLayout(self.mainLayout)


    def openImage(self):
        self.img = Image.open(QFileDialog.getOpenFileName(self, "select image",'./', 'imagefile(*.png *.jpg)')[0])
        self.lbShowImg.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.img)))

    def sliderValueChange(self, value):
        self.blurPic = self.img.filter(ImageFilter.GaussianBlur(value))
        self.lbShowImg.setPixmap(ImageQt.toqpixmap(self.blurPic))
        
if __name__ == '__main__': 
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec()