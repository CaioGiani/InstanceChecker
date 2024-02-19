from PySide6.QtWidgets import QApplication, QWidget,QComboBox, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        cb = QComboBox()
        cb.addItems(['item1','item2','item3'])
        cb.currentIndexChanged.connect(self.showName)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)

    def showName(self,name):
        print(name)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec()