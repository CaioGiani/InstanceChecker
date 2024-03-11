from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("滑鼠事件")
        self.lb = ImageBox(self)
        self.lb.setGeometry(100, 100, 200, 100)
        self.lb.setText("滑鼠事件")
        self.setCentralWidget(self.lb)

class ImageBox(QLabel):

    def mousePressEvent(self, event):
        pos = event.position().toPoint().toTuple()
        if event.button() == Qt.LeftButton:
            self.setText(f"滑鼠左鍵被按下了，\n座標：{pos}")
        if event.button() == Qt.RightButton:
            self.setText(f"按下滑鼠右鍵，\n座標：{pos}")

    def mouseMoveEvent(self, event):
        pos = event.position().toPoint().toTuple()
        self.setText(f"滑鼠移動中，座標：{pos}")

    def mouseReleaseEvent(self, event):
        gpos = event.globalPosition().toPoint().toTuple()
        self.setText(f"滑鼠提起來了！！，全域座標：{gpos}")
       

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

