import os
from dotenv import load_dotenv

class DeviceConfig:
    @staticmethod
    def load_configuration():
        try:
            load_dotenv()
            device_office_hostname = os.getenv("MQTT_DEVICE_OFFICE_HOSTNAME")
            device_office_ip_address = os.getenv("MQTT_DEVICE_OFFICE_IP_ADDRESS")
            device_kitchen_hostname = os.getenv("MQTT_DEVICE_KITCHEN_HOSTNAME")
            device_kitchen_ip_address = os.getenv("MQTT_DEVICE_KITCHEN_IP_ADDRESS") 
            return device_office_hostname, device_office_ip_address, device_kitchen_hostname, device_kitchen_ip_address  
        except Exception as e:
            print(f"Error loading configuration: {e}")