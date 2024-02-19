from PyQt5.QtCore import QObject, pyqtSignal
from Models.rgb import RGB
from ui import MainWindow

class MainWindowController(QObject):
    onsliderValueChanged = pyqtSignal(RGB)
    
    def __init__(self):
        super().__init__()
        self.main_window = MainWindow()
        self.main_window.sliderValueChanged.connect(self.handleSliderValueChanged)

    def handleSliderValueChanged(self, red, green, blue):
        rgb_object = RGB(red, green, blue)  
        self.onsliderValueChanged.emit(rgb_object)

        
        