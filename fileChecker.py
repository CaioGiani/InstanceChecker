from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QLineEdit, QFileDialog, QTextBrowser
from PySide6.QtCore import Qt
import os
from PySide6.QtGui import QPixmap
from Ui_test import Ui_MainWindow
from PIL import Image, ImageQt, ImageDraw, ImageFont

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
  
    def bind(self):
        self.categoryIndex = False
        self.actionOpen.triggered.connect(self.openFile)
        self.actionQuit.triggered.connect(self.close)
        self.pushButtonAnnotation.clicked.connect(self.switchAnnotation)
        if not self.categoryIndex:
            self.categoryIndex = [  'BiologicalColonization',           'Plant',         'Discoloration',     'Crust&Deposit',
                                    'Subflorescence&efflorescence',     'Graffiti',      'Alveolization',     'Erosion',
                                    'Peeling',                          'Delamination',  'Crack',             'Disintegration'
                                    ]
            self.colorIndex = [ [196.36, 182.69, 100.75774],
                                [108.79, 114.33, 55.32],
                                [206.8, 130.08, 131.81],
                                [248.904, 92.56, 200.51],

                                [156.76, 47.006, 79.201],
                                [131.24, 105.24, 145.38],
                                [192.83, 11.103, 253.69],
                                [252.85, 235.66, 83.937],

                                [150.046, 216.47, 203.75],
                                [40.367, 155.43, 218.26],
                                [254.99, 120.09, 32.34],
                                [25.5, 241.7, 10.47]
                                ]
                    

    def openFile(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.directory:
            file_list = []
            txt_file = []
            list_files = os.listdir(self.directory)
            for file in list_files:
                if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                    file_list.append(self.directory + '/' + file)
            for file in file_list:
                checkTxtDirection = (os.path.splitext(file)[0] + '.txt')
                assert os.path.exists(checkTxtDirection), "No txt file found" 
                txt_file.append(checkTxtDirection)
            self.imageFiles = file_list
            self.txt_file = txt_file
            self.indexImage = 0
            self.curretImageDirection = self.imageFiles[self.indexImage]
            self.plotImage(Image.open(self.curretImageDirection))
            self.readText()

    def readText(self):
        textFileDirectory = self.txt_file[self.indexImage]
        self.annotationContentDict = dict()
        content = 'Annotation Content:\n\n'
        with open(textFileDirectory, 'r') as file:
            rawText = file.read()
        for i,line in enumerate(rawText.split('\n')):
            if line:
                line = line.split(' ')
                category = int(line[0])
                x = float(line[1])
                y = float(line[2])
                w = float(line[3])
                h = float(line[4])
                self.annotationContentDict[i] = [self.categoryIndex[category], x, y, w, h]
                content += f'No_{i}:   {self.annotationContentDict[i][0]}\n'
        self.textBrowser.setText(content)
        self.annotateImagefromText()

    def switchAnnotation(self):
        if self.pushButtonAnnotation.text() == 'Show Annotation':
            self.pushButtonAnnotation.setText('Hide Annotation')
            self.plotImage(self.annotatedImage)
        else:  
            self.pushButtonAnnotation.setText('Show Annotation')
            self.plotImage(Image.open(self.curretImageDirection))

    def annotateImagefromText(self):
        self.annotatedImage = Image.open(self.curretImageDirection)
        X, Y = self.annotatedImage.size
        for key in self.annotationContentDict.keys():
            category = self.annotationContentDict[key][0]
            x = int(self.annotationContentDict[key][1] * X)
            y = int(self.annotationContentDict[key][2] * Y)
            w = int(self.annotationContentDict[key][3] * X)
            h = int(self.annotationContentDict[key][4] * Y)
            xmin = x - w//2
            ymin = y - h//2
            xmax = x + w//2
            ymax = y + h//2
            self.drawRectangularsonImage(category, xmin, ymin, xmax, ymax)

    def drawRectangularsonImage(self, category, xmin, ymin, xmax, ymax):
        draw = ImageDraw.Draw(self.annotatedImage)
        outline = tuple(map(int, self.colorIndex[self.categoryIndex.index(category)]))
        draw.rectangle([xmin, ymin, xmax, ymax], outline=outline, width=5)
        draw.text((xmin, ymin), category, fill=outline, font= ImageFont.truetype("arial.ttf", 20))
        
    
    def plotImage(self, image2plot):
        image2plot.resize((640, 640))
        image2plot = ImageQt.ImageQt(image2plot)
        image2plot = QPixmap.fromImage(image2plot)
        self.lbImg.setPixmap(image2plot)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()