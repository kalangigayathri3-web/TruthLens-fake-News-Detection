🔍 TruthLens – AI-Powered Fake News Detection

📌 About the Project

TruthLens is a machine learning-based web application that helps users analyze news articles and identify potentially fake or real news.

It also searches for existing fact-check reports using the Google Fact Check Tools API.

✨ Features

- Fake and Real News Prediction
- Machine Learning-based Classification
- TF-IDF Text Vectorization
- Google Fact Check API Integration
- Prediction Confidence Scores
- Prediction History
- Interactive Streamlit Interface

🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- TF-IDF
- Google Fact Check Tools API

📂 Project Structure

TruthLens/
│
├── app.py
├── main.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── dataset/
│   ├── Fake.csv
│   └── True.csv
└── README.md

⚙️ Installation and Setup

1. Clone this repository:

git clone https://github.com/kalangigayathri3-web/TruthLens-fake-News-Detection.git

2. Open the project folder.

3. Install required packages:

pip install -r requirements.txt

4. Run the application:

streamlit run app.py

🔑 Google Fact Check API

Configure your Google Fact Check API key using Streamlit secrets.

Create ".streamlit/secrets.toml" and add:

GOOGLE_FACT_CHECK_API_KEY = "YOUR_API_KEY"

Never upload your actual API key to GitHub.

⚠️ Disclaimer

TruthLens is an educational machine learning prototype. Its predictions are not verified facts. Always cross-check news with reliable sources.

👩‍💻 Author

K. Gayathri

B.Tech – Computer Science and Engineering
