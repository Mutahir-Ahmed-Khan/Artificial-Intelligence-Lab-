print("Smart Classroom Light Controller\n")

presenceList = ["No", "Yes", "Yes", "No", "No", "Yes", "Yes", "No"]

lastStudents = "No"
lastLight = "OFF"
lightState = "OFF"

for step in range(8):
    currentStudents = presenceList[step]

    if currentStudents == "Yes" and lightState == "OFF":
        decision = "Turning lights ON"
        lightState = "ON"
    elif currentStudents == "No" and lightState == "ON":
        decision = "Turning lights OFF"
        lightState = "OFF"
    else:
        decision = "No action needed"

    print(f"Step {step + 1}")
    print(f"Students Present: {currentStudents}")
    print(f"Action Taken: {decision}")
    print(f"Agent Memory → Previous Students: {lastStudents}, Previous Light: {lastLight}")
    print("-" * 45)

    lastStudents = currentStudents
    lastLight = lightState
