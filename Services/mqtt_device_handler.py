class MqttDeviceHandler:
  def __init__(self):
    self.devices = set()
    
  def add_device(self, device):
    self.devices[device.id] = device
    
  def add_devices(self, devices):
    for device in devices:
      self.add_device(device)
    
  def count_devices(self):
    return len(self.devices)
    
  def remove_device(self, device):
    del self.devices[device.id]
    
  def set_device_topic(self, device_id, topic):
    device = self.devices.get(device_id)
    if device:
      device.add_topic(topic)
    else:
      raise Exception(f"Device with id {device_id} not found.")
  
   
  
  
  
  
  
  
    

    

