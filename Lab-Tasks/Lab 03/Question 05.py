print("Learning Agent Game")
print()

actionValues = {"Play": 0, "Rest": 0}

for turn in range(1, 11):
    if actionValues["Play"] <= actionValues["Rest"]:
        chosenAction = "Play"
        receivedReward = 5
    else:
        chosenAction = "Rest"
        receivedReward = 1

    actionValues[chosenAction] += receivedReward

    print(f"Step {turn}: Action chosen → {chosenAction}, Reward received → {receivedReward}")

print()
print("Q-table Updated")
print(actionValues)
