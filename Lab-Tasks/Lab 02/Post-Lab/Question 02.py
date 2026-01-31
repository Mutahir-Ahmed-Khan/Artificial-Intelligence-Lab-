class employee: 
  def __init__(self, name, empID):
    self.name = name
    self.empID = empID

    def calcSalary(self):
      pass

class FullTime(employee): 
  def __init__(self, name, empID, monthSalary):
    super().__init__(name, empID)
    self.monthSalary = monthSalary

  def calcSalary(self):
    return self.monthSalary / 12

class PartTime(employee):
  def __init__(self, name, empID, hoursWorked, hourlyRate):
    super().__init__(name, empID)
    self.hoursWorked = hoursWorked
    self.hourlyRate = hourlyRate

  def calcSalary(self):
    return self.hoursWorked * self.hourlyRate

obj1 = FullTime("Mutahir", 1030, 1000)
obj2 = PartTime("Mutahir", 1030, 40, 100)

print(obj1.calcSalary())
print(obj2.calcSalary())
