class lights:
  status = "ON"
  def __init__(self, name): 
    self.name = name

  def switchON(self):
    self.status = "ON"

  def switchOFF(self):
    self.status = "OFF"

  def disStatus(self):
    print(self.name, " lights turned ", self.status)

room1 = lights("Living Room")
room1.disStatus()
room2 = lights("Bedroom")
room2.switchOFF()
room2.disStatus()
room1.switchON()
room1.disStatus()
room2.switchOFF()
room2.disStatus()
