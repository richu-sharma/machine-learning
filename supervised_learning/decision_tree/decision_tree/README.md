# 🌳 Decision Tree Classification

## Overview

Decision Tree is a supervised machine learning algorithm used for **classification and regression tasks**.

It works by splitting the dataset into branches based on feature values, forming a tree-like structure.

In this example, the model predicts whether a customer will **purchase a product** based on:

* Age
* Salary

---

## Sample Dataset

| Age | Salary | Purchased |
| --- | ------ | --------- |
| 22  | 20000  | 0         |
| 25  | 25000  | 0         |
| 47  | 50000  | 1         |
| 52  | 60000  | 1         |
| 46  | 52000  | 1         |

Where:

* **0 → Not Purchased**
* **1 → Purchased**

---

## Libraries Used

* pandas
* scikit-learn

---

## How to Run

Install dependencies:

```
pip install pandas scikit-learn
```

Run the program:

```
python decision_tree_classifier.py
```

---

## Learning Outcomes

✔ Understanding decision tree structure
✔ Training classification models
✔ Making predictions using machine learning
