import json
from PyQt5.QtCore import QObject, pyqtSignal
from Models.rgb import RGB
from Services import MqttClientHandler, MqttDeviceHandler
from UI import MainWindow

class MainWindowController(QObject):
    onsliderValueChanged = pyqtSignal(RGB)
    
    def __init__(self, client_handler: MqttClientHandler, device_handler: MqttDeviceHandler):
        super().__init__()
        self.main_window = MainWindow()
        self.client_handler = client_handler
        self.client_handler.on_message = self.on_message
        self.device_handler = device_handler
        self.main_window.sliderValueChanged.connect(self.handleSliderValueChanged)

    def handleSliderValueChanged(self, red, green, blue):
        rgb_object = RGB(red, green, blue)  
        self.onsliderValueChanged.emit(rgb_object)

        
    def on_message(self, client, userdata, message):
        officeDevice = self.device_handler.get_device_by_id("shellyrgbw2-2C696B")
        message_topic = f"shellies/{officeDevice.id}/color/0/status"

        if message.topic == message_topic:
            payload = message.payload.decode('utf-8')
            data = json.loads(payload)
            rgb = RGB(data['red'], data['green'], data['blue'])

            if self.main_window.isSliderPressed == False:
                self.main_window.updateSliders(rgb)
