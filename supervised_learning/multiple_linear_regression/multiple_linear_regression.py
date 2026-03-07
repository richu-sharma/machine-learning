# Multiple Linear Regression Example

import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "Size_sqft": [1000, 1500, 2000, 2500, 3000],
    "Bedrooms": [2, 3, 3, 4, 4],
    "Age": [10, 8, 6, 4, 2],
    "Price": [200000, 300000, 400000, 500000, 600000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Size_sqft", "Bedrooms", "Age"]]
y = df["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction for a new house
prediction = model.predict([[2200, 3, 5]])

print("Predicted House Price:", prediction[0])
