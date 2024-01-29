class MqttDeviceHandler:
  def __init__(self):
    self.devices = []

  def add_device(self, device):
    self.devices.append(device)
    
  def remove_device(self, device):
    self.devices.remove(device)

  def get_device_count(self):
    return len(self.devices)

  def get_all_devices(self):
    return self.devices
    

