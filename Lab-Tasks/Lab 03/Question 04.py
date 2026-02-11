print("Restaurant Selector")
print()

restaurantData = {
    "A": {"distance": 3, "rating": 7},
    "B": {"distance": 5, "rating": 9}
}

restaurantScores = {}

for rest in restaurantData:
    score = restaurantData[rest]["rating"] - restaurantData[rest]["distance"]
    restaurantScores[rest] = score
    print("Restaurant", rest, "Utility =", score)

topChoice = max(restaurantScores, key=restaurantScores.get)
print()
print("Selected Restaurant:", topChoice)
