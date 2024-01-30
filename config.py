import logging
from Config.logging_config import configure_logging
from Config.broker_config import BrokerConfig
from Config.device_config import DeviceConfig
from Models.device import Device

class ConfigurationManager:
  def __init__(self):
    self.mqtt_client_handler = None
    self.mqtt_device_handler = None
    self.broker_config = BrokerConfig()
    self.device_config = DeviceConfig()

  def configure_logging(self):
    configure_logging()
    logging.info("Logging initialized")
      
  def configure_mqtt_client(self):
    self.mqtt_client_handler.configure_client()
    config_values = self.broker_config.load_configuration()
    if config_values:
      username, password, ip_address, port = config_values
      self.mqtt_client_handler.configure_broker(username, password, ip_address, port)
    else:
      # throw and error, dont break everything, just stop the program or something.
      logging.error("No broker configuration found.")
      Exception("No broker configuration found.")
      
  def configure_devices(self):
    config_values = self.device_config.load_configuration()
    if config_values:
        device_office_hostname, device_office_ip_address, device_kitchen_hostname, device_kitchen_ip_address = config_values
        self.mqtt_device_handler.add_devices([
            Device(device_office_hostname, device_office_ip_address, "Office Light"),
            Device(device_kitchen_hostname, device_kitchen_ip_address, "Kitchen Light")
        ])
    else:
        # throw and error, dont break everything, just stop the program or something.
        logging.error("No device configuration found.")
        Exception("No device configuration found.")
          
  def configure(self, ClientHandler, DeviceHandler):
    self.mqtt_client_handler = ClientHandler
    self.mqtt_device_handler = DeviceHandler
    self.configure_logging()
    self.configure_mqtt_client()
    self.configure_devices()