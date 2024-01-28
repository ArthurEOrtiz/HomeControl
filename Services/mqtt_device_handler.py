class MQTTDeviceManager:
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
    
  class Device:
    def __init__(self, name, id, status):
      self.name = name
      self.id = id
      self.status = status
    def get_name(self):
      return self.name
    def get_id(self):
      return self.id
    def get_status(self):
      return self.status
    def set_name(self, name):
      self.name = name
    def set_id(self, id):
      self.id = id
    def set_status(self, status):
      self.status = status
