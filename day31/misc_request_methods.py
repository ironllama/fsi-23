from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def pong():
  return request.args.get("code") if "code" in request.args else "pong"


# GET requests
# ===========================
@app.get("/nameandcolor")
def name_color():
  in_name = request.args.get('name', 'Adam')
  in_color = request.args.get('color', 'black')
  return f"<h1 style='color: {in_color}'>Hello, {in_name}</h1>"


# POST requests
# ===========================
# Expects x-www-form-urlencoded data and returns 'text/plain'
@app.route("/add10", methods=['POST'])
def add10():
  print("ADD10: FORM:", request.form)
  in_form = request.form
  in_num = int(in_form.get('number', '0'))
  return str(in_num + 10)  # Must cast to string for return

# Expects application/json and return application/json
@app.post("/multiply10")
def multiply10():
  in_json = request.json
  in_num = int(in_json.get('number', '0'))
  return { "result": in_num * 10 }  # Dictionary gets turned into JSON string


# Both requests
# ===========================
@app.route('/both', methods=['POST', 'GET'])
def both():
  if request.method == 'POST':
    in_fruit = "peppers"
  else:
    in_fruit = "grapes"
  return in_fruit


# Path Variables
# ===========================
@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {username}'s Profile!"

# @app.route('/post/<post_id>')
# def show_post(post_id)
#   return f'Post {int(post_id) + 1}'

# Same as above, but with a converter with the path variable
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id + 1}'
    
@app.route('/product/<int:product_id>/<option_id>')
def show_product(product_id, option_id):
  return f'Product {product_id + 1} with option {option_id}'


# To show all built-in converters
# print(app.url_map.converters.keys())
