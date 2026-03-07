# 📈 Simple Linear Regression – House Price Prediction

## 🧠 Overview

**Simple Linear Regression** is a supervised machine learning algorithm used to model the relationship between **one independent variable** and **one dependent variable**.

In this project, we use Linear Regression to predict **house prices** based on **house size (in square feet)**.

The model learns the relationship between size and price and then predicts the price for a new house size.

---

## 📊 Sample Dataset

| House Size (sqft) | Price (₹) |
| ----------------- | --------- |
| 500               | 1,000,000 |
| 800               | 1,500,000 |
| 1000              | 1,800,000 |
| 1200              | 2,200,000 |
| 1500              | 2,700,000 |

This dataset is created directly inside the Python code for demonstration.

---

## ⚙️ Algorithm Used

We use **Linear Regression** from the **Scikit-learn** library.

The regression line follows the equation:

**Price = m × Size + b**

Where:

* **m** → slope of the line
* **b** → intercept

This line represents the **best fit for the dataset**.

---

## 🧰 Libraries Used

* **pandas** → data handling
* **scikit-learn** → machine learning model

---

## ▶️ How to Run the Code

### 1️⃣ Install required libraries

```
pip install pandas scikit-learn
```

### 2️⃣ Run the Python file

```
python simple_linear_regression.py
```

---

## 💻 Example Output

```
Predicted Price: 2900000
```

This means the model predicts that a **1600 sqft house** may cost approximately **₹29,00,000**.

---

## 📁 Project Structure

```
supervised_learning/
│
└── linear_regression
    │
    ├── simple_linear_regression.py
    └── README.md
```

---

## 🎯 Learning Outcomes

✔ Understanding **Supervised Learning**
✔ Training a **Linear Regression model**
✔ Making predictions using **Scikit-learn**
✔ Implementing machine learning with **Python**

---

⭐ This project is part of a **Machine Learning Algorithms Repository** where different supervised learning algorithms are implemented step by step.
