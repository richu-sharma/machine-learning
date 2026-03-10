# Stock Price Prediction using Time Series Cross Validation

from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np

# Example time-series dataset
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([2,4,6,8,10,12,14,16])

# Create Linear Regression model
model = LinearRegression()

# Time Series Cross Validation
tscv = TimeSeriesSplit(n_splits=4)

# Evaluate model
scores = cross_val_score(model, X, y, cv=tscv)

# Print results
print("Cross Validation Scores:", scores)
print("Average Score:", scores.mean())
