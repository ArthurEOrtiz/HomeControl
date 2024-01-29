import logging
from Config.logging_config import configure_logging
from Config.broker_config import BrokerConfig
from Config.device_config import DeviceConfig
from Models.device import Device
from Services.mqtt_client_handler import MqttClientHandler
from Services.mqtt_device_handler import MqttDeviceHandler

class Application:
  def __init__(self):
    self.mqtt_client_handler = MqttClientHandler()
    self.mqtt_device_handler = MqttDeviceHandler()
    self.broker_config = BrokerConfig()
    self.device_config = DeviceConfig() 
    
  def configure(self):
    configure_logging()
    logging.info("Logging initialized")
    
    self.mqtt_client_handler.configure_client()
    username, password, ip_address, port = self.broker_config.load_configuration()
    self.mqtt_client_handler.configure_broker(username, password, ip_address, port)
  
    config_values = self.device_config.load_configuration()
    if config_values:
      device_office_hostname, device_office_ip_address, device_kitchen_hostname, device_kitchen_ip_address = config_values
      self.mqtt_device_handler.configure_device_handler(
        [Device(device_office_hostname, device_office_ip_address, "officeLight"), 
         Device(device_kitchen_hostname, device_kitchen_ip_address, "kitchenLight")])
      
    # Now that the device handler has the devices. We can have the clien start subscribing to the devices
      
      
  def initialize(self):
    self.configure()
    self.mqtt_client_handler.connect()
    #subscribe to the list of devices
    #self.mqtt_client_handler.subscribe_to_devices()
    
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
    app.initialize()
    app.run_tasks()
  except Exception as e:
    logging.error(f"Error: {e}")
  except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
  finally:
    app.cleanup()
    app.stop()