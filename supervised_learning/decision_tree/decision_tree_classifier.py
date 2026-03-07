# Decision Tree Classification Example

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    "Age": [22,25,47,52,46,56,55,60,62,61],
    "Salary": [20000,25000,50000,60000,52000,80000,75000,90000,95000,100000],
    "Purchased": [0,0,1,1,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Age", "Salary"]]
y = df["Purchased"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, pred))
