
class Device:
  def __init__(self, id, name, ip_address):
    self.name = name # human readable name
    self.id = id # device id, what identitfeis the device to the topic
    self.ip_address = ip_address
    self.topics = []# a list of topics that the device uses for communication
    self.payloads = [] # a list of payloads that the device uses for communication
    
  def add_topic(self, topic):
    self.topics.append(topic)
    
  def remove_topic(self, topic):
    self.topics.remove(topic)
    
    

    