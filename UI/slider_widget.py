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
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 10px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
                margin: 2px 0;
            }

            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #F5F5F5, stop:1 #DADADA);
                border: 1px solid #999999;
                width: 18px;
                margin: -2px 0;
                border-radius: 3px;
            }

            QSlider::add-page:horizontal {
                background: #575757;
                border: 1px solid #999999;
                height: 10px;
                margin: 2px 0;
            }

            QSlider::sub-page:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                            stop:0 #45AFE4, stop:1 #0097E0);
                border: 1px solid #999999;
                height: 10px;
                margin: 2px 0;
            }
        """)
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
