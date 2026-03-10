# Customer Churn Prediction using K-Fold Cross Validation

from sklearn.model_selection import KFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

# Create synthetic dataset
X, y = make_classification(n_samples=500, n_features=5)

# Create Decision Tree model
model = DecisionTreeClassifier()

# K-Fold Cross Validation
kf = KFold(n_splits=5, shuffle=True)

# Evaluate model
scores = cross_val_score(model, X, y, cv=kf)

# Print results
print("Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())
