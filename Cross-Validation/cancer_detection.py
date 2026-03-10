# Cancer Detection System using Stratified K-Fold Cross Validation

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Create model
model = RandomForestClassifier()

# Stratified K-Fold Cross Validation
skf = StratifiedKFold(n_splits=5)

# Evaluate model
scores = cross_val_score(model, X, y, cv=skf)

# Print results
print("Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())
