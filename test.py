import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QMainWindow
import glob

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('test.ui', self)
        self.actionOpen.triggered.connect(self.open_directory)
        self.actionQuit.triggered.connect(self.close)

    
    def open_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.list_files(directory)
    
    def list_files(self, directory):
        self.ListInstance.clear()
        file_list = []
        # Add code here to list all image files in the directory and append them to file_list
        
        for file in file_list:
            pixmap = QPixmap(file)
            label = QLabel()
            label.setPixmap(pixmap)
            self.ListInstance.layout().addWidget(label)
     

    def read_images_and_txt(directory):
        file_list = glob.glob(directory + '/*.jpg')  # Change the file extension if needed
        txt_list = glob.glob(directory + '/*.txt')  # Change the file extension if needed
        
        for file in file_list:
            pixmap = QPixmap(file)
            label = QLabel()
            label.setPixmap(pixmap)
            self.frameImage.layout().addWidget(label)
        
        for txt_file in txt_list:
            with open(txt_file, 'r') as file:
                content = file.read()
                self.ListInstance.addItem(content)    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

   