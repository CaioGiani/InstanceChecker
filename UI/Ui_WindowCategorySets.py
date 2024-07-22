from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QHBoxLayout
import sys

class EditableTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['Category', 'Acronym', 'Color'])
        self.layout.addWidget(self.table_widget)

        self.input_layout = QHBoxLayout()
        
        self.input_line1 = QLineEdit()
        self.input_line1.setPlaceholderText("Category")
        self.input_layout.addWidget(self.input_line1)

        self.input_line2 = QLineEdit()
        self.input_line2.setPlaceholderText("Acronym")
        self.input_layout.addWidget(self.input_line2)

        self.input_line3 = QLineEdit()
        self.input_line3.setPlaceholderText("Color")
        self.input_layout.addWidget(self.input_line3)

        self.layout.addLayout(self.input_layout)

        self.add_button = QPushButton("Add Row")
        self.add_button.clicked.connect(self.add_row)
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete Selected Row")
        self.delete_button.clicked.connect(self.delete_row)
        self.layout.addWidget(self.delete_button)

        self.last_Layout = QHBoxLayout()

        self.accept_button = QPushButton("Accept")
        self.accept_button.clicked.connect(self.on_accept_button_clicked)
        self.last_Layout.addWidget(self.accept_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.on_cancel_button_clicked)
        self.last_Layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.last_Layout)

    def add_row(self):
        text1 = self.input_line1.text()
        text2 = self.input_line2.text()
        text3 = self.input_line3.text()
        if text1 and text2 and text3:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(text1))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(text2))
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(text3))
            self.input_line1.clear()
            self.input_line2.clear()
            self.input_line3.clear()

    def delete_row(self):
        selected_items = self.table_widget.selectedItems()
        if selected_items:
            row = self.table_widget.row(selected_items[0])
            self.table_widget.removeRow(row)
            self.update_indexes()

    def update_indexes(self):
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(row + 1)))

    def on_accept_button_clicked(self):
        pass

    def on_cancel_button_clicked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditableTableWidget()
    window.show()
    sys.exit(app.exec())
