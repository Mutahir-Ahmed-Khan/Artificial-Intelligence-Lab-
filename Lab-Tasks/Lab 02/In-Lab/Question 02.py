class uniStaff: 
  def __init__(self, name, staffID, department):
    self.name = name
    self.staffID = staffID
    self.department = department

  def displayInfo(self):
    print("Name: ", self.name, "\nStaff ID: ", self.staffID, "\nDepartment: ", self.department)
  
class Teachers(uniStaff): 
  def __init__ (self, name, staffID, department, courses, salary):
    super().__init__(name, staffID, department)
    self.courses = courses
    self.salary = salary

  def teachingCourses(self):
    print(self.name,"(", self.staffID, ") " , "is teaching", self.courses, "courses to ", self.department, "with Salary of ", self.salary )

  def displayInfo(self):
    print("Name: ", self.name, "\nStaff ID: ", self.staffID, "\nDepartment: ", self.department)

class AdminStaff(uniStaff): 
  def __init__ (self, name, staffID, department, role, workingHours):
    super().__init__(name, staffID, department)
    self.role = role
    self.workingHours = workingHours
  
  def performingTasks(self):
    print(self.name, "is performing tasks")

  def displayInfo(self):
    print("Name: ", self.name, "\nStaff ID: ", self.staffID)

class ResearchAssistants(uniStaff): 
  def __init__ (self, name, staffID, department, topic, stipend):
    super().__init__(name, staffID, department)
    self.topic = topic
    self.stipend = stipend

  def displayInfo(self):
    print("Name: ", self.name, "\nStaff ID: ", self.staffID, "\nDepartment: ", self.department)
  
  def workResearch(self):
    print(self.name, "is working on research")

mem1 = Teachers("Ammar", 1001, "EE", 6, 70000)
mem1.teachingCourses()
mem2 = AdminStaff("Mutahir", 2002, "CS", "Assistant Professor", 10)
mem2.performingTasks()
mem3 = ResearchAssistants("Jazzy", 3003, "CS", "Machine Learning", 10000)
mem3.workResearch()

print("\n")

mem1.displayInfo()
print("\n")
mem2.displayInfo()
print("\n")
mem3.displayInfo()
  
