from flask import Flask, request

app = Flask(__name__)

@app.get("/top")
def top():
    in_snack = request.args.get('snack', 'Water')
    return f"GET: {in_snack} is a good choice! I like it, too."

@app.post("/bottom")
def bottom():
    in_snack = request.form.get('snack', 'Water')
    return f"POST: {in_snack} is a good choice! I like it, too."

@app.route("/topbottom", methods=['GET', 'POST'])
def topbottom():
    if request.method == 'GET':
        in_snack = request.args.get('snack', 'Water')
    else:
        in_snack = request.form.get('snack', 'Water')

    return f"{request.method.upper()}: {in_snack} is a good choice! I like it, too."

@app.route("/topbottomnina/<snack>", methods=['GET','POST'])
def topbottomnina(snack):
    return f"{request.method.upper()}: {snack} is a good choice! I like it, too."
