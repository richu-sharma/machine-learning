# PCA Dimensionality Reduction Example

import pandas as pd
from sklearn.decomposition import PCA

# Sample dataset
data = {
    "Age":[22,25,47,52,46,56,55,60,62,61],
    "Income":[20000,25000,50000,60000,52000,80000,75000,90000,95000,100000],
    "SpendingScore":[30,40,60,70,65,80,75,90,95,85]
}

df = pd.DataFrame(data)

# Apply PCA
pca = PCA(n_components=2)

reduced_data = pca.fit_transform(df)

print("Reduced Data:")
print(reduced_data)
