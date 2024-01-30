import logging
from config import ConfigurationManager
from Services.mqtt_client_handler import MqttClientHandler
from Services.mqtt_device_handler import MqttDeviceHandler

class Application:
  def __init__(self):
    self.configuration = ConfigurationManager()
    self.mqtt_client_handler = MqttClientHandler()
    self.mqtt_device_handler = MqttDeviceHandler()
    
  def config(self):
    self.configuration.configure(
      self.mqtt_client_handler, 
      self.mqtt_device_handler)  
      
  def initialize(self):
    self.mqtt_client_handler.initialize_client()  
    self.mqtt_client_handler.connect()
    
    '''
      At this point, the application is connected to the broker,
      and we have 2 devices loaded into the device handler. 
      So now I either have to load those devices with some topics 
      programmatically, or hardcode that in for now. 
    '''
    
  def run_tasks(self):
    while True:
      # Your Application tasks go here
      # Application tasks are run in a loop in the main thread
      # These tasks could include processing incoming messages, 
      # handling user input, performing background calculations, etc.
      pass
  
  def cleanup(self):
    logging.info("Cleaning up.")
    self.mqtt_client_handler.disconnect()
    
  def stop(self):
    logging.info("Stopping.")
    exit(0)
    
if __name__ == "__main__":
  
  app = Application()
  try:
    app.config()
    app.initialize()
    app.run_tasks()
  except Exception as e:
    logging.error(f"Error: {e}")
  except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
  finally:
    app.cleanup()
    app.stop()