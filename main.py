import logging
from Config.logging_config import configure_logging
from Config.broker_config import BrokerConfig
from Services.mqtt_client_handler import MqttClientHandler

class Application:
  def __init__(self):
    self.mqtt_client_handler = MqttClientHandler()
    self.broker_config = BrokerConfig()
    
  def configure(self):
    configure_logging()
    logging.info("Logging initialized")
    self.mqtt_client_handler.configure_client()
    username, password, ip_address, port = self.broker_config.load_configuration()
    self.mqtt_client_handler.configure_broker(username, password, ip_address, port)
  
  def initialize(self):
    self.configure()
    self.mqtt_client_handler.connect()
    
  def run_tasks(self):
    while True:
      # Your Application tasks go here
      # Application tasks are run in a loop in the main thread
      # These tasks could include processing incoming messages, 
      # handling user input, performing background calculations, etc.
      pass
  
  def cleanup(self):
    print("Cleaning up.")
    self.mqtt_client_handler.disconnect()
    
  def stop(self):
    print("Application Exiting.")
    exit(0)
    
if __name__ == "__main__":
  
  app = Application()
  try:
    app.initialize()
    app.run_tasks()
  except Exception as e:
    print(f"Error: {e}")
  except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
  finally:
    app.cleanup()
    app.stop()