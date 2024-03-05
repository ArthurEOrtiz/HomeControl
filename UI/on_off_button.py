from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal

class OnOffButton(QWidget):
    turnOn = pyqtSignal()
    turnOff = pyqtSignal()
    
    def __init__(self):
      super().__init__()

      layout = QHBoxLayout()

      self.on_button = QPushButton("ON")
      self.off_button = QPushButton("OFF")
      
      self.on_button.clicked.connect(self.turn_on)
      self.off_button.clicked.connect(self.turn_off)
      
      layout.addWidget(self.off_button)
      layout.addWidget(self.on_button)
      
      self.setLayout(layout)
    
    def turn_on(self):
      self.turnOn.emit()
    
    def turn_off(self):
      self.turnOff.emit()        


        
