class MqttDeviceHandler:
  def __init__(self):
    self.devices = {}
    
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
    
  def get_all_device_topics(self):
    topics = []
    for device_id, device in self.devices.items():
        for topic_type, topic_list in device.topics.items():
            for topic in topic_list:
                topics.append(topic.string)
    return topics
    
  def add_common_topic_to_all_device(self, topic_type, topic_string):
    for device_id, device in self.devices.items():
      full_topic_string = f"shellies/{device_id}/{topic_string}"
      device.add_topic(topic_type, full_topic_string)
      

  
  
  
    

    

