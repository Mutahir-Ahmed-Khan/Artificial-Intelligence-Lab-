from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

DT = DecisionTreeClassifier()

DT.fit(x_train, y_train)

predictionDT = DT.predict(x_test)
print("Prediction:", predictionDT)

training_acc = DT.score(x_train, y_train) * 100
print("Training Accuracy:", training_acc)

testing_acc = accuracy_score(y_test, predictionDT) * 100
print("Testing Accuracy:", testing_acc)
