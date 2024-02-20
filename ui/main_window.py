from PyQt5.QtWidgets import QMainWindow, QSlider, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt, pyqtSignal

from Models.rgb import RGB

class MainWindow(QMainWindow):
    sliderValueChanged = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Control")
        self.isSliderPressed = False

        layoutSliders = QVBoxLayout()

        labelRed = QLabel("Red")
        labelRed.setStyleSheet("padding: 10px;")
        layoutSliders.addWidget(labelRed)
        
        self.sliderRed = QSlider(Qt.Horizontal)
        self.sliderRed.setMinimum(0)
        self.sliderRed.setMaximum(255)
        self.sliderRed.setValue(127)
        self.sliderRed.setSingleStep(1)
        self.sliderRed.setStyleSheet("padding: 10px;")
        self.sliderRed.valueChanged.connect(self.updateSliderValues)
        self.sliderRed.sliderPressed.connect(self.sliderPressed)
        self.sliderRed.sliderReleased.connect(self.sliderReleased)
        layoutSliders.addWidget(self.sliderRed)
        
        labelGreen = QLabel("Green")
        labelGreen.setStyleSheet("padding: 10px;")
        layoutSliders.addWidget(labelGreen)
        
        self.sliderGreen = QSlider(Qt.Horizontal)
        self.sliderGreen.setMinimum(0)
        self.sliderGreen.setMaximum(255)
        self.sliderGreen.setValue(127)
        self.sliderGreen.setSingleStep(1)
        self.sliderGreen.setStyleSheet("padding: 10px;")
        self.sliderGreen.valueChanged.connect(self.updateSliderValues)
        self.sliderGreen.sliderPressed.connect(self.sliderPressed)
        self.sliderGreen.sliderReleased.connect(self.sliderReleased)
        layoutSliders.addWidget(self.sliderGreen)
        
        labelBlue = QLabel("Blue")
        labelBlue.setStyleSheet("padding: 10px;")
        layoutSliders.addWidget(labelBlue)
        
        self.sliderBlue = QSlider(Qt.Horizontal)
        self.sliderBlue.setMinimum(0)
        self.sliderBlue.setMaximum(255)
        self.sliderBlue.setValue(127)
        self.sliderBlue.setSingleStep(1)
        self.sliderBlue.setStyleSheet("padding: 10px;")
        self.sliderBlue.valueChanged.connect(self.updateSliderValues)
        self.sliderBlue.sliderPressed.connect(self.sliderPressed)
        self.sliderBlue.sliderReleased.connect(self.sliderReleased)
        layoutSliders.addWidget(self.sliderBlue)

        widget = QWidget()
        
        widget.setLayout(layoutSliders)

        self.setCentralWidget(widget)
        self.resize(500,300)

    def updateSliderValues(self):
        red = self.sliderRed.value()
        green = self.sliderGreen.value()
        blue = self.sliderBlue.value()
        self.sliderValueChanged.emit(red, green, blue)

    def getSliderValues(self):
        red = self.sliderRed.value()
        green = self.sliderGreen.value()
        blue = self.sliderBlue.value()
        return red, green, blue
    
    def updateSliders(self, rgb: RGB):
        self.sliderRed.setValue(rgb.red)
        self.sliderGreen.setValue(rgb.green)
        self.sliderBlue.setValue(rgb.blue)

    def sliderPressed(self):
        self.isSliderPressed = True
        
    def sliderReleased(self):
        self.isSliderPressed = False
