print("Firefighting Robot Simulation")
print()

roomStatus = {
    'a': 'safe', 'b': 'safe', 'c': 'fire',
    'd': 'safe', 'e': 'fire', 'f': 'safe',
    'g': 'safe', 'h': 'safe', 'j': 'fire'
}

roomPath = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

def showEnvironment():
    allRooms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
    for i in range(0, 9, 3):
        rowRooms = allRooms[i:i+3]
        for r in rowRooms:
            if roomStatus[r] == "fire":
                print("F", end=" ")
            else:
                print(".", end=" ")
        print()

print("Initial Environment State:")
showEnvironment()

for currentRoom in roomPath:
    print("Robot moved to room", currentRoom)

    if roomStatus[currentRoom] == "fire":
        print("Fire detected! Extinguishing fire...")
        roomStatus[currentRoom] = "safe"
    else:
        print("Room is already safe")

    showEnvironment()

print("Final Environment: All rooms are safe")
showEnvironment()
