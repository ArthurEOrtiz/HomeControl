from PyQt5.QtWidgets import QMainWindow, QSlider, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Home Control")

        layoutSliders = QVBoxLayout()

        sliderRed = QSlider(Qt.Horizontal)
        sliderRed.setMinimum(0)
        sliderRed.setMaximum(255)
        layoutSliders.addWidget(sliderRed)
        
        sliderGreen = QSlider(Qt.Horizontal)
        sliderGreen.setMinimum(0)
        sliderGreen.setMaximum(255)
        layoutSliders.addWidget(sliderGreen)
        
        sliderBlue = QSlider(Qt.Horizontal)
        sliderBlue.setMinimum(0)
        sliderBlue.setMaximum(255)
        layoutSliders.addWidget(sliderBlue)

        widget = QWidget()
        
        widget.setLayout(layoutSliders)

        self.setCentralWidget(widget)