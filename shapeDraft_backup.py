import sys
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem, QGraphicsPixmapItem
from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QPolygonF, QBrush, QPen, QPainter, QPixmap

class AnchorPoint(QGraphicsEllipseItem):
    def __init__(self, x, y, radius=5):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius)
        self.setPos(x, y)
        self.setBrush(QBrush(Qt.red))
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.ItemSendsScenePositionChanges)
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.radius = radius

    def itemChange(self, change, value):
        if change == QGraphicsEllipseItem.ItemScenePositionHasChanged:
            scene = self.scene()
            if scene:
                scene.views()[0].complete_polygon()
        return super().itemChange(change, value)
    
    def contains_point(self, x, y):
        """检查指定位置 (x, y) 是否在锚点范围内"""
        return (self.x() - x) ** 2 + (self.y() - y) ** 2 <= (self.radius ** 2)

class PolygonBuilder(QGraphicsView):
    def __init__(self, sideLimitation = None):
        super().__init__()
        print("PolygonBuilder initiated")

        self.resize(1041, 831)

        self.setScene(QGraphicsScene(self))
        self.setSceneRect(0, 0, 1041, 831)
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.RubberBandDrag)  # 允许项目移动
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QGraphicsView.NoFrame)

        self.points = []  # 存储所有 AnchorPoints
        self.lines = []   # 存储用于连接 AnchorPoints 的线段
        self.is_closed = False  # 用于跟踪多边形是否已完成

        self.current_polygon = None  # 用于显示最终多边形
        self.sideLimitation = sideLimitation if sideLimitation and sideLimitation>=4 else None

        #添加背景图
        # dir_bg = r"C:\Users\Simone\Desktop\Project\github\InstanceChecker\testData\CER-BIO-VEG-CIN-0001.png"
        # img_bg = QGraphicsPixmapItem(QPixmap(dir_bg))
        # self.scene().addItem(img_bg)


    def mousePressEvent(self, event):
        logginMessage = None
        if self.is_closed:
            logginMessage = "Reset the polygon draft"
            self.reset()
            return logginMessage
        # #判断点击位置是否在scene中
        # if not self.sceneRect().contains(event.scenePos()):
        #     return
        pos = self.mapToScene(event.position().toPoint())
        x, y = pos.x(), pos.y()

        # 创建一个新的 AnchorPoint
        point = AnchorPoint(x, y)
        self.points.append(point)
        self.scene().addItem(point)

        if len(self.points) == 2:
            # 连接当前点和前一个点
            line = QGraphicsLineItem(self.points[0].x(), self.points[0].y(), x, y)
            line.setPen(QPen(Qt.black, 2))
            self.lines.append(line)
            self.scene().addItem(line)
        if len(self.points) > 2:
            if self.sideLimitation:
                if self.points[0].contains_point(x, y):
                    if len(self.points) < self.sideLimitation:
                        logginMessage = "Polygon side limitation not reached, please add more points"
                        self.scene().removeItem(self.points[-1])
                        self.points.pop()
                    elif len(self.points) == self.sideLimitation:
                        logginMessage = "Too close to the first point, please try again"
                        self.scene().removeItem(self.points[-1])
                        self.points.pop()
                elif len(self.points) < self.sideLimitation:
                    self.complete_polygon()
                elif len(self.points) == self.sideLimitation:
                    logginMessage = "Polygon side limitation reached, polygon closed"
                    self.complete_polygon()
                    self.is_closed = True
            elif self.points[0].contains_point(x, y):
                print("Polygon closed.")
                self.scene().removeItem(self.points[-1])
                self.is_closed = True
            else:
                self.complete_polygon()
                    
        super().mousePressEvent(event)  # 确保默认的鼠标事件处理不会被覆盖
        if logginMessage:
            print(logginMessage)
            return logginMessage

    def complete_polygon(self):
        if self.lines:
            # 清空直线的线
            self.scene().removeItem(self.lines.pop())
        if self.current_polygon:
            # 清空当前多边形
            self.scene().removeItem(self.current_polygon)

        polygon = QPolygonF([point.scenePos() for point in self.points])
        self.current_polygon = QGraphicsPolygonItem(polygon)
        self.current_polygon.setBrush(QBrush(Qt.transparent))
        self.current_polygon.setPen(QPen(Qt.blue, 2))
    
        self.scene().addItem(self.current_polygon)
        self.setRenderHint(QPainter.Antialiasing)


    def reset(self):
        # 重置所有状态，允许用户再次开始创建新的多边形
        for point in self.points:
            if point in self.scene().items():
                self.scene().removeItem(point)
        for line in self.lines:
            self.scene().removeItem(line)
        if self.current_polygon:
            self.scene().removeItem(self.current_polygon)

        self.points.clear()
        self.lines.clear()
        self.current_polygon = None
        self.is_closed = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PolygonBuilder()
    window.setWindowTitle("Interactive Polygon Builder with PySide6")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
