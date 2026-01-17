from flask import Flask, request, jsonify, render_template
from ollama_ai import generate_html

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    html = generate_html(prompt)

    return jsonify({"html": html})

if __name__ == "__main__":
    app.run(debug=True)
