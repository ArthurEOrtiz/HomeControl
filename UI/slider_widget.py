from PyQt5.QtWidgets import QSlider, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import Qt, pyqtSignal

class SliderWidget(QWidget):
    sliderValueChanged = pyqtSignal(int)
    isSliderPressed = pyqtSignal(bool)
    
    def __init__(self, label_text):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel(label_text)
        label.setStyleSheet("padding: 10px;")
        layout.addWidget(label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setValue(127)
        self.slider.setSingleStep(1)
        self.slider.setStyleSheet("padding: 10px;")
        self.slider.valueChanged.connect(self.updateSliderValue)
        self.slider.sliderPressed.connect(self.sliderPressed)
        self.slider.sliderReleased.connect(self.sliderReleased)
        layout.addWidget(self.slider)

        self.setLayout(layout)

    def updateSliderValue(self):
        value = self.slider.value()
        self.sliderValueChanged.emit(value)

    def setValue(self, value):
        self.slider.setValue(value)

    def getValue(self):
        return self.slider.value()

    def sliderPressed(self):
        self.isSliderPressed.emit(True)

    def sliderReleased(self):
        self.isSliderPressed.emit(False)
