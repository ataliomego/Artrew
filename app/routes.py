from flask import request, jsonify
from app import app
from app.paraphrase import paraphrase_text

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Article Rewriter API is running!"})

@app.route("/rewrite", methods=["POST"])
def rewrite():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    if len(text) > 12000:
        return jsonify({"error": "Text exceeds maximum limit of 12,000 characters"}), 400

    rewritten_text = paraphrase_text(text)
    return jsonify({"rewritten_text": rewritten_text})
