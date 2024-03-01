from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import pyqtSignal
from Models.rgb import RGB
from UI.navigation_bar import NavigationBar
from UI.slider_container import SliderContainer


class MainWindow(QMainWindow):
    sliderValueChanged = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Control")
        self.isSliderPressed = False
        self.isKitchenLightSelected = False
        self.isOfficeLightSelected = True
        
        # Navigation bar
        self.navbar = NavigationBar()
        self.navbar.officeLightSelected.connect(self.officeLightSelected)
        self.navbar.kitchenLightSelected.connect(self.kitchenLightSelected)
        
        # Selection Label
        self.selectionLabel = QLabel("Office Light")

        # Sliders container 
        layoutSliders = QVBoxLayout()
        self.slider_container = SliderContainer()
        self.slider_container.sliderValue.connect(self.updateSliderValues)
        self.slider_container.isSliderPressed.connect(self.sliderPressed)
        layoutSliders.addWidget(self.slider_container)
        
        # Main widget layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.navbar)
        mainLayout.addWidget(self.selectionLabel)
        mainLayout.addLayout(layoutSliders)
        
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
        self.resize(500,300)

    def updateSliderValues(self, red, green, blue):
        self.sliderValueChanged.emit(red, green, blue)
    
    def updateSliders(self, rgb: RGB):
        self.slider_container.updateSliders(rgb.red, rgb.green, rgb.blue)

    def sliderPressed(self, value):
        self.isSliderPressed = value
        
    def officeLightSelected(self):
        self.isKitchenLightSelected = False
        self.isOfficeLightSelected = True
        self.selectionLabel.setText("Office Light")
        
    def kitchenLightSelected(self):
        self.isKitchenLightSelected = True
        self.isOfficeLightSelected = False
        self.selectionLabel.setText("Kitchen Light")
        