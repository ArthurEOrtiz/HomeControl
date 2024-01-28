import paho.mqtt.client as mqtt


class MqttClientHandler():
  def __init__(self):
    self.client = mqtt.Client()
    self.client_id = "home_control"
    self.clean_session = None # This is contingent on qos being 0
    self.user_data = None # I could probably use this to store stuff for calll backs, maybe the last updated status of each device?
    self.broker_username = None
    self.broker_password = None
    self.broker_ip_address = None
    self.broker_port_number = None
    self.broker_keep_alive = None
    
  def connect(self):
    
    """
      I dont want to just recreate the connect method. I need it to do something specific 
      for my application. If this "handles" connection, then on connect, it should be given
      what it needs to configure the client, then start up the client, and then inform the parent
      class that it has successfully connected and running. 
      
      So far when this class is initiated the client, client_id, clean_session, and user_data
      are set to there initial values. We also need username and password, the IP address,
      and the port number. How would i pass username and password into this?
      
      I think configure_client should have a way to changee client_id,
      clean_session, and change user_data. 
    """
    
    self.client.username_pw_set(self.user_name, self.user_password)
    self.client.user_data_set(self.user_data)
    self.client.connect_async(self.broker_ip_address, port=self.broker_port_number, keepalive=self.broker_keep_alive)
    self.client.loop_start() # on_connect() will be called once this is successful here. 
    self.client.on_connect = self.on_connect
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
      Subscribing in on_connect() means that if we lose the connection and
      reconnect then subscriptions will be renewed.
    """
    if rc != 0:
      """
        Return and error but dont break everything. 
        
        0: Connection successful
            1: Connection refused - incorrect protocol version
            2: Connection refused - invalid client identifier
            3: Connection refused - server unavailable
            4: Connection refused - bad username or password
            5: Connection refused - not authorised
            6-255: Currently unused.
      """
  
  def configure_client(self, id, ip_address, broker_port, keep_alive = 60, clean_session=True):
    self.client_id = id
    self.clean_session = clean_session
    self.broker_ip_address = ip_address
    self.broker_port_number = broker_port
    self.broker_keep_alive = keep_alive
  
  def configure_user(self, username, password):
    self.broker_username = username
    self.broker_password = password

  
  
  

  
  """
    Do I really need to have an configure_device method?? Should that be handled by the device class?
    I think it should be handled by the device class. I think I should just have a configure_client method
  """
    
      
    
    
    
    
    
    
    