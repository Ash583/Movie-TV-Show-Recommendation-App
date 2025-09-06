from flask import Flask, render_template, request
from tmdb_api import search_movies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        if query != "":
            results = search_movies(query)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)
