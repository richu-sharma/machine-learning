# Sentiment Analysis on Movie Reviews using Logistic Regression

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Example dataset (sample movie reviews)
reviews = [
    "This movie was amazing and very interesting",
    "I loved the acting and story",
    "Fantastic film with great performance",
    "The movie was boring and too long",
    "I did not like the storyline",
    "Terrible movie and bad acting"
]

labels = [1,1,1,0,0,0]  # 1 = positive, 0 = negative

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)
y = labels

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
