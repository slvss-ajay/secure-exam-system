from flask import Flask, render_template, request, jsonify
import base64
from datetime import datetime

app = Flask(__name__)

MODEL_ANSWER = "Cloud computing allows data storage and processing over the internet."

logs = []

# Encryption
def encrypt(data):
    return base64.b64encode(data.encode()).decode()

def decrypt(data):
    return base64.b64decode(data.encode()).decode()

# Improved AI scoring
def evaluate_answer(student_answer):
    student = student_answer.lower()
    score = 0

    keywords = ["cloud", "data", "storage", "internet", "processing"]

    for word in keywords:
        if word in student:
            score += 2

    if len(student.split()) > 8:
        score += 2

    return min(score, 10)

# Secure processing
def secure_evaluation(encrypted_answer):
    answer = decrypt(encrypted_answer)
    return evaluate_answer(answer)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    answer = data['answer']

    encrypted = encrypt(answer)
    score = secure_evaluation(encrypted)

    log = {
        "score": score,
        "time": str(datetime.now())
    }
    logs.append(log)

    return jsonify({
        "encrypted": encrypted,
        "score": score,
        "logs": logs
    })

if __name__ == '__main__':
    app.run(debug=True)