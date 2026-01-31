class Vehicle: 
  def __init__(self, vehicleID, brand, rentPerDay):
    self.vehicleID = vehicleID
    self.brand = brand
    self.rentPerDay = rentPerDay

  def displayDetails(self):
    print("Vehicle ID: ", self.vehicleID, "\nBrand: ", self.brand, "\nRent per day: ", self.rentPerDay)

  def calcRent(self, days):
    return self.rentPerDay * days

obj1 = Vehicle(1001, "Toyota", 18)
obj2 = Vehicle(2002, "Mercedes", 90)

obj1.displayDetails()
print("\n")
obj2.displayDetails()

print("\n")
dys = int(input("Enter the number of days: "))
print("Total Rent For ",dys ," :" ,obj1.calcRent(dys))
print("Total Rent For ",dys ," :", obj1.calcRent(dys))
