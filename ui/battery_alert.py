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

        max_label = QLabel('Set Alert For Maximum Battery %')
        min_label = QLabel('Set Alert For Minimum Battery %')

        self.max_percent = QSlider(Qt.Orientation.Horizontal, self)
        self.max_percent.setMinimum(0)
        self.max_percent.setMaximum(100)
        self.max_percent.setValue(75)
        self.max_percent.valueChanged.connect(self.max_slider_value)
        
        self.min_percent = QSlider(Qt.Orientation.Horizontal, self)
        self.min_percent.setMinimum(0)
        self.min_percent.setMaximum(100)
        self.min_percent.setValue(25)
        self.min_percent.valueChanged.connect(self.min_slider_value)

        self.max_edit = QLineEdit(str(self.max_percent.value()) + '%')
        self.max_edit.setMaximumWidth(50)
        self.max_edit.setMaximumHeight(50)
        
        self.min_edit = QLineEdit(str(self.min_percent.value()) + '%')
        self.min_edit.setMaximumWidth(50)
        self.min_edit.setMaximumHeight(50)

        self.button = QPushButton('OK')

        max_value_slider_layout = QHBoxLayout()
        max_value_slider_layout.addWidget(self.max_edit)
        max_value_slider_layout.addWidget(self.max_percent)
        
        min_value_slider_layout = QHBoxLayout()
        min_value_slider_layout.addWidget(self.min_edit)
        min_value_slider_layout.addWidget(self.min_percent)

        max_layout = QVBoxLayout()
        max_layout.addWidget(max_label)
        max_layout.addLayout(max_value_slider_layout)
        
        min_layout = QVBoxLayout()
        min_layout.addWidget(min_label)
        min_layout.addLayout(min_value_slider_layout)


        layout = QVBoxLayout()
        layout.addLayout(max_layout)
        layout.addLayout(min_layout)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def max_slider_value(self):
        self.max_edit.setText(str(self.max_percent.value()) + '%');

    def min_slider_value(self):
        self.min_edit.setText(str(self.min_percent.value()) + '%')