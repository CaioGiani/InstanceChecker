from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QLineEdit, QFileDialog, QTextBrowser, QWidget, QMessageBox, QRubberBand
from PySide6.QtCore import Qt, Signal, QRect, QSize
import os
from PySide6.QtGui import QPixmap, QIcon
from UI.Ui_WindowMain import Ui_MainWindow
from UI.Ui_WindowAnnotation import Ui_AnnotationWindow
from PIL import Image, ImageQt, ImageDraw, ImageFont

# import sys
# if getattr(sys, 'frozen', False):
#     # in a PyInstaller bundle
#     basedir = os.path.dirname(sys.executable)
# else:
#     # in a normal Python environment
#     basedir = os.path.dirname(os.path.abspath(__file__)) 


basedir = os.path.dirname(__file__)

class MyWindow(QMainWindow, Ui_MainWindow):
    sendValueToSub = Signal(object)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.annotationChanged = False  
        self.categoryIndex = [  'BiologicalColonization',                  'Plant',          'Discoloration',              'Crust&Deposit',
                                'Subflorescence & Efflorescence',       'Graffiti',          'Alveolization',                    'Erosion',
                                'Peeling',                          'Delamination',                  'Crack',             'Disintegration'
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
        self.regionOfInterest = None
        self.rubberBandAnnotation = QRubberBand(QRubberBand.Rectangle, self.lbImg)
        self.rubberBandAnnotation.setStyleSheet("border: 2px solid red;")
        self.regionOfInterest_startpoint = None
        self.thresholdIoU = 0.5
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
        self.pushButtonAddInstance.clicked.connect(self.addInstance)

    def showManual(self):
        textInformation  = "Thank you for using the annotation tool.\n\n"
        textInformation += "Here are some brief instructions of how to use this app:\n\n"
        textInformation += "1. Click [File] - [Open] to load the folder of the images and txt files.\n\n"
        textInformation += "2. Click 'Show && Edit Annotation' to show the annotation of the current image.\n"
        textInformation += "   You can double click an existing box to edit previous annotation.\n\n"
        textInformation += "3. You can also drag a box and click [+] to add new annotation.\n"
        textInformation += "   Notice that the new annotation will not be added if the overlap is over 0.5.\n\n"
        textInformation += "4. Click [Accept] or [Abort] to save or cancel the modification.\n\n"
        textInformation += "5. Click 'Next' or 'Previous' to switch to the next or previous image.\n\n"
        # textInformation += "6. \n\n"
        # textInformation += "7. \n\n"
        textInformation += "In case of any question, please contact kai.zhang@polimi.it"
        QMessageBox.information(self, "User Manual", textInformation)

    def loggingMain(self, text):
        self.plainTextEditLog.appendPlainText(text)
        self.plainTextEditLog.verticalScrollBar().setValue(self.plainTextEditLog.verticalScrollBar().maximum())

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
                if not os.path.exists(checkTxtDirection):
                    self.loggingMain(f'Annotation file for {os.path.basename(file)} does not exist.')
                    open(checkTxtDirection, 'w').close()
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
        '''
        Read the txt file and store the content in a dict
        return: dict, the content of the txt file, in whcih
                key: int, the index of the annotation, starting from 0
                value: list, the category:str, x:float, y, w, h of the annotation
        '''
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
                #the dict contains the category:str, x:float, y, w, h of the annotation
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
        '''
        Draw the rectangular on the image with the category and the key
        key: int, the index of the annotation
        category: str, the category of the annotation
        xmin, ymin, xmax, ymax: int, the coordinates of the rectangular
        '''
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
        if self.annotatingKey == len(self.annotationContentDict):
            self.rubberBandAnnotation.close()
            if decision == 'Deleted':
                self.loggingMain(f'No annotation is made.')                
            else:
                x = self.regionOfInterest[0]/640 + (self.regionOfInterest[2]-self.regionOfInterest[0])/1280
                y = self.regionOfInterest[1]/640 + (self.regionOfInterest[3]-self.regionOfInterest[1])/1280
                w = (self.regionOfInterest[2]-self.regionOfInterest[0])/640
                h = (self.regionOfInterest[3]-self.regionOfInterest[1])/640
                self.annotationContentDict[self.annotatingKey] = [decision, x, y, w, h]
                self.writeText()
                self.annotateImagefromText()
                self.plotImage(self.annotatedImage)
                self.loggingMain(f'New annotation is added. \nClick Accept to save the change.')
                self.annotationChanged = True
        else:            
            if decision == 'Deleted':
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

    def markRegionOfInterest(self):
        return self.regionOfInterest

    def mousePressEvent(self, event):
        if self.pushButtonAnnotation.text() == 'Hide Annotation':
            self.regionOfInterest_startpoint = event.position().toPoint()
            self.rubberBandAnnotation.setGeometry(self.regionOfInterest_startpoint.x()-5, self.regionOfInterest_startpoint.y()-15, 0, 0)
            self.rubberBandAnnotation.show()

    def mouseMoveEvent(self, event):
        if self.pushButtonAnnotation.text() == 'Hide Annotation':
            if self.regionOfInterest_startpoint:
                selectdRect = QRect(self.regionOfInterest_startpoint.x()-5,
                                    self.regionOfInterest_startpoint.y()-15,
                                    event.position().toPoint().x() - self.regionOfInterest_startpoint.x()-5,
                                    event.position().toPoint().y() - self.regionOfInterest_startpoint.y()-15
                                    )
                self.rubberBandAnnotation.setGeometry(selectdRect.normalized())

    def mouseReleaseEvent(self, event):
        if self.pushButtonAnnotation.text() == 'Hide Annotation':
            selectedRect = self.rubberBandAnnotation.geometry()
            imageRect = self.lbImg.geometry()
            rectIntersected = selectedRect.intersected(imageRect)
            if selectedRect.isValid() and rectIntersected.width() > 40 and rectIntersected.height() > 40:
                self.regionOfInterest = rectIntersected.getCoords()
                self.loggingMain(f'New boundingbox is made, double click button [+] to add the annotatation.')
            else:
                self.rubberBandAnnotation.close()

    def addInstance(self):
        if self.regionOfInterest:
            #for each annotation, check the intersection over union is over a threshold
            #if yes, then the annotation is not added
            #if no, then the annotation is added
            annotationPermission = True
            xminbb = (self.regionOfInterest[0]-10)/640
            yminbb = (self.regionOfInterest[1]-10)/640
            xmaxbb = (self.regionOfInterest[2]-10)/640
            ymaxbb = (self.regionOfInterest[3]-10)/640
            bbNew = [xminbb, yminbb, xmaxbb, ymaxbb]
            for key in self.annotationContentDict.keys():
                xminanno = self.annotationContentDict[key][1] - self.annotationContentDict[key][3]/2
                yminanno = self.annotationContentDict[key][2] - self.annotationContentDict[key][4]/2
                xmaxanno = self.annotationContentDict[key][1] + self.annotationContentDict[key][3]/2
                ymaxanno = self.annotationContentDict[key][2] + self.annotationContentDict[key][4]/2
                bbPrev = [xminanno, yminanno, xmaxanno, ymaxanno]
                if bbIntersectionofEach(bbNew, bbPrev)[0] > self.thresholdIoU or bbIntersectionofEach(bbNew, bbPrev)[1] > self.thresholdIoU:
                    self.loggingMain(f'The new annotation is overlapped with instance {key}.')
                    annotationPermission = False
                    break
            if annotationPermission:
                self.annotatingKey = len(self.annotationContentDict)
                self.sendValueToSub.emit('new')
                self.AnnotationWindow.show()
            

        else:
            self.loggingMain(f'Please mark the bounding box first.')


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
        if value == 'new':
            self.labelForInstance.setText(f'New instance is to be ...')
            self.labelForDecision.setText(f'{self.comboBoxDecision.currentText()}')
        else:
            self.key = value
            self.labelForInstance.setText(f'No.{self.key} instance is to be ...')
            self.labelForDecision.setText(f'{self.comboBoxDecision.currentText()}')

    def setComboBox(self):
        itemList_combobox = ['---Select Decision---']
        itemList_combobox.extend(self.parent.categoryIndex)
        itemList_combobox.append('Deleted')
        self.comboBoxDecision.addItems(itemList_combobox)

    def changeLabel(self):
        self.labelForDecision.setText(f'{self.comboBoxDecision.currentText()}')
        if self.comboBoxDecision.currentText() != '---Select Decision---': 
            self.pushButtonAccept.setEnabled(True)

    def acceptAnnotation(self):
        if self.comboBoxDecision.currentText() != '---Select Decision---':
            self.sendValueToMain.emit(self.comboBoxDecision.currentText())
            self.close()        

    def cancelAnnotation(self):
        self.close()

def bbIntersectionofEach(bb1, bb2):
    '''
    Calculate the intersection over union of two bounding boxes
    bb1, bb2: list, [xmin, ymin, xmax, ymax]
    return: float, the intersection over union of the two bounding boxes
    '''
    x1, y1, x2, y2 = bb1
    x3, y3, x4, y4 = bb2
    x5 = max(x1, x3)
    y5 = max(y1, y3)
    x6 = min(x2, x4)
    y6 = min(y2, y4)
    intersection = max(0, x6 - x5) * max(0, y6 - y5)
    area1 = (x2 - x1) * (y2 - y1)
    area2 = (x4 - x3) * (y4 - y3)
    return [intersection/area1, intersection/area2]

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(os.path.join(basedir, 'Checker.ico')))
    window = MyWindow()
    window.show()
    app.exec()