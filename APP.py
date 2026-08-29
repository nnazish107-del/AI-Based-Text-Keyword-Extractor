from flask import Flask, render_template, request
from rake_nltk import Rake
import nltk

app = Flask(__name__)


# Download NLTK data
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


@app.route("/", methods=["GET", "POST"])
def index():
    keywords = []
    error = None

    if request.method == "POST":
        text = request.form.get("text", "")

        if not text.strip():
            error = "Please enter some text to extract keywords."

        else:
            r = Rake()
            r.extract_keywords_from_text(text)
            keywords = r.get_ranked_phrases()

    return render_template(
        "index.html",
        keywords=keywords,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
