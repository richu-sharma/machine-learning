# 📊 Lasso Regression

## Overview

Lasso Regression is a regularization technique used in linear regression to reduce model complexity.

It uses **L1 regularization**, which can shrink some coefficients to **zero**, effectively performing **feature selection**.

## Formula

Cost function:

J = RSS + λ Σ |β|

Where:

* RSS = Residual Sum of Squares
* λ = Regularization parameter
* β = coefficients

## Libraries Used

* pandas
* scikit-learn

## How to Run

Install dependencies:

pip install pandas scikit-learn

Run program:

python lasso_regression.py
