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
        self.main_window.sliderValueChanged.connect(self.handleSliderValueChanged)
        self.client_handler = client_handler
        self.client_handler.on_message = self.on_message
        self.device_handler = device_handler
        

    def handleSliderValueChanged(self, red, green, blue):
        rgb_object = RGB(red, green, blue)  
        self.onsliderValueChanged.emit(rgb_object)

        
    def on_message(self, client, userdata, message):
        
        message_topic = self.message_cypher()
        
        # print(f"message_topic selected: {message_topic}")
        # print(f"message topic:          {message.topic}")
        
        if message.topic == message_topic:
            payload = message.payload.decode('utf-8')
            data = json.loads(payload)
            rgb = RGB(data['red'], data['green'], data['blue'])
            print(f"payload: {payload}")    
            if self.main_window.isSliderPressed == False:
                self.main_window.updateSliders(rgb)
    
    def message_cypher(self):
        officeDevice = self.device_handler.get_device_by_id("shellyrgbw2-2C696B")
        kitchenDevice = self.device_handler.get_device_by_id("shellyrgbw2-2CC350")
        if self.main_window.isOfficeLightSelected == True:
            return f"shellies/{officeDevice.id}/color/0/status"
        elif self.main_window.isKitchenLightSelected == True:
            return f"shellies/{kitchenDevice.id}/color/0/status"
        