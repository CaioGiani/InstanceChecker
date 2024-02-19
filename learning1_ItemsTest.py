from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # btn = QPushButton('button',self)
        # btn.setGeometry(0,0,200,100)
        # btn.setToolTip('这是一个按钮')
        # btn.setText('按钮')

        # mainlayout = QVBoxLayout()
        # lb = QLabel('label')
        # lb.setText('标签')
        # lb.setAlignment(Qt.Alignment.AlignCenter)
        # mainlayout.addWidget(lb)
        # self.setCentralWidget(lb)

        line = QLineEdit(self)
        line.setPlaceholderText('请输入内容')
       

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()