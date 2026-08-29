from flask import Flask, render_template, request
from rake_nltk import Rake
import nltk
import time

# Download required NLTK data
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    keywords = []
    error = None

    if request.method == "POST":
        text = request.form.get("text", "")

        if not text.strip():
            error = "Please enter some text to extract keywords."
        else:
            time.sleep(1)

            r = Rake()
            r.extract_keywords_from_text(text)
            keywords = r.get_ranked_phrases()

    return render_template(
        "index.html",
        keywords=keywords,
        error=error
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8501,
        debug=False,
        use_reloader=False
    )
