
from Models import Topic

class Device:
  def __init__(self, id, ip_address, name):
    self.id = id # device id, what identitfeis the device to the topic
    self.ip_address = ip_address
    self.name = name # human readable name
    self.manufacturer = None
    self.topics = {} # a dictionary of topics that the device uses for communication
    self.payloads = {} # a dictionary of payloads that the device uses for communication
    
  def add_topic(self, topic_type, topic_string):
    if topic_type not in self.topics:
      self.topics[topic_type] = []
    self.topics[topic_type].append(Topic(topic_type, topic_string))   
    
  def remove_topic(self, topic_type, topic_string):
    if topic_type in self.topics:
      self.topics[topic_type] = [topic for topic in self.topics[topic_type] if topic.string != topic_string]
    


    