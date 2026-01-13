from flask import Flask, request, render_template, jsonify
from ai import process_csv, chat_with_ai

# Create the Flask app
app = Flask(__name__)

# Home page – serves the HTML frontend
@app.route("/")
def home():
    return render_template("index.html")

# Endpoint for uploading a CSV file with transactions
@app.route("/upload", methods=["POST"])
def upload():
    # Get the uploaded file from the request
    file = request.files["file"]

    # Send the file to the AI logic for analysis
    insights = process_csv(file)

    # Return the AI-generated insights as JSON
    return jsonify({"insights": insights})

# Chat endpoint – user asks questions about their spending
@app.route("/chat", methods=["POST"])
def chat():
    # Read the user message from JSON body
    user_message = request.json["message"]

    # Ask the AI to reason about the message
    response = chat_with_ai(user_message)

    return jsonify({"response": response})

# Run the app in debug mode for development
if __name__ == "__main__":
    app.run(debug=True)
