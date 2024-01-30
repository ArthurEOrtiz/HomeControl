from Models.device import Device
from Config.device_config import DeviceConfig

class MqttDeviceHandler:
  def __init__(self):
    self.devices = []
    
  def add_device(self, device):
    self.devices.append(device)
    
  def add_devices(self, devices):
    for device in devices:
      self.add_device(device)
    
  def count_devices(self):
    return len(self.devices)
    
  def remove_device(self, device):
    self.devices.remove(device)
    
  def return_device_topics(self, device_id):
    for device in self.devices:
      if device.id == device_id:
        return device.topics
    return None
  
  
  
    

    

