# Lasso Regression Example

import pandas as pd
from sklearn.linear_model import Lasso

# Sample dataset
data = {
    "Size_sqft": [1000,1500,2000,2500,3000],
    "Bedrooms": [2,3,3,4,4],
    "Age": [10,8,6,4,2],
    "Price": [200000,300000,400000,500000,600000]
}

df = pd.DataFrame(data)

X = df[["Size_sqft","Bedrooms","Age"]]
y = df["Price"]

# Train model
model = Lasso(alpha=0.1)
model.fit(X, y)

prediction = model.predict([[2200,3,5]])

print("Predicted Price:", prediction[0])
