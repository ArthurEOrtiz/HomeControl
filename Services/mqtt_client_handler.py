import logging
import paho.mqtt.client as mqtt

class MqttClientHandler():
  def __init__(self):
    self.client_id = None
    self.clean_session = None
    self.user_data = None # client offers this, might use it later for callbacks.
    self.client = None
    
    self.broker_username = None
    self.broker_password = None
    self.broker_ip_address = None
    self.broker_port_number = None
    self.keep_alive = None
    
  def initialize_client(self):
    self.client = mqtt.Client(self.client_id, self.clean_session, self.user_data)
    self.client.on_connect = self.on_connect
    self.client.on_message = self.on_message
    self.client.on_disconnect = self.on_disconnect
    
  def connect(self):
    """
      I dont want to just recreate the connect method. I need it to do something specific 
      for my application. If this "handles" connection, then on connect, it should set the username
      and password, 
    """
    self.client.username_pw_set(self.broker_username, self.broker_password)
    self.client.user_data_set(self.user_data)
    logging.info("Connecting to broker.")
    logging.info(f"Broker IP: {self.broker_ip_address}")
    logging.info(f"Broker Port: {self.broker_port_number}")
    logging.info(f"Keep Alive: {self.keep_alive}")
    self.client.connect(self.broker_ip_address, port=self.broker_port_number, keepalive=self.keep_alive)
    self.client.loop_start()
    """
      "
        loop_start()
        loop_stop(force=False)
        
        These functions implement a threaded interface to the network loop. Calling loop_start() once, 
        before or after connect*(), runs a thread in the background to call loop() automatically. 
        This frees up the main thread for other work that may be blocking. This call also handles 
        reconnecting to the broker. Call loop_stop() to stop the background thread. The force argument is currently ignored.
      "
      
      Thay being said then, I need a way to stop the loops after so many failed attempts at connecting or reconnecting. 

    """
    
  def on_connect(self, client, userdata, flags, rc):
    """
      This is the callback for when the client receives a CONNACK response from the server.
      
      0: Connection successful
      1: Connection refused - incorrect protocol version
        The Server does not suport the level of MQTT protocol requested by the Client.
      2: Connection refused - invalid client identifier
        The Client identifier is correct UTF-8 but not allowed by the Server
      3: Connection refused - server unavailable
        The Network Connection has been made but the MQTT service is unavailable
      4: Connection refused - bad username or password
        The data in the user name or password is malformed
      5: Connection refused - not authorised
        The Client is not authorized to connect
      6-255: Currently unused.
      
      Subscribing in on_connect() means that if we lose the connection and
      reconnect then subscriptions will be renewed.
    """
    if rc != 0:
      raise Exception(f"Connection failed with result code {rc}")
    else:
      """
        At this point the clientId is an empty string which means
        
        "A Server MAY allow a Client to supply a ClientId that 
        has a length of zero bytes, however if it does so the 
        Server MUST treat this as a special case and assign a 
        unique ClientId to that Client. It MUST then process 
        the CONNECT packet as if the Client had provided that 
        unique ClientId [MQTT-3.1.3-6].

        If the Client supplies a zero-byte ClientId, the Client 
        MUST also set CleanSession to 1" [MQTT-3.1.3-7].
      """
      logging.info("Connected to broker.")
      logging.info(f"Paho Client:\n {client.__dict__}")
      logging.info(f"Userdata: {userdata}")
      logging.info(f"Flags: {flags}")
      logging.info(f"Reason Code: {rc}")
      
  def on_message(self, client, userdata, message):
    """
      The callback for when a PUBLISH message is received from the server.
    """
    logging.info("****Message received.****")
    logging.info(f"\tTopic: {message.topic}")
    logging.info(f"\tPayload:{message.payload.decode()}")
      
  def subscribe(self, topic="#", qos=0, options=None):
    # options is for MQTTv5, so like dont mess with it. 
    logging.info(f"Subscribing to {topic}, qos={qos}") 
    self.client.subscribe(topic, qos, options)
  
  def subscribe_to_topics(self, topics):
    for topic in topics:
      logging.info(f"Subscribing to {topic}")
      self.client.subscribe(topic)

  def disconnect(self): 
    logging.info("Disconnecting from broker.")
    self.client.loop_stop()
    self.client.disconnect()
  
  def on_disconnect(self, client, userdata, rc):
    """ 
      This might not be too important right now since i'm using
      qos 0 and clean_session=True. but if that ever changes this
      will be important.
    """
    logging.info("Disconnected from broker.")
    logging.info(f"Paho Client:\n{client.__dict__}")
    logging.info(f"Userdata: {userdata}")
    logging.info(f"Reason code: {rc}")
  
  def configure_client(self, id='', userdata = None, keep_alive = 60, clean_session=True):
    self.client_id = id
    self.user_data = userdata
    self.keep_alive = keep_alive
    self.clean_session = clean_session
    
  def configure_broker(self, username, password, ip_address, broker_port):
    self.broker_username = username
    self.broker_password = password
    self.broker_ip_address = ip_address
    self.broker_port_number = broker_port
