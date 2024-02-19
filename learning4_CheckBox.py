from PySide6.QtWidgets import QApplication, QWidget,QCheckBox, QVBoxLayout, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        cb = QCheckBox('select me')
        cb.stateChanged.connect(self.showState)

        btn = QPushButton('acquire state') 
        btn.clicked.connect(lambda:print(cb.isChecked()))

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        mainlayout.addWidget(btn)
        self.setLayout(mainlayout)

    def showState(self,state):
        print(state)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec()