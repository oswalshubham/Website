import imp
from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# New functions

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/education/")
def education():
    return render_template("education.html")
