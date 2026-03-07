# 🤝 K-Nearest Neighbors (KNN)

## Overview

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for **classification and regression**.

It works by finding the **K closest data points** to a new input and predicting the label based on majority voting.

---

## Dataset

In this example, we predict whether a customer will **purchase a product** based on:

* Age
* Salary

| Age | Salary | Purchased |
| --- | ------ | --------- |
| 22  | 20000  | 0         |
| 25  | 25000  | 0         |
| 47  | 50000  | 1         |
| 52  | 60000  | 1         |

Where:

* **0 → Not Purchased**
* **1 → Purchased**

---

## Libraries Used

* pandas
* scikit-learn

---

## How to Run

Install libraries:

```
pip install pandas scikit-learn
```

Run the program:

```
python knn_classifier.py
```

---

## Learning Outcomes

✔ Understanding distance-based algorithms
✔ Implementing KNN for classification
✔ Training and evaluating ML models
