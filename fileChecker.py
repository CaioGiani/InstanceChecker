from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QLineEdit, QFileDialog, QTextBrowser
from PySide6.QtCore import Qt
import os
from PySide6.QtGui import QPixmap
from Ui_test import Ui_MainWindow
from PIL import Image, ImageQt

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lbImg = QLabel()
        self.textBrowser = QTextBrowser()
        self.bind()

    def bind(self):
        self.actionOpen.triggered.connect(self.openFile)
        self.actionQuit.triggered.connect(self.close)
        

    def openFile(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            print('found directory')
            self.list_files(directory)
                    
    def list_files(self, directory):
        file_list = []
        list_files = os.listdir(directory)
        indexImage = 0
        for file in list_files:
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                file_list.append(file)
        for file in file_list:
            txt_file = os.path.join(directory, os.path.splitext(file)[0] + '.txt')
            assert os.path.exists(txt_file), "No txt file found"             #need a dialog box to show the error
        self.imageFiles = file_list
        self.indexImage = indexImage
        self.openImage(directory)
        self.plotText(directory)

    def openImage(self, directory):
        imageFile = os.path.join(directory, self.imageFiles[self.indexImage])
        print(imageFile)
        self.img = Image.open(imageFile)
        self.img = self.img.resize((640, 640))
        self.lbImg.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.img)))
        print('found image')

    def plotText(self, directory):
        txtFile = os.path.join(directory, os.path.splitext(self.imageFiles[self.indexImage])[0] + '.txt')
        print(txtFile)
        with open(txtFile, 'r') as file:
            content = file.read()
            self.textBrowser.setText(content)
            # print(content)
        print('found txt')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()