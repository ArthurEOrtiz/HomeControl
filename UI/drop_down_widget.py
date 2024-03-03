from PyQt5.QtWidgets import QComboBox, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal

class DropdownWidget(QWidget):
    selectionChanged = pyqtSignal(str)

    def __init__(self, options):
      super().__init__()

      layout = QVBoxLayout()

      self.comboBox = QComboBox()
      self.comboBox.addItems(options)
      self.comboBox.currentIndexChanged.connect(self.emitSelectionChanged)
      layout.addWidget(self.comboBox)

      self.setLayout(layout)

    def emitSelectionChanged(self, index):
        selected_option = self.comboBox.currentText()
        self.selectionChanged.emit(selected_option)
