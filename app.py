from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample keywords for scam detection
SCAM_KEYWORDS = ["phishing", "investment scam", "crypto", "forex", "fake", "guaranteed returns"]

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Analyze route
@app.route('/analyze', methods=['POST'])
def analyze():
    ad_text = request.form.get('ad_text', '')

    if not ad_text:
        return jsonify({"error": "Ad text is required"}), 400

    # Simple scam detection logic
    prediction = "Scam" if any(keyword in ad_text.lower() for keyword in SCAM_KEYWORDS) else "Legit"
    is_suspicious = prediction == "Scam"
    scam_match = any(keyword in ad_text.lower() for keyword in SCAM_KEYWORDS)

    return jsonify({
        "prediction": prediction,
        "is_suspicious": is_suspicious,
        "scam_match": scam_match
    })

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
