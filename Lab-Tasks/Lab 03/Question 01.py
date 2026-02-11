class environment:
  def __init__ (self, heatLevel = 'High'):
    self.heatLevel = heatLevel

  def getPercept(self):
    if(self.heatLevel == 'High'):
      return 'Hot'
    else:
      return 'Cold'
    
class simpleReflex:
  def __init__(self):
    pass

  def act(self, percept):
    if(percept == 'Hot'):
      return 'Pull Away the Hand'
    else:
      return 'Dont Pull Away'

def runAgent(env, agent):
  percept = env.getPercept()
  action = agent.act(percept)
  print(f"Percept: {percept}, Agent: {action}")

#Main
e1 = environment('High')
ag = simpleReflex()

runAgent(e1, ag)
