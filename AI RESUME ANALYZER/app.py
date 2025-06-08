from flask import Flask, request, jsonify, render_template
import spacy
from PyPDF2 import PdfReader
from docx import Document
import os

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Create uploads directory if needed
os.makedirs('uploads', exist_ok=True)


@app.route("/")
def home():
    """Render the main upload page"""
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_resume():
    """Handle resume file upload and analysis"""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save file temporarily
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    try:
        text = extract_text_from_file(filepath)
        analysis = analyze_text(text)
        # Include filename in response
        analysis['filename'] = file.filename
        return jsonify(analysis)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)


def extract_text_from_file(filepath):
    """Extract text from PDF or DOCX files"""
    text = ""
    if filepath.endswith('.pdf'):
        with open(filepath, 'rb') as f:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    elif filepath.endswith('.docx'):
        doc = Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text.strip()


def analyze_text(text):
    """Analyze resume text and return insights"""
    if not text:
        return {"error": "No text found in document"}

    doc = nlp(text)
    target_skills = {
        "Python", "JavaScript", "Flask", "SQL", "API", "Postman",
        "HTML", "CSS", "Git", "React", "Node.js", "Django", "MongoDB"
    }

    found_skills = set()
    for token in doc:
        if token.text in target_skills:
            found_skills.add(token.text)
    for chunk in doc.noun_chunks:
        if chunk.text in target_skills:
            found_skills.add(chunk.text)

    score = min(100, len(found_skills) * 10)

    return {
        "skills": sorted(list(found_skills)),
        "score": score,
        "suggestions": generate_suggestions(found_skills),
        "word_count": len(text.split())
    }


def generate_suggestions(found_skills):
    """Generate improvement suggestions"""
    priority_skills = ["Python", "JavaScript", "Git", "SQL"]
    return [f"Add '{skill}' experience" for skill in priority_skills
            if skill not in found_skills]


if __name__ == "__main__":
    app.run(debug=True)