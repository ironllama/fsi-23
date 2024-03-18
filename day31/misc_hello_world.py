from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Nik!</p>"

@app.route("/ping")
def ping():
    return "<p style='font-weight:bold;font-size:3rem;color:red;text-align:center;'>pong<p>"

@app.route("/party")
def partyparty():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dancing Salamander</title>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
    </style>
</head>
<body>
    <img src="static/dance.gif" alt="dancing salamander">
    <script>
        function randomBackground() {
            const decRan = Math.floor(Math.random() * 16777215);
            document.body.style.backgroundColor = "#" + decRan.toString(16);
            setTimeout(randomBackground, 250);
        }
        randomBackground();
    </script>
</body>
</html>
"""

# If you want to run directly as 'python hello_world.py'
# if __name__ == '__main__':
#     app.run(debug=True)