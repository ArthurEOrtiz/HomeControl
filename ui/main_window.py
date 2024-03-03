from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
from Models.rgb import RGB
from UI.slider_container import SliderContainer

class MainWindow(QMainWindow):
    sliderValueChanged = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Control")
        self.isSliderPressed = False

        layoutSliders = QVBoxLayout()
        
        self.slider_container = SliderContainer()
        self.slider_container.sliderValue.connect(self.updateSliderValues)
        self.slider_container.isSliderPressed.connect(self.sliderPressed)
        
        layoutSliders.addWidget(self.slider_container)

        widget = QWidget()
        
        widget.setLayout(layoutSliders)

        self.setCentralWidget(widget)
        self.resize(500,300)

    def updateSliderValues(self, red, green, blue):
        self.sliderValueChanged.emit(red, green, blue)
    
    def updateSliders(self, rgb: RGB):
        self.slider_container.updateSliders(rgb.red, rgb.green, rgb.blue)

    def sliderPressed(self, value):
        self.isSliderPressed = value
        