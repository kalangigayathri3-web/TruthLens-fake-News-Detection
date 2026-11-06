TruthLens – AI-Based Fake News Detection

TruthLens is an AI-powered Fake News Detection and Fact-Checking web application built using Python and Streamlit.

Project Overview

The main objective of TruthLens is to identify whether a given news article is likely to be Fake or Real using Machine Learning techniques.

It also integrates Google Fact Check Tools API to help users find relevant fact-check reports.

Features

- Fake and Real News Classification
- TF-IDF Text Feature Extraction
- Logistic Regression Machine Learning Model
- Google Fact Check API Integration
- Prediction Confidence Display
- User-Friendly Streamlit Interface
- Prediction History

Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Google Fact Check Tools API

Project Structure

TruthLens/
├── app.py
├── main.py
├── requirements.txt
├── model.pkl
├── vectorizer.pkl
├── dataset/
│   ├── Fake.csv
│   └── True.csv
└── .gitignore

Installation

1. Clone the repository:

git clone https://github.com/kalangigayathri3-web/TruthLens-fake-News-Detection.git

2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

streamlit run app.py

Important Note

Machine Learning predictions are not guaranteed to be accurate. Always verify important news using reliable sources and fact-check reports.

Project Purpose

This project is developed for educational purposes to demonstrate Machine Learning, Natural Language Processing, and fact-checking integration.

---

Developed by: K. Gayathri
