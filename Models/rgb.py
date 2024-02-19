class RGB:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue

  def __str__(self):
    return f'"red":{self.red}, "green": {self.green}, "blue": {self.blue},'

  def __repr__(self):
    return f'RGB({self.red}, {self.green}, {self.blue})'

  def __eq__(self, other):
    if isinstance(other, RGB):
      return self.red == other.red and self.green == other.green and self.blue == other.blue
    return False

  def __add__(self, other):
    if isinstance(other, RGB):
      new_red = min(self.red + other.red, 255)
      new_green = min(self.green + other.green, 255)
      new_blue = min(self.blue + other.blue, 255)
      return RGB(new_red, new_green, new_blue)
    raise TypeError("Unsupported operand type for +: 'RGB' and '{}'".format(type(other).__name__))