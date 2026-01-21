from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('../results/gdpr_report.json', 'r') as f:
        report = json.load(f)
    return render_template('index.html', report=report)

if __name__ == "__main__":
    app.run(debug=True)
