# 📈 Polynomial Regression

## Overview

Polynomial Regression is an extension of **Linear Regression** used when the relationship between variables is **non-linear**.

Instead of fitting a straight line, the model fits a **curved line** (polynomial curve) to the data.

---

## Dataset

In this example, we predict **salary based on job level**.

| Level | Salary |
| ----- | ------ |
| 1     | 45000  |
| 2     | 50000  |
| 3     | 60000  |
| 4     | 80000  |
| 5     | 110000 |
| 6     | 150000 |
| 7     | 200000 |

---

## Algorithm Concept

Polynomial Regression transforms the input variable into **higher degree polynomial features**.

Example equation:

```
y = b0 + b1x + b2x² + b3x³
```

This allows the model to capture **curved relationships**.

---

## Libraries Used

* pandas
* numpy
* scikit-learn

---

## How to Run

Install dependencies:

```
pip install pandas numpy scikit-learn
```

Run the program:

```
python polynomial_regression.py
```

---

## Learning Outcomes

✔ Understanding non-linear regression
✔ Using PolynomialFeatures in Scikit-learn
✔ Predicting values with polynomial models
