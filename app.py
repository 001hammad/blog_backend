import logging
logging.basicConfig(level=logging.DEBUG)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Codify Blog API is UP!"

@app.route('/ping')
def ping():
    return "pong"
