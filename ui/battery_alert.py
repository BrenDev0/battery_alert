from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class Battery_alert(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Battery Alert')
        self.setMaximumWidth(500)
        self.setMinimumWidth(500)
        self.setMaximumHeight(300)
        self.setMinimumHeight(300)

        max_edit = QLineEdit()
        max_edit.setMaximumWidth(50)
        max_edit.setMaximumHeight(50)

        max_percent = QSlider(Qt.Orientation.Horizontal, self)

        max_layout = QHBoxLayout()
        max_layout.addWidget(max_edit)
        max_layout.addWidget(max_percent)

        layout = QVBoxLayout()
        layout.addLayout(max_layout)

        self.setLayout(layout)

    def hide_clicked(self):
        self.hide()