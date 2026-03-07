# 📉 Ridge Regression

## Overview

Ridge Regression is a type of **linear regression with regularization**.

It adds a **penalty term** to the loss function to prevent overfitting and improve model generalization.

The penalty term is based on the **L2 regularization**.

## Formula

Ridge regression modifies the cost function:

J = RSS + λ Σ (β²)

Where:

* RSS = Residual Sum of Squares
* λ = Regularization parameter
* β = model coefficients

## Libraries Used

* pandas
* scikit-learn

## How to Run

Install dependencies:

pip install pandas scikit-learn

Run program:

python ridge_regression.py
