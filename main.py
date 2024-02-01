import asyncio
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
    self.mqtt_device_handler.add_common_topic_to_all_device("subscribe_all", "#")
    topics = self.mqtt_device_handler.get_all_device_topics()
    #self.mqtt_client_handler.subscribe_to_topics(topics)
    self.mqtt_client_handler.subscribe()

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
    
    
async def main():
  app = Application()
  try:
    app.config()
    
    #Create an event loop 
    loop = asyncio.get_event_loop()
    
    # Schedule the initialize methos as a coroutine in the event loop 
    await loop.run_in_executor(None, app.initialize)
    
    #Run the event loop for the run_tasks method
    await loop.run_in_executor(None, app.run_tasks)
    
  except Exception as e:
    logging.error(f"Error: {e}")
  except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
  finally:
    await loop.run_in_executor(None, app.cleanup)
    await loop.run_in_executor(None, app.stop)
  
if __name__ == "__main__":
  asyncio.run(main())