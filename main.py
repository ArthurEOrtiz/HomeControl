import logging
import sys
from config import ConfigurationManager
from PyQt5.QtWidgets import QApplication
from Services import MqttClientHandler, MqttDeviceHandler
from ui import MainWindow

class Application:
  def __init__(self):
    self.app = QApplication(sys.argv)
    self.configuration = ConfigurationManager()
    self.mqtt_client_handler = MqttClientHandler()
    self.mqtt_device_handler = MqttDeviceHandler()
    self.main_window = MainWindow()
    
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
    self.mqtt_device_handler.add_common_topic_to_all_device("subscribe_all", "#")
    topics = self.mqtt_device_handler.get_all_device_topics()
    self.mqtt_client_handler.subscribe_to_topics(topics)
    
    self.main_window.show()
    sys.exit(self.app.exec_())

  def run_tasks(self):
    while True:
      
      # Your Application tasks go here
      # Application tasks are run in a loop in the main thread
      # These tasks could include processing incoming messages, 
      # handling user input, performing background calculations, etc.
      # The loop will run until the application is stopped.
      pass
  
  def cleanup(self):
    logging.info("Cleaning up.")
    self.mqtt_client_handler.disconnect()
    
  def stop(self):
    logging.info("Stopping.")
    exit(0)
    
def main():
  app = Application()
  try:
    app.config()
    app.initialize()
    #app.main_window.show()
    # app.run_tasks()
    
  except Exception as e:
    logging.error(f"Error: {e}")
  except KeyboardInterrupt:
    logging.warning("Keyboard interrupt detected.")
  finally:
    app.cleanup()
    app.stop()
  
if __name__ == "__main__":
  main()