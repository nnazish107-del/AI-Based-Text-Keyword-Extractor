from flask import Flask, render_template, request
from rake_nltk import Rake
import nltk
import time

# Download required NLTK data (only first time)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    keywords = []
    error = None
    loading = False

    if request.method == "POST":
        text = request.form.get("text")

        # Handle empty input
        if not text or text.strip() == "":
            error = "Please enter some text to extract keywords."
        else:
            loading = True
            time.sleep(1)  # Simulate loading state

            # Keyword Extraction Logic
            r = Rake()
            r.extract_keywords_from_text(text)
            keywords = r.get_ranked_phrases()

    return render_template("index.html",
                           keywords=keywords,
                           error=error,
                           loading=loading)

if __name__ == "__main__":
    app.run(debug=True)
