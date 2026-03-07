import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Size_sqft": [500, 800, 1000, 1200, 1500],
    "Price": [1000000, 1500000, 1800000, 2200000, 2700000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Size_sqft"]]
y = df["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction
predicted_price = model.predict([[1600]])

print("Predicted Price:", predicted_price[0])
