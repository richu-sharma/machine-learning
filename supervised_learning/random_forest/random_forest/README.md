# 🌲 Random Forest Classification

## Overview

Random Forest is a supervised machine learning algorithm used for **classification and regression tasks**.

It works by combining multiple **decision trees** and taking the majority vote for classification or average for regression.

This makes the model more **accurate and less prone to overfitting**.

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

Install dependencies:


pip install pandas scikit-learn


Run the program:

python random_forest_classifier.py

## Learning Outcomes

✔ Understanding ensemble learning
✔ Training Random Forest models
✔ Improving prediction accuracy using multiple trees
