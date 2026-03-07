# Polynomial Regression Example

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Sample dataset
data = {
    "Level": [1,2,3,4,5,6,7,8,9,10],
    "Salary": [45000,50000,60000,80000,110000,150000,200000,300000,500000,1000000]
}

df = pd.DataFrame(data)

X = df[["Level"]]
y = df["Salary"]

# Convert to polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, y)

# Prediction
level = 6.5
prediction = model.predict(poly.transform([[level]]))

print("Predicted Salary:", prediction[0])
