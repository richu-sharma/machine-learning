# 📊 Multiple Linear Regression

## Overview

Multiple Linear Regression is a supervised machine learning algorithm used to predict a dependent variable using **two or more independent variables**.

Unlike simple linear regression, which uses one feature, multiple regression uses **multiple features to improve prediction accuracy**.

---

## Example Problem

Predict **house price** using multiple factors:

* House Size (sqft)
* Number of Bedrooms
* Age of the house

---

## Sample Dataset

| Size (sqft) | Bedrooms | Age | Price  |
| ----------- | -------- | --- | ------ |
| 1000        | 2        | 10  | 200000 |
| 1500        | 3        | 8   | 300000 |
| 2000        | 3        | 6   | 400000 |
| 2500        | 4        | 4   | 500000 |
| 3000        | 4        | 2   | 600000 |

---

## Model Equation

The regression equation becomes:

```
Price = b0 + b1(Size) + b2(Bedrooms) + b3(Age)
```

Where:

* **b0** = intercept
* **b1, b2, b3** = coefficients

---

## Libraries Used

* pandas
* scikit-learn

---

## How to Run

Install required libraries:

```
pip install pandas scikit-learn
```

Run the program:

```
python multiple_linear_regression.py
```

---

## Learning Outcomes

✔ Understanding regression with multiple features
✔ Training machine learning models with multiple inputs
✔ Predicting real-world values using Python
