from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>PARTH'S KISAN SAATHI 🚜</h1><p>Working Successfully ✅</p>"
