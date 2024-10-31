from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsScene, QPushButton, QLabel, 
     QVBoxLayout, QLineEdit, QFileDialog, QTextBrowser, QWidget, QMessageBox, QRubberBand, 
     QGraphicsPixmapItem, QGraphicsView, QGraphicsScene)
from PySide6.QtCore import Qt, Signal, QRect, QSize
import os
from PySide6.QtGui import QPixmap, QIcon, QActionGroup, QPainter
from UI.Ui_WindowMain_multi_copy import Ui_MainWindow
from UI.Ui_WindowAnnotation import Ui_AnnotationWindow
from PIL import Image, ImageQt, ImageDraw, ImageFont
from shapeDraft import AnchorPoint, AnnotationBuilder

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
        self.size_view = (1041, 831) 
        ''' 这里可以看看怎么用yaml文件来存储这些信息'''
        # self.categoryIndex = [  'BiologicalColonization',                  'Plant',          'Discoloration',              'Crust&Deposit',
        #                         'Subflorescence & Efflorescence',       'Graffiti',          'Alveolization',                    'Erosion',
        #                         'Peeling',                          'Delamination',                  'Crack',             'Disintegration']
        # self.categoryIndexForShort = [  'COL',          'PLT',         'CHR',     'CRU',
        #                                 'SNE',          'GRA',         'ALV',     'ERO',
        #                                 'PEL',          'DEL',         'CRA',      'DIS']
        # self.colorIndex = [ [196.36, 182.69, 100.75774],    [108.79, 114.33, 55.32],    [206.8, 130.08, 131.81],    [248.904, 92.56, 200.51],
        #                     [156.76, 47.006, 79.201],       [131.24, 105.24, 145.38],   [192.83, 11.103, 253.69],   [252.85, 235.66, 83.937],
        #                     [150.046, 216.47, 203.75],      [40.367, 155.43, 218.26],   [254.99, 120.09, 32.34],    [25.5, 241.7, 10.47]]   
        
        #  
        self.categoryIndex = [  'Smoke Detector',                  'Alarm Button',          'Fire Extinguisher',              'Ceiling Light',
                                'FM Power Point (Plug)',       'Command Point (Switch)',          'Security Cameras']
        self.categoryIndexForShort = [  'SDT',          'ABT',         'FEX',     'LGT',
                                        'PLUG',          'SWT',         'CAM']
        self.colorIndex = [ [196.36, 182.69, 100.75774],    [108.79, 114.33, 55.32],    [206.8, 130.08, 131.81],    [248.904, 92.56, 200.51],
                            [156.76, 47.006, 79.201],       [131.24, 105.24, 145.38],   [192.83, 11.103, 253.69]]
                            


        self.directory = False 
        self.graphicsViewAnnotation = AnnotationBuilder(self)
        self.layout().addWidget(self.graphicsViewAnnotation)
        self.graphicsViewAnnotation.setGeometry(10, 30, 1041, 831)
        self.annotationMethod_action_group = QActionGroup(self)
        self.annotationMethod_action_group.addAction(self.actionNormal_box)
        self.annotationMethod_action_group.addAction(self.actionOriented_box)
        self.annotationMethod_action_group.addAction(self.actionEllipse)
        self.annotationMethod_action_group.addAction(self.action4_side_polygon)
        self.annotationMethod_action_group.addAction(self.actionMulti_side_polygon)
        self.annotationMethod_action_group.setExclusive(True)
        self.annotationMethod = 4
        self.annotationMethod_action_group.actions()[self.annotationMethod-1].setChecked(True)
        self.annotationMtethodPreparation(self.annotationMethod)
        print(f'annotation method is {self.annotationMethod}')     
        self.AnnotationWindow = AnnotationWindow(self)    
        self.thresholdIoU = 0.5
        self.bind()

  
    def bind(self):
        self.annotationMethod_action_group.triggered.connect(self.selectAnnotation)      
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

    def selectAnnotation(self, action):
        annotationList = ['Normal box', 'Oriented box', 'Ellipse', '4-side polygon', 'Multi-side polygon']
        selectedAction = self.annotationMethod_action_group.checkedAction()
        selectedMethod = annotationList.index(selectedAction.text()) + 1
        if selectedMethod != self.annotationMethod:
            self.annotationMethod = selectedMethod
            self.annotationMtethodPreparation(self.annotationMethod)

    def annotationMtethodPreparation(self, method):
        self.loggingMain(f'Annotation method is set to {self.annotationMethod_action_group.checkedAction().text()}.')
        self.graphicsViewAnnotation.reset()
        self.regionOfInterest = None
        if self.directory:
            if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                self.plotImage(self.currentImage)
            else:
                self.plotImage(self.annotatedImage)
        if method == 1:    #Normal box
            self.rubberBandAnnotation = QRubberBand(QRubberBand.Rectangle, self.graphicsViewAnnotation)
            self.rubberBandAnnotation.setStyleSheet("border: 2px solid red;")
            self.regionOfInterest_startpoint = None
            print('annotation for normal box is activated')            
        if method == 2:    #Oriented box
            pass
        if method == 3:     #Ellipse
            pass
        if method == 4 or method == 5:     #4-side polygon or Multi-side polygon 
            self.graphicsViewAnnotation.sideLimitation = method
            # self.graphicsViewAnnotation = AnnotationBuilder(method)              
            print('annotation for polygon is activated')

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

            self.currentImageDirection = self.imageFiles[self.indexImage]
            self.currentImage = Image.open(self.currentImageDirection).resize(self.size_view)
            self.plotImage(self.currentImage)
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
                if len(line) == 5:                          #for normal box, category:str, x:float, y, w, h of the annotation
                    category = int(line[0])
                    x = float(line[1])
                    y = float(line[2])
                    w = float(line[3])
                    h = float(line[4])
                    self.annotationContentDict[i] = [self.categoryIndex[category], x, y, w, h]   
                elif len(line) == 6:                         #for oriented box and ellipse, category:str, x:float, y, w, h, theta:int of the annotation
                    category = int(line[0])
                    x = float(line[1])
                    y = float(line[2])
                    w = float(line[3])
                    h = float(line[4])
                    theta = int(line[5])
                    self.annotationContentDict[int(line[5])] = [self.categoryIndex[category], x, y, w, h, theta]  
                elif len(line) >= 9 and len(line) % 2 == 1:                 #for multi-side polygon, category:str, x1:float, y1, x2, y2, x3, y3, ... of the annotation
                    category = int(line[0])
                    self.annotationContentDict[i] = [self.categoryIndex[category]]
                    self.annotationContentDict[i].extend([float(line[j]) for j in range(1, len(line))])
        self.writeText()
        self.currentImage = Image.open(self.currentImageDirection).resize(self.size_view)
        self.annotateImagefromText()

    def writeText(self):
        content = 'Annotation Content:\n\n'
        shape = None
        for key in self.annotationContentDict.keys():
            num_param = len(self.annotationContentDict[key])-1
            if num_param == 4:
                shape = 'box'
            if num_param == 5:
                shape = 'orient'
            if num_param == 8:
                shape = 'poly'
            if num_param > 8:
                shape = 'multi'
            content += f'{key}_{shape}: {self.annotationContentDict[key][0]}\n'
        self.textBrowser.setText(content)

    def switchAnnotation(self):
        if self.directory:
            if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                self.pushButtonAnnotation.setText('Hide Annotation')
                self.plotImage(self.annotatedImage)
                self.graphicsViewAnnotation.clickPermission = True
            else:  
                self.pushButtonAnnotation.setText('Show && Edit Annotation')
                self.graphicsViewAnnotation.clickPermission = False
                self.graphicsViewAnnotation.reset()                
                self.plotImage(self.currentImage)
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')

    def annotateImagefromText(self):
        self.annotatedImage = self.currentImage.copy()
        self.annotatedImage = self.annotatedImage.convert('RGB')
        for key in self.annotationContentDict.keys():
            if len(self.annotationContentDict[key]) == 5:
                category = self.annotationContentDict[key][0]
                x = int(self.annotationContentDict[key][1] * self.size_view[0])
                y = int(self.annotationContentDict[key][2] * self.size_view[1])
                w = int(self.annotationContentDict[key][3] * self.size_view[0])
                h = int(self.annotationContentDict[key][4] * self.size_view[1])
                xmin = x - w//2
                ymin = y - h//2
                xmax = x + w//2
                ymax = y + h//2
                self.drawRectangularsonImage(key, category, xmin, ymin, xmax, ymax)
            elif len(self.annotationContentDict[key]) == 6:
                category = self.annotationContentDict[key][0]
                x = int(self.annotationContentDict[key][1] * self.size_view[0])
                y = int(self.annotationContentDict[key][2] * self.size_view[1])
                w = int(self.annotationContentDict[key][3] * self.size_view[0])
                h = int(self.annotationContentDict[key][4] * self.size_view[1])
                theta = self.annotationContentDict[key][5]
                if self.annotationMethod == 2:                  
                    self.drawOrientedBoxonImage(key, category, x, y, w, h, theta)
                elif self.annotationMethod == 3:
                    self.drawEllipseonImage(key, category, x, y, w, h, theta)
            elif len(self.annotationContentDict[key]) >= 9 and len(self.annotationContentDict[key]) % 2 == 1:
                category = self.annotationContentDict[key][0]
                points = []
                for i in range(1, len(self.annotationContentDict[key]), 2):
                    x = int(self.annotationContentDict[key][i] * self.size_view[0])
                    y = int(self.annotationContentDict[key][i+1] * self.size_view[1])
                    points.extend([x, y])
                self.drawMultiSidePolygononImage(key, category, *points)

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
        cx = (xmin + xmax) / 2
        cy = (ymin + ymax) / 2
        txt = f'{self.categoryIndexForShort[self.categoryIndex.index(category)]}'
        draw.text((cx-20,cy-10), txt,fill=outline, font= ImageFont.truetype("arial.ttf", 10))
        draw.text((cx+10,cy-15), str(key), fill=outline, font= ImageFont.truetype("arial.ttf", 20))

    def drawOrientedBoxonImage(self, key, category, x, y, w, h, theta):
        pass

    def drawEllipseonImage(self, key, category, x, y, w, h, theta):
        pass

    def drawMultiSidePolygononImage(self, key, category, *points):
        '''
        draw polygons with multiple sides (including 4-side) on the image with the category and the key
        '''
        draw = ImageDraw.Draw(self.annotatedImage)
        outline = tuple(map(int, self.colorIndex[self.categoryIndex.index(category)]))
        points_pairs = [(points[i], points[i+1]) for i in range(0, len(points), 2)]
        draw.polygon(points_pairs, outline=outline, width=5) 
        cx = sum([point[0] for point in points_pairs]) / len(points_pairs)
        cy = sum([point[1] for point in points_pairs]) / len(points_pairs)
        txt = f'{self.categoryIndexForShort[self.categoryIndex.index(category)]}'
        draw.text((cx-20,cy-10), txt,fill=outline, font= ImageFont.truetype("arial.ttf", 10))
        draw.text((cx+10,cy-15), str(key), fill=outline, font= ImageFont.truetype("arial.ttf", 20))

    def plotImage(self, image2plot):
        if image2plot.size != self.size_view:
            self.loggingMain(f'Orginal image size is {image2plot.size}. Resized to ({self.size_view[0],self.size_view[1]}).')
            image2plot.resize(self.size_view)
        img_bg = QGraphicsPixmapItem(QPixmap.fromImage(ImageQt.ImageQt(image2plot)))
        self.graphicsViewAnnotation.scene().clear()
        self.graphicsViewAnnotation.scene().addItem(img_bg)
     
    def nextImage(self):
        if self.directory:
            if not self.annotationChanged:
                while self.indexImage < self.numberOfImages - 1:
                    self.indexImage += 1
                    self.currentImageDirection = self.imageFiles[self.indexImage]
                    self.readText()
                    if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                        self.plotImage(self.currentImage)
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
                    self.currentImageDirection = self.imageFiles[self.indexImage]
                    self.readText()
                    if self.pushButtonAnnotation.text() == 'Show && Edit Annotation':
                        self.plotImage(self.currentImage)
                    else:
                        self.plotImage(self.annotatedImage)
                    self.pushButtonNext.setText(f'Next ({self.indexImage+1}/{self.numberOfImages})')
                    break
            else:
                self.loggingMain(f'Please accept or cancel the modification first.')
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')
 
    def modificationAnnotation(self, decision):
        if self.annotatingKey == len(self.annotationContentDict):
            if decision == 'Deleted':
                self.loggingMain(f'No annotation is made.')                
            else:
                if self.annotationMethod == 1:
                    x = self.regionOfInterest[0]/self.size_view[0] + (self.regionOfInterest[2]-self.regionOfInterest[0])/self.size_view[0]/2
                    y = self.regionOfInterest[1]/self.size_view[1] + (self.regionOfInterest[3]-self.regionOfInterest[1])/self.size_view[1]/2
                    w = (self.regionOfInterest[2]-self.regionOfInterest[0])/self.size_view[0]
                    h = (self.regionOfInterest[3]-self.regionOfInterest[1])/self.size_view[1]
                    self.annotationContentDict[self.annotatingKey] = [decision, x, y, w, h]
                if self.annotationMethod == 4 or self.annotationMethod == 5:
                    #分别对resgionOfInterest中的xy进行处理，得到多边形的坐标
                    points = []
                    for i in range(0, len(self.regionOfInterest), 2):
                        x = self.regionOfInterest[i]/self.size_view[0]
                        y = self.regionOfInterest[i+1]/self.size_view[1]
                        points.extend([x, y])
                    self.annotationContentDict[self.annotatingKey] = [decision]
                    self.annotationContentDict[self.annotatingKey].extend(points)
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
                        file.write(f'{self.categoryIndex.index(self.annotationContentDict[key][0])} ')
                        num_parameters = len(self.annotationContentDict[key])
                        key_temp = 1
                        while key_temp < num_parameters:
                            value = round(float(self.annotationContentDict[key][key_temp]), 3)
                            if key_temp == num_parameters - 1:
                                file.write(f'{value}\n')
                            else:
                                file.write(f'{value} ')
                            key_temp += 1
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
                    self.plotImage(self.currentImage)
                else:
                    self.plotImage(self.annotatedImage)
                self.loggingMain(f'Annotation is cancelled.')
            else:
                self.loggingMain(f'No modification is to be canceled.')
        else:
            self.loggingMain(f'Please click [File] - [Open] to load files first.')
    
    def sendValue(self, value):
        self.sendValueToSub.emit(value)
       
    def mousePressEvent(self, event):
        if self.pushButtonAnnotation.text() == 'Hide Annotation':
            if self.annotationMethod == 1:
                self.regionOfInterest_startpoint = event.position().toPoint()
                print(f'start point is {self.regionOfInterest_startpoint}')              
                self.rubberBandAnnotation.setGeometry(self.regionOfInterest_startpoint.x()-10, self.regionOfInterest_startpoint.y()-30, 0, 0)
            elif self.annotationMethod == 4 or self.annotationMethod == 5:
                self.graphicsViewAnnotation.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.pushButtonAnnotation.text() == 'Hide Annotation':
            if self.annotationMethod == 1:
                if self.regionOfInterest_startpoint:
                    selectedRect = QRect(self.regionOfInterest_startpoint.x()-10,    #exact the position
                                        self.regionOfInterest_startpoint.y()-30,
                                        event.position().toPoint().x() - self.regionOfInterest_startpoint.x(),     #relative size
                                        event.position().toPoint().y() - self.regionOfInterest_startpoint.y()
                                        )
                    self.rubberBandAnnotation.setGeometry(selectedRect.normalized())
                    self.rubberBandAnnotation.show()
                    self.rubberBandAnnotation.raise_()
                    self.rubberBandAnnotation.update()
            elif self.annotationMethod == 4 or self.annotationMethod == 5:
                self.graphicsViewAnnotation.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.pushButtonAnnotation.text() == 'Hide Annotation':
            if self.annotationMethod == 1:
                selectedRect = self.rubberBandAnnotation.geometry()
                imageRect = self.graphicsViewAnnotation.geometry()
                rectIntersected = selectedRect.intersected(imageRect)
                if selectedRect.isValid() and rectIntersected.width() > 10 and rectIntersected.height() > 10:
                    self.regionOfInterest = rectIntersected.getCoords()
                    self.loggingMain(f'New boundingbox is made, click button [+] to add the annotatation.')
                else:
                    self.rubberBandAnnotation.close()
            elif self.annotationMethod == 4 or self.annotationMethod == 5:

                self.graphicsViewAnnotation.mouseReleaseEvent(event)

    def addInstance(self):
        if self.regionOfInterest is not None:
            print(self.regionOfInterest)
            if self.annotationMethod == 1:
                #for each annotation, check the intersection over union is over a threshold
                #if yes, then the annotation is not added
                #if no, then the annotation is added
                annotationPermission = True
                xminbb = (self.regionOfInterest[0]-10)/self.size_view[0]
                yminbb = (self.regionOfInterest[1]-10)/self.size_view[1]
                xmaxbb = (self.regionOfInterest[2]-10)/self.size_view[0]
                ymaxbb = (self.regionOfInterest[3]-10)/self.size_view[1]
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
            if self.annotationMethod == 4 or self.annotationMethod == 5:
                self.graphicsViewAnnotation.reset()
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