# 🤖 Supervised Learning - Machine Learning

Welcome to the **Supervised Learning** section of my Machine Learning repository.
This folder contains implementations of popular **Supervised Machine Learning algorithms**, including explanations, code, and model evaluation.

Supervised learning is a type of machine learning where a model learns from **labeled training data** to make predictions on unseen data.

---

## 📌 What is Supervised Learning?

Supervised learning involves training a model using a dataset that contains **input features (X)** and **known output labels (Y)**.

The model learns the relationship between inputs and outputs and can later predict results for **new unseen data**.

### Example

| Features    | Label       |
| ----------- | ----------- |
| Age, Salary | Buy Product |
| Study Hours | Exam Score  |

---

## 🎯 Types of Supervised Learning

### 1️⃣ Classification

Used when the output variable is **categorical**.

Examples:

* Spam Detection
* Disease Prediction
* Fraud Detection

Algorithms used:

* Logistic Regression
* Decision Trees
* Random Forest
* Support Vector Machine
* K-Nearest Neighbors
* Naive Bayes

---

### 2️⃣ Regression

Used when the output variable is **continuous**.

Examples:

* House Price Prediction
* Sales Forecasting
* Temperature Prediction

Algorithms used:

* Linear Regression
* Polynomial Regression
* Ridge & Lasso Regression

---

## 📂 Project Structure

```
Supervised-Learning
│
├── datasets
│   └── sample_dataset.csv
│
├── notebooks
│   └── supervised_learning.ipynb
│
├── models
│   └── trained_model.pkl
│
├── src
│   ├── preprocessing.py
│   ├── train_model.py
│   └── evaluate_model.py
│
└── README.md
```

---

## ⚙️ Steps in the Project

### 1️⃣ Import Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

### 2️⃣ Load Dataset

```python
data = pd.read_csv("dataset.csv")
data.head()
```

---

### 3️⃣ Data Preprocessing

* Handle missing values
* Encode categorical variables
* Feature scaling
* Train-test split

```python
from sklearn.model_selection import train_test_split
```

---

### 4️⃣ Train Model

Example: Logistic Regression

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
```

---

### 5️⃣ Model Evaluation

```python
from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
```

---

## 📊 Evaluation Metrics

Some commonly used metrics:

| Metric    | Description                             |
| --------- | --------------------------------------- |
| Accuracy  | Correct predictions / total predictions |
| Precision | Correct positive predictions            |
| Recall    | Ability to find all positive samples    |
| F1 Score  | Balance between precision and recall    |

---

## 🧠 Algorithms Covered

✔ Linear Regression
✔ Logistic Regression
✔ Decision Tree
✔ Random Forest
✔ KNN
✔ Naive Bayes
✔ Support Vector Machine

---

## 📈 Tools & Libraries

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🚀 Applications of Supervised Learning

* Credit card fraud detection
* Medical diagnosis
* Email spam detection
* Customer churn prediction
* Stock price prediction

---

## 📌 Future Improvements

* Hyperparameter tuning
* Deep learning models
* Model deployment using Flask/Streamlit
* Real-time prediction system

---

