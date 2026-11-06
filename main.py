import pandas as pd
import re
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load datasets
fake = pd.read_csv("dataset/Fake.csv")
real = pd.read_csv("dataset/True.csv")

# 2. Add labels
fake["label"] = 0
real["label"] = 1

# 3. Combine datasets
data = pd.concat([fake, real], ignore_index=True)

print("Original dataset shape:", data.shape)

# 4. Remove duplicate rows
data = data.drop_duplicates()

# 5. Handle missing values
data["title"] = data["title"].fillna("")
data["text"] = data["text"].fillna("")

# 6. Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

data["title"] = data["title"].apply(clean_text)
data["text"] = data["text"].apply(clean_text)

# Combine title and text
data["content"] = data["title"] + " " + data["text"]

# 7. Separate input and output
X = data["content"]
y = data["label"]

# 8. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 9. Convert text into numbers using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# 10. Create and train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("\nModel Training Completed!")

# 11. Test model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 12. Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

# 13. Save vectorizer
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("\nModel and Vectorizer Saved Successfully!")