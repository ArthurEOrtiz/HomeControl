from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
from Models.rgb import RGB
from UI.drop_down_widget import DropdownWidget
from UI.on_off_button import OnOffButton
from UI.slider_container import SliderContainer

class MainWindow(QMainWindow):
    sliderValueChanged = pyqtSignal(int, int, int)
    selection = pyqtSignal(str)
    turnOnDevice = pyqtSignal()
    turnOffDevice = pyqtSignal()    

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Control")
        self.isSliderPressed = False

        self.main_window_layout = QVBoxLayout()
        
        options = ["Office Light", "Kitchen Light"]
        self.dropdown = DropdownWidget(options)
        self.dropdown.selectionChanged.connect(self.handleDropdownSelection)
        
        self.main_window_layout.addWidget(self.dropdown)
        
        self.slider_container = SliderContainer()
        self.slider_container.sliderValue.connect(self.updateSliderValues)
        self.slider_container.isSliderPressed.connect(self.sliderPressed)
        
        self.main_window_layout.addWidget(self.slider_container)
        
        self.on_off_button = OnOffButton()
        self.on_off_button.turnOn.connect(self.turn_on_device)
        self.on_off_button.turnOff.connect(self.turn_off_device)
        
        self.main_window_layout.addWidget(self.on_off_button)
        

        widget = QWidget()
        
        widget.setLayout(self.main_window_layout)

        self.setCentralWidget(widget)
        self.resize(500,300)

    def updateSliderValues(self, red, green, blue):
        self.sliderValueChanged.emit(red, green, blue)
    
    def updateSliders(self, rgb: RGB):
        self.slider_container.updateSliders(rgb.red, rgb.green, rgb.blue)

    def sliderPressed(self, value):
        self.isSliderPressed = value
        
    def handleDropdownSelection(self, selected_option):
        self.selection.emit(selected_option)
        
    def getDropdownSelection(self):
        return self.dropdown.getSelectedOption()
    
    def turn_on_device(self):
        self.turnOnDevice.emit()
    
    def turn_off_device(self):
        self.turnOffDevice.emit()