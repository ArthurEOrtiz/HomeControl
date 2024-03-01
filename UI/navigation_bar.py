from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import pyqtSignal

class NavigationBar(QWidget):
    officeLightSelected = pyqtSignal()
    kitchenLightSelected = pyqtSignal()
    

    def __init__(self):
        super().__init__()

        self.navbarLayout = QHBoxLayout()
        self.navLabel = QLabel("Navigation")
        self.devicesComboBox = QComboBox()
        self.devicesComboBox.addItem("Office Light")
        self.devicesComboBox.addItem("Kitchen Light")
        self.devicesComboBox.currentIndexChanged.connect(self.handleComboBoxSelection)
        self.currentIndex = self.devicesComboBox.currentIndex()
        self.navbarLayout.addWidget(self.navLabel)
        self.navbarLayout.addWidget(self.devicesComboBox)
        self.setLayout(self.navbarLayout)

    def handleComboBoxSelection(self, index):
        if index == 0:
            self.officeLightSelected.emit()
        elif index == 1:
            self.kitchenLightSelected.emit()
