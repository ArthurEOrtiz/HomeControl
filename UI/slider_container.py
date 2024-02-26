from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from UI.slider_widget import SliderWidget

class SliderContainer(QWidget):
    sliderValue = pyqtSignal(int, int, int)  
    isSliderPressed = pyqtSignal(bool)
  
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.sliderRed = SliderWidget("Red")
        self.sliderRed.sliderValueChanged.connect(self.updateSiderValues)
        self.sliderRed.isSliderPressed.connect(self.sliderPressed)  
        layout.addWidget(self.sliderRed)

        self.sliderGreen = SliderWidget("Green")
        self.sliderGreen.sliderValueChanged.connect(self.updateSiderValues)
        self.sliderGreen.isSliderPressed.connect(self.sliderPressed)
        layout.addWidget(self.sliderGreen)

        self.sliderBlue = SliderWidget("Blue")
        self.sliderBlue.sliderValueChanged.connect(self.updateSiderValues)
        self.sliderBlue.isSliderPressed.connect(self.sliderPressed)
        layout.addWidget(self.sliderBlue)

        self.setLayout(layout)
        
    def updateSiderValues(self):
        red = self.sliderRed.getValue()
        green = self.sliderGreen.getValue()
        blue = self.sliderBlue.getValue()
        self.sliderValue.emit(red, green, blue)

    def updateSliders(self, red, green, blue):
        self.sliderRed.setValue(red)
        self.sliderGreen.setValue(green)
        self.sliderBlue.setValue(blue)
        
    def sliderPressed(self, value):
      self.isSliderPressed.emit(value)

        
