from flask import Flask, render_template, request
from jinja_templates import intro, jetsons_details, jetsons_trivia
import random

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html", intro=intro)

@app.get("/chars")
def chars():
    return render_template("chars.html")

@app.get("/check_name/<name>")
def check_name(name):
    return str(name.lower() in jetsons_details)

@app.get("/details/<name>")
def details(name):
    jetson = jetsons_details.get(name, '')
    return render_template("details.html", jetson=jetson)

@app.get("/trivia")
def trivia():
    # return render_template("trivia.html", trivia=random.choice(jetsons_trivia))  # Does not get an index.
    idx = random.randrange(0, len(jetsons_trivia))
    return render_template("trivia.html", trivia=jetsons_trivia[idx], q_id=idx)

@app.get("/trivia/<int:q_id>")
def trivia_check(q_id):
    guess = request.args.get('guess', '')
    return str(jetsons_trivia[q_id]['answer'] == guess)
