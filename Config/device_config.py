import os
from dotenv import load_dotenv

class DeviceConfig:
    @staticmethod
    def load_configuration():
        try:
            load_dotenv()
            device_office_hostname = os.getenv("MQTT_DEVICE_OFFICE_HOSTNAME")
            device_kitchen_hostname = os.getenv("MQTT_DEVICE_KITCHEN_HOSTNAME")
            return device_office_hostname, device_kitchen_hostname  
        except Exception as e:
            print(f"Error loading configuration: {e}")