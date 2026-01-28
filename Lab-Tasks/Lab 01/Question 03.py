dict = {}

for i in range(3):
  name = input("Enter the name: ")
  marks = int(input("Enter the marks: "))
  dict[name] = marks

print("Student Records: ")
for name in dict:
  print(name, " : ", dict[name])
