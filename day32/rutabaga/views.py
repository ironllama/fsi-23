from rutabaga import app
from flask import render_template, request

@app.route("/")
def index():
  return render_template("show_kid.html")

@app.route("/info")
def info():
  user = request.args.get('user', 'George')
  return render_template("greetings.html", name=user)
