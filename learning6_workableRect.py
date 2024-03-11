import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsRectItem, QApplication
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)

# Draw a rectangle item, setting the dimensions.
rect = QGraphicsRectItem(0, 0, 200, 50)

# Set the origin (position) of the rectangle in the scene.
rect.setPos(50, 20)

# Define the pen (line)
pen = QPen(Qt.GlobalColor.cyan)
pen.setWidth(10)
rect.setPen(pen)

# Add the items to the scene. Items are stacked in the order they are added.
scene.addItem(rect)

rect.setFlag(QGraphicsItem.ItemIsMovable)
rect.setFlag(QGraphicsItem.ItemIsFocusable)


view = QGraphicsView(scene)
view.show()
app.exec()