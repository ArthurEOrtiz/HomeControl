import os
from dotenv import load_dotenv

class BrokerConfig:
    @staticmethod
    def load_configuration():
        try:
            load_dotenv()
            username = os.getenv("MQTT_BROKER_USERNAME")
            password = os.getenv("MQTT_BROKER_PASSWORD")
            ip_address = os.getenv("MQTT_BROKER_ADDRESS")
            port = int(os.getenv("MQTT_BROKER_PORT"))
        
            return username, password, ip_address, port
        except Exception as e:
            print(f"Error loading configuration: {e}")
            