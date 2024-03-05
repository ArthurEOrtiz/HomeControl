import json
from PyQt5.QtCore import QObject
from Models import RGB, Device
from Services import MqttClientHandler, MqttDeviceHandler
from UI import MainWindow

class MainWindowController(QObject):
    
    def __init__(self, client_handler: MqttClientHandler, device_handler: MqttDeviceHandler):
        super().__init__()
        self.main_window = MainWindow()
        self.client_handler = client_handler
        self.client_handler.on_message = self.on_message
        self.device_handler = device_handler
        self.main_window.sliderValueChanged.connect(self.handleSliderValueChanged)
        self.device_handler.topic_message.connect(self.client_handler.publish)
        self.main_window.selection.connect(self.handleDropdownSelection)
        self.main_window.turnOnDevice.connect(self.turn_on_device)
        self.main_window.turnOffDevice.connect(self.turn_off_device)
        self.selected_device : Device = None
        self.isDeviceUpdated = False
        
    
    def initialize(self):
        self.selected_device = self.device_handler.get_device_by_name("Office Light")
        if self.client_handler.client is not None:
            self.client_handler.subscribe(f"shellies/{self.selected_device.id}/#")
        
    def handleDropdownSelection(self, selected_option):
        self.client_handler.unsubscribe(f"shellies/{self.selected_device.id}/#")
        if selected_option == "Office Light":
            self.isDeviceUpdated = False
            self.selected_device = self.device_handler.get_device_by_name("Office Light")
        elif selected_option == "Kitchen Light":
            self.isDeviceUpdated = False
            self.selected_device = self.device_handler.get_device_by_name("Kitchen Light")
        self.client_handler.subscribe(f"shellies/{self.selected_device.id}/#")

    def handleSliderValueChanged(self, red, green, blue):
        if self.selected_device is None:
            print("No device selected.")
            return

        rgb_object = RGB(red, green, blue) 
        device_hostname = self.selected_device.id   
        self.device_handler.handle_slider_update(device_hostname, rgb_object)
        
    def on_message(self, client, userdata, message):
        device = self.selected_device

        print("           Topic: ", message.topic)
        print("Received message: ", message.payload.decode('utf-8'))
        
        if message.topic == f"shellies/{device.id}/info":
            payload = message.payload.decode('utf-8')
            data = json.loads(payload)
            light = data['lights'][0]
            rgb = RGB(light['red'], light['green'], light['blue'])

            if self.main_window.isSliderPressed == False:
                self.main_window.updateSliders(rgb)
                
        if message.topic == f"shellies/{device.id}/color/0/status" and self.isDeviceUpdated == False:
            payload = message.payload.decode('utf-8')
            data = json.loads(payload)
            rgb = RGB(data['red'], data['green'], data['blue'])
            if self.main_window.isSliderPressed == False:
                self.main_window.updateSliders(rgb)
                self.isDeviceUpdated = True
    
    def turn_on_device(self):
        self.client_handler.publish(f"shellies/{self.selected_device.id}/color/0/set", '{"turn": "on" }')
    
    def turn_off_device(self):
        self.client_handler.publish(f"shellies/{self.selected_device.id}/color/0/set", '{"turn": "off" }')

