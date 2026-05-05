import numpy as nm
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as mtp

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=42)

LR = LinearRegression()
ModelLR = LR.fit(x_train, y_train)

PredictionLR = ModelLR.predict(x_test)
print("Prediction: ", PredictionLR)

mse = mean_squared_error(y_test, PredictionLR)
print("\nMean Error: ", mse)

r2 = r2_score(y_test, PredictionLR)
print("\nR2 Score: ", r2)
