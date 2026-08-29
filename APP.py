import streamlit as st
from rake_nltk import Rake
import nltk

# Download required NLTK data
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

# Page configuration
st.set_page_config(
    page_title="AI Text Keyword Extractor",
    page_icon="🔑",
    layout="centered"
)

st.title("🔑 AI-Based Text Keyword Extractor")
st.write("Enter some text below and I'll extract the most important keywords.")

# Text input
text = st.text_area(
    "Enter your text:",
    height=250,
    placeholder="Paste or type your text here..."
)

# Extract button
if st.button("Extract Keywords"):
    if not text.strip():
        st.error("Please enter some text to extract keywords.")
    else:
        with st.spinner("Extracting keywords..."):
            r = Rake()
            r.extract_keywords_from_text(text)
            keywords = r.get_ranked_phrases()

        if keywords:
            st.subheader("Extracted Keywords")

            for keyword in keywords:
                st.write("🔹", keyword)
        else:
            st.warning("No keywords could be extracted.")
