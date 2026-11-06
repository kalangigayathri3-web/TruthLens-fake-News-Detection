# import streamlit as st
# import pickle
# import requests
# import re

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="TruthLens | Fake News Detector",
#     page_icon="📰",
#     layout="wide"
# )
# # Store prediction history
# if "history" not in st.session_state:
#     st.session_state.history = []

# # ---------------- CUSTOM DESIGN ----------------
# st.markdown("""
# <style>
# .main {
#     background-color: #f5f7fb;
# }
# .title {
#     text-align: center;
#     font-size: 38px;
#     font-weight: bold;
#     color: #17365d;
# }
# .subtitle {
#     text-align: center;
#     color: #555;
#     font-size: 17px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- LOAD MODEL ----------------
# @st.cache_resource
# def load_model():
#     with open("model.pkl", "rb") as f:
#         model = pickle.load(f)

#     with open("vectorizer.pkl", "rb") as f:
#         vectorizer = pickle.load(f)

#     return model, vectorizer


# try:
#     model, vectorizer = load_model()
# except FileNotFoundError:
#     st.error("Model files not found. Run python main.py first.")
#     st.stop()

# # ---------------- TEXT CLEANING ----------------
# def clean_text(text):
#     text = str(text).lower()
#     text = re.sub(r"[^a-zA-Z\s]", "", text)
#     return text


# # ---------------- FACT CHECK API ----------------
# def fact_check_news(news, api_key):

#     url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

#     params = {
#         "query": news,
#         "languageCode": "en",
#         "pageSize": 5,
#         "key": api_key
#     }

#     try:
#         response = requests.get(
#             url, params=params, timeout=20
#         )
#         response.raise_for_status()
#         return response.json()

#     except requests.exceptions.RequestException:
#         return None


# # ---------------- HEADER ----------------
# st.markdown(
#     '<div class="title">📰 TruthLens</div>',
#     unsafe_allow_html=True
# )

# st.markdown(
#     '<div class="subtitle">AI-Powered Fake News Detection & Fact Checking</div>',
#     unsafe_allow_html=True
# )

# st.write("")
# st.info(
#     "Enter a news headline and article to analyze its content."
# )

# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     st.title("About TruthLens")
#     st.write("""
#     This project combines:

#     - Machine Learning
#     - TF-IDF Vectorization
#     - Logistic Regression
#     - Google Fact Check Tools API
#     - Streamlit

#     **Purpose:** Help users examine news claims.
#     """)

# # ---------------- USER INPUT ----------------
# st.subheader("Enter News Details")

# title = st.text_input(
#     "News Headline",
#     placeholder="Enter the news headline..."
# )

# article = st.text_area(
#     "News Article",
#     height=220,
#     placeholder="Paste the complete news article here..."
# )

# # ---------------- ANALYZE BUTTON ----------------
# if st.button("🔍 Analyze News", use_container_width=True):

#     if not title.strip() and not article.strip():
#         st.warning("Please enter a headline or news article.")

#     else:
#         combined_news = clean_text(title) + " " + clean_text(article)

#         # -------- ML PREDICTION --------
#         st.divider()
#         st.subheader("1. Machine Learning Result")

#         news_vector = vectorizer.transform([combined_news])

#         prediction = model.predict(news_vector)[0]
# probabilities = model.predict_proba(news_vector)[0]

# fake_confidence = probabilities[0] * 100
# real_confidence = probabilities[1] * 100

# result_label = "Fake News" if prediction == 0 else "Real News"

# st.session_state.history.append({
#     "Headline": title if title.strip() else "No headline",
#     "Prediction": result_label,
#     "Fake Confidence": f"{fake_confidence:.2f}%",
#     "Real Confidence": f"{real_confidence:.2f}%"
# })

# if prediction == 0:
#             st.error("🚨 Prediction: Fake News")
#     else:   
#             st.success("✅ Prediction: Real News")

#             st.metric(
#             "Model Confidence",
#             f"{confidence:.2f}%"
#         )

#             st.progress(float(confidence / 100))

#         st.caption(
#             "Confidence is the model's classification score, "
#             "not proof that the claim is true."
#         )

#         # -------- GOOGLE FACT CHECK --------
#         st.divider()
#         st.subheader("2. Existing Fact-Check Reports")

#         try:
#             api_key = st.secrets["GOOGLE_FACT_CHECK_API_KEY"]
#         except (KeyError, FileNotFoundError):
#             api_key = None

#         if not api_key:
#             st.warning(
#                 "API key not configured. Check .streamlit/secrets.toml."
#             )

#         else:
#             search_query = title.strip() or article[:300]

#             with st.spinner("Searching fact-check reports..."):
#                 result = fact_check_news(search_query, api_key)

#             if result is None:
#                 st.error("Fact-check service could not be reached.")

#             else:
#                 claims = result.get("claims", [])

#                 if not claims:
#                     st.info(
#                         "No matching reports found. "
#                         "This does not mean the news is true or false."
#                     )

#                 else:
#                     st.write(f"Reports found: {len(claims)}")

#                     for i, claim in enumerate(claims, start=1):
#                         with st.expander(f"Fact-Check Report {i}"):

#                             st.write(
#                                 "**Claim:**",
#                                 claim.get("text", "Not available")
#                             )

#                             st.write(
#                                 "**Claimant:**",
#                                 claim.get("claimant", "Not available")
#                             )

#                             for review in claim.get("claimReview", []):

#                                 publisher = review.get("publisher", {})

#                                 st.write(
#                                     "**Publisher:**",
#                                     publisher.get("name", "Not available")
#                                 )

#                                 st.write(
#                                     "**Rating:**",
#                                     review.get(
#                                         "textualRating", "Not available"
#                                     )
#                                 )

#                                 st.write(
#                                     "**Review Date:**",
#                                     review.get(
#                                         "reviewDate", "Not available"
#                                     )
#                                 )

#                                 report_url = review.get("url")

#                                 if report_url:
#                                     st.markdown(
#                                         f"[Read Full Report]({report_url})"
#                                     )

# # ---------------- PREDICTION HISTORY ----------------
# st.divider()
# st.subheader("3. Prediction History")

# if st.session_state.history:

#     for i, item in enumerate(
#         reversed(st.session_state.history), start=1
#     ):
#         st.write(f"**{i}. {item['Headline']}**")
#         st.write("Prediction:", item["Prediction"])
#         st.write("Confidence:", item["Confidence"])
#         st.divider()

#     if st.button("Clear History"):
#         st.session_state.history = []
#         st.rerun()

# else:
#     st.info("No previous predictions available.")
# # ---------------- FOOTER ----------------
# st.divider()

# st.caption(
#     "TruthLens | Fake News Detection and Fact-Checking Project"
# )

# st.warning(
#     "Important: ML predictions are not verified facts. "
#     "Always check reliable sources before trusting a news claim."
# )
import streamlit as st
import pickle
import requests
import re
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="TruthLens",
    page_icon="🔍",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.title {
    text-align: center;
    color: #243b64;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 17px;
}
.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #eaf1ff;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    '<div class="title">🔍 TruthLens</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Fake News Detection & Fact Checking</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- SESSION HISTORY ----------------

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

# ---------------- TEXT CLEANING ----------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text

# ---------------- GOOGLE FACT CHECK ----------------

def google_fact_check(query):
    api_key = st.secrets.get("GOOGLE_FACT_CHECK_API_KEY", "")

    if not api_key:
        return None, "Google Fact Check API key not configured."

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

    params = {
        "query": query,
        "key": api_key,
        "pageSize": 5
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        claims = data.get("claims", [])

        if not claims:
            return [], None

        return claims, None

    except requests.RequestException:
        return None, "Unable to connect to Google Fact Check right now."

# ---------------- INPUT SECTION ----------------

st.subheader("📰 Enter News Details")

title = st.text_input(
    "News Headline",
    placeholder="Enter news headline..."
)

article = st.text_area(
    "News Article",
    placeholder="Paste the complete news article here...",
    height=200
)

analyze = st.button(
    "🔍 Analyze News",
    use_container_width=True
)

# ---------------- PREDICTION ----------------

if analyze:

    if not title.strip() and not article.strip():
        st.warning("Please enter a headline or news article.")

    else:
        try:
            model, vectorizer = load_model()

            combined_text = title + " " + article
            cleaned_text = clean_text(combined_text)

            news_vector = vectorizer.transform([cleaned_text])

            prediction = model.predict(news_vector)[0]
            probabilities = model.predict_proba(news_vector)[0]

            fake_confidence = probabilities[0] * 100
            real_confidence = probabilities[1] * 100

            result_label = (
                "Fake News" if prediction == 0
                else "Real News"
            )

            # Display result

            st.divider()
            st.subheader("📊 ML Prediction Result")

            if prediction == 0:
                st.error("⚠️ Prediction: FAKE NEWS")
            else:
                st.success("✅ Prediction: REAL NEWS")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Fake News Confidence",
                    f"{fake_confidence:.2f}%"
                )

            with col2:
                st.metric(
                    "Real News Confidence",
                    f"{real_confidence:.2f}%"
                )

            st.progress(float(fake_confidence / 100))

            st.caption(
                "Confidence scores represent the model's estimates, "
                "not the probability that a news claim is true."
            )

            # Save history

            st.session_state.history.append({
                "Headline": title if title.strip() else "No headline",
                "Prediction": result_label,
                "Fake Confidence": f"{fake_confidence:.2f}%",
                "Real Confidence": f"{real_confidence:.2f}%"
            })

            # Google fact check

            st.divider()
            st.subheader("🌐 Google Fact Check Results")

            search_query = title.strip() or article[:200]

            claims, error = google_fact_check(search_query)

            if error:
                st.info(error)

            elif not claims:
                st.info(
                    "No matching fact-check reports found. "
                    "This does not prove that the news is true or false."
                )

            else:
                for claim in claims:
                    st.markdown(
                        f"**Claim:** {claim.get('text', 'Not available')}"
                    )

                    for review in claim.get("claimReview", []):
                        st.write(
                            "Publisher:",
                            review.get("publisher", {}).get(
                                "name", "Unknown"
                            )
                        )

                        st.write(
                            "Rating:",
                            review.get("textualRating", "Not available")
                        )

                        review_url = review.get("url")

                        if review_url:
                            st.markdown(
                                f"[Read Fact Check Report]({review_url})"
                            )

                    st.divider()

        except FileNotFoundError:
            st.error(
                "Model files not found. Keep model.pkl and "
                "vectorizer.pkl in the same folder as app.py."
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")

# ---------------- PREDICTION HISTORY ----------------

st.divider()
st.subheader("📜 Prediction History")

if st.session_state.history:

    st.dataframe(
        st.session_state.history,
        use_container_width=True
    )

    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()

else:
    st.info("No previous predictions available.")

# ---------------- ABOUT ----------------

st.divider()

with st.expander("ℹ️ About TruthLens"):
    st.write("""
    TruthLens is a machine-learning-based fake news detection
    and fact-checking prototype.

    It uses:
    - TF-IDF for text feature extraction
    - Logistic Regression for classification
    - Google Fact Check Tools API for matching reports

    Important:
    ML predictions are not proof of whether a news claim is true.
    Always verify important information using reliable sources.
    """)

st.caption(
    "TruthLens | Educational Project | AI-Based News Analysis"
)