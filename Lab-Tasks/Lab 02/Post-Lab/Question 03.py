class Student:
  def __init__(self, attributeMarks):
    self.__attributeMarks = attributeMarks

  def getMarks(self):
    return self.__attributeMarks

  def setMarks(self, __attributeMarks):
    self.__attributeMarks = __attributeMarks

  def calcGrades(self):
    marks = self.getMarks()
    if marks >= 90:
      return "Grade " + 'A'
    elif marks >= 80:
      return "Grade " + 'B'
    elif marks >= 70:
      return "Grade " + 'C'

std1 = Student(79)
std2 = Student(95)

print(std1.calcGrades())
print(std2.calcGrades())
