# 📊 Naive Bayes Classification

## Overview

Naive Bayes is a supervised machine learning algorithm used for **classification tasks**.

It is based on **Bayes' Theorem** and assumes that features are **independent of each other**.

Despite this simple assumption, Naive Bayes performs very well on many real-world problems such as **spam detection and text classification**.

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

```
pip install pandas scikit-learn
```

Run the program:

```
python naive_bayes_classifier.py
```

---

## Learning Outcomes

✔ Understanding probabilistic machine learning algorithms
✔ Applying Bayes theorem for classification
✔ Implementing Naive Bayes using Scikit-learn
