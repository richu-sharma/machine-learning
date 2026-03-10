# Image Classification using Repeated K-Fold Cross Validation

from sklearn.model_selection import RepeatedKFold, cross_val_score
from sklearn.svm import SVC
from sklearn.datasets import load_digits

# Load digits dataset
digits = load_digits()
X = digits.data
y = digits.target

# Create SVM model
model = SVC()

# Repeated K-Fold Cross Validation
rkf = RepeatedKFold(n_splits=5, n_repeats=3)

# Evaluate model
scores = cross_val_score(model, X, y, cv=rkf)

# Print results
print("Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())
