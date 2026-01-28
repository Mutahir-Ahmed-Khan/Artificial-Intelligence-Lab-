n = int(input("Enter the N Value: "))
counter = 0

for i in range(2,n + 1,2):
  print(i)
  counter += 1

print("Total Even Number: ",counter)
