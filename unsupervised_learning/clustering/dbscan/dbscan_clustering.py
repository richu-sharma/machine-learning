# DBSCAN Clustering Example

import pandas as pd
from sklearn.cluster import DBSCAN

# Sample dataset
data = {
    "Age":[22,25,47,52,46,56,55,60,62,61],
    "Income":[20000,25000,50000,60000,52000,80000,75000,90000,95000,100000]
}

df = pd.DataFrame(data)

X = df[["Age","Income"]]

# Train model
model = DBSCAN(eps=10, min_samples=2)

df["Cluster"] = model.fit_predict(X)

print(df)
