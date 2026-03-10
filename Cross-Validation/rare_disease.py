# Rare Disease Research using Leave-One-Out Cross Validation

from sklearn.model_selection import LeaveOneOut, cross_val_score
from sklearn.svm import SVC
import numpy as np

# Small dataset (example)
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([0,0,1,1,1])

# Create SVM model
model = SVC()

# Leave-One-Out Cross Validation
loo = LeaveOneOut()

# Evaluate model
scores = cross_val_score(model, X, y, cv=loo)

# Print results
print("Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())
