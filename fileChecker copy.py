from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QLineEdit, QFileDialog, QTextBrowser, QWidget, QMessageBox
from PySide6.QtCore import Qt, Signal
import os
from PySide6.QtGui import QPixmap
from Ui_test import Ui_MainWindow
from Ui_AnnotationWindow import Ui_AnnotationWindow
from PIL import Image, ImageQt, ImageDraw, ImageFont

class MyWindow(QMainWindow, Ui_MainWindow):
    sendValueToSub = Signal(object)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.annotationChanged = False
        self.categoryIndex = [  'BiologicalColonization',           'Plant',         'Discoloration',     'Crust&Deposit',
                                'Subflorescence&efflorescence',     'Graffiti',      'Alveolization',     'Erosion',
                                'Peeling',                          'Delamination',  'Crack',             'Disintegration'
                            ]
        self.categoryIndexForShort = [  'COL',          'PLT',         'CHR',     'CRU',
                                        'SNE',          'GRA',         'ALV',     'ERO',
                                        'PEL',          'DEL',         'CRA',      'DIS'
                                    ]
        self.colorIndex = [ [196.36, 182.69, 100.75774],    [108.79, 114.33, 55.32],    [206.8, 130.08, 131.81],    [248.904, 92.56, 200.51],
                            [156.76, 47.006, 79.201],       [131.24, 105.24, 145.38],   [192.83, 11.103, 253.69],   [252.85, 235.66, 83.937],
                            [150.046, 216.47, 203.75],      [40.367, 155.43, 218.26],   [254.99, 120.09, 32.34],    [25.5, 241.7, 10.47]
                            ]    
        self.AnnotationWindow = AnnotationWindow(self)
        self.directory = False
        self.bind()
  
    def bind(self):
        self.actionOpen.triggered.connect(self.openFile)
        self.actionQuit.triggered.connect(self.close)
        self.actionUser_Manual.triggered.connect(self.showManual)
        self.pushButtonAnnotation.clicked.connect(self.switchAnnotation)
        self.pushButtonNext.clicked.connect(self.nextImage)
        self.pushButtonPrevious.clicked.connect(self.previousImage)
        self.pushButtonAccept.clicked.connect(self.acceptAnnotationMain)
        self.pushButtonAbort.clicked.connect(self.cancelAnnotationMain)
        self.sendValueToSub.connect(self.AnnotationWindow.setTextToPlot)   

    def showManual(self):
        textInformation  = "1. Open the directory of the images and the corresponding txt files.\n\n"
        textInformation += "2. Click 'Show && Edit Annotation' to show the annotation of the current image.\n\n"
        textInformation += "3. Click 'Next' or 'Previous' to switch to the next or previous image.\n\n"
        textInformation += "4. Double click on the image to modify the annotation.\n\n"
        textInformation += "5. Click 'Quit' to exit the program.\n\n"
        textInformation += "In case of any question, please contact kai.zhang@polimi.it or chiara.mea@mail.polimi.it"
        QMessageBox.information(self, "User Manual", textInformation)

    def loggingMain(self, text):
        self.plainTextEditLog.appendPlainText(text)

    def openFile(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.annoationChanged = False
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
            self.numberOfImages = len(self.imageFiles)
            self.pushButtonNext.setText(f'Next ({self.indexImage+1}/{self.numberOfImages})')

            self.curretImageDirection = self.imageFiles[self.indexImage]
            self.plotImage(Image.open(self.curretImageDirection))
            self.readText()
            self.loggingMain(f'{self.numberOfImages} images are loaded from {self.directory}')

    def readText(self):
        textFileDirectory = self.txt_file[self.indexImage]
        self.annotationContentDict = dict()
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
        self.writeText()
        self.annotateImagefromText()

    def writeText(self):
        content = 'Annotation Content:\n\n'
        for key in self.annotationContentDict.keys():
            content += f'No_{key}:   {self.annotationContentDict[key][0]}\n'
        self.textBrowser.setText(content)

    def switchAnnotation(self):
        if self.directory:
            if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                self.pushButtonAnnotation.setText('Hide Annotation')
                self.plotImage(self.annotatedImage)
            else:  
                self.pushButtonAnnotation.setText('Show && Edit Annotation')
                self.plotImage(Image.open(self.curretImageDirection))
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')

    def annotateImagefromText(self):
        self.annotatedImage = Image.open(self.curretImageDirection).resize((640, 640))
        for key in self.annotationContentDict.keys():
            category = self.annotationContentDict[key][0]
            x = int(self.annotationContentDict[key][1] * 640)
            y = int(self.annotationContentDict[key][2] * 640)
            w = int(self.annotationContentDict[key][3] * 640)
            h = int(self.annotationContentDict[key][4] * 640)
            xmin = x - w//2
            ymin = y - h//2
            xmax = x + w//2
            ymax = y + h//2
            self.drawRectangularsonImage(key, category, xmin, ymin, xmax, ymax)

    def drawRectangularsonImage(self, key, category, xmin, ymin, xmax, ymax):
        draw = ImageDraw.Draw(self.annotatedImage)
        outline = tuple(map(int, self.colorIndex[self.categoryIndex.index(category)]))
        draw.rectangle([xmin, ymin, xmax, ymax], outline=outline, width=5)
        draw.text((xmin+5 , ymin+3),
                    self.categoryIndexForShort[self.categoryIndex.index(category)],
                    fill=outline,
                    font= ImageFont.truetype("arial.ttf", 20))
        xcenter = (xmin+xmax)/2 - 20
        ycenter = (ymin+ymax)/2 - 20
        draw.text((xcenter,ycenter), str(key), fill=outline, font= ImageFont.truetype("arial.ttf", 40))
       
    def plotImage(self, image2plot):
        if image2plot.size != (640, 640):
            self.loggingMain(f'Orginal image size is {image2plot.size}. Resized to (640, 640).')
            image2plot.resize((640, 640))
        image2plot = ImageQt.ImageQt(image2plot)
        image2plot = QPixmap.fromImage(image2plot)
        self.lbImg.setPixmap(image2plot)

    def nextImage(self):
        if self.directory:
            if not self.annotationChanged:
                while self.indexImage < self.numberOfImages - 1:
                    self.indexImage += 1
                    self.curretImageDirection = self.imageFiles[self.indexImage]
                    self.readText()
                    if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                        self.plotImage(Image.open(self.curretImageDirection))
                    else:
                        self.plotImage(self.annotatedImage)
                    self.pushButtonNext.setText(f'Next ({self.indexImage+1}/{self.numberOfImages})')            
                    break
            else:
                self.loggingMain(f'Please accept or cancel the modification first.')
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')

    def previousImage(self):
        if self.directory:
            if not self.annotationChanged:
                while self.indexImage > 0:
                    self.indexImage -= 1
                    self.curretImageDirection = self.imageFiles[self.indexImage]
                    self.readText()
                    if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                        self.plotImage(Image.open(self.curretImageDirection))
                    else:
                        self.plotImage(self.annotatedImage)
                    self.pushButtonNext.setText(f'Next ({self.indexImage+1}/{self.numberOfImages})')
                    break
            else:
                self.loggingMain(f'Please accept or cancel the modification first.')
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')

    def mouseDoubleClickEvent(self, event):
        if self.pushButtonAnnotation.text() == 'Hide Annotation':    # Only works when the annotation is shown
            posSelectImage = event.position().toPoint().toTuple()     # Get the position of the mouse click
            x_SelectedImage = posSelectImage[0]-10
            y_SelectedImage = posSelectImage[1]-10
            if x_SelectedImage<640 and y_SelectedImage<640:
                for key in self.annotationContentDict.keys():
                    x = int(self.annotationContentDict[key][1] * 640)
                    y = int(self.annotationContentDict[key][2] * 640)
                    w = int(self.annotationContentDict[key][3] * 640)
                    h = int(self.annotationContentDict[key][4] * 640)
                    xmin = x - w//2
                    ymin = y - h//2
                    xmax = x + w//2
                    ymax = y + h//2
                    if xmin < x_SelectedImage < xmax and ymin < y_SelectedImage < ymax:      # if the click is inside the b-box
                        self.annotatingKey = key
                        self.sendValueToSub.emit(self.annotatingKey)
                        self.AnnotationWindow.show()
                        break

    def modificationAnnotation(self, decision):
        if decision == 'Delete':
            del self.annotationContentDict[self.annotatingKey]
            self.annotationContentDict = dict(enumerate(self.annotationContentDict.values()))
            self.annotationContentDict = {k: v for k, v in self.annotationContentDict.items()}
            self.writeText()
            self.annotateImagefromText()
            self.plotImage(self.annotatedImage)
            self.loggingMain(f'Annotation No.{self.annotatingKey} is deleted. \nClick Accept to save the change.')
            self.annotationChanged = True
        else:
            self.annotationContentDict[self.annotatingKey][0] = decision
            self.writeText()
            self.annotateImagefromText()
            self.plotImage(self.annotatedImage)
            self.loggingMain(f'Annotation No.{self.annotatingKey} is modified to {decision}. \nClick Accept to save the change.')
            self.annotationChanged = True

    def acceptAnnotationMain(self):
        if self.directory:
            if self.annotationChanged:
                with open(self.txt_file[self.indexImage], 'w') as file:
                    for key in self.annotationContentDict.keys():
                        category = self.categoryIndex.index(self.annotationContentDict[key][0])
                        x = self.annotationContentDict[key][1]
                        y = self.annotationContentDict[key][2]
                        w = self.annotationContentDict[key][3]
                        h = self.annotationContentDict[key][4]
                        file.write(f'{category} {x} {y} {w} {h}\n')
                self.pushButtonNext.setEnabled(True)
                self.pushButtonPrevious.setEnabled(True)
                self.annotationChanged = False
                self.loggingMain(f'Annotation is accepted.The txt file is renewed.')
            else:
                self.loggingMain(f'No modification is made.')
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')
        
    def cancelAnnotationMain(self):
        if self.directory:
            if self.annotationChanged:
                self.pushButtonNext.setEnabled(True)
                self.pushButtonPrevious.setEnabled(True)
                self.annotationChanged = False
                self.readText()
                if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                    self.plotImage(Image.open(self.curretImageDirection))
                else:
                    self.plotImage(self.annotatedImage)
                self.loggingMain(f'Annotation is cancelled.')
            else:
                self.loggingMain(f'No modification is to be canceled.')
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')
    
    def sendValue(self, value):
        self.sendValueToSub.emit(value)

class AnnotationWindow(QWidget, Ui_AnnotationWindow):
    sendValueToMain = Signal(object)

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setComboBox()
        self.setTextToPlot
        self.pushButtonAccept.setEnabled(False)
        self.bind()

    def bind(self):
        self.comboBoxDecision.currentIndexChanged.connect(self.changeLabel)
        self.pushButtonAccept.clicked.connect(self.acceptAnnotation)
        self.pushButtonCancel.clicked.connect(self.cancelAnnotation)
        self.sendValueToMain.connect(self.parent.modificationAnnotation)

    def setTextToPlot(self,value):
        self.key = value
        self.labelForInstance.setText(f'No.{self.key} instance is to be ...')
        self.labelForDecision.setText(f'{self.comboBoxDecision.currentText()}')

    def setComboBox(self):
        itemList_combobox = ['Select Decision']
        itemList_combobox.extend(self.parent.categoryIndex)
        itemList_combobox.append('Delete')
        self.comboBoxDecision.addItems(itemList_combobox)

    def changeLabel(self):
        self.labelForDecision.setText(f'{self.comboBoxDecision.currentText()}')
        if self.comboBoxDecision.currentText() != 'Select Decision': 
            self.pushButtonAccept.setEnabled(True)

    def acceptAnnotation(self):
        if self.comboBoxDecision.currentText() != 'Select Decision':
            self.sendValueToMain.emit(self.comboBoxDecision.currentText())
            self.close()        

    def cancelAnnotation(self):
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()