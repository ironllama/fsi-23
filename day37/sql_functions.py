from flask import Flask
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

engine = sqlalchemy.create_engine('mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23')

@app.get('/')
def home():
    resString = '<style>table { border-spacing: 0; } th { text-align: left; } th, td { margin: 0; border: 1px solid black; }</style>'
    with engine.begin() as db:
        resString += "<h3>Q1</h3>"
        res = db.execute(text('SELECT UPPER(brand) as upper_brand, LOWER(model) as lower_model FROM phones'))
        resString += '<table><tr><th>Brand</th><th>Model</th></tr>'
        for row in res:
            resString += f'<tr><td>{row.upper_brand}</td><td>{row.lower_model}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q2</h3>"
        res = db.execute(text("SELECT CONCAT(owner, ' ---- ', model, '(', brand, ')', price, '$') FROM phones"))
        resString += '<table><tr><th>Phone List</th></tr>'
        for row in res:
            resString += f'<tr><td>{row[0]}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q3</h3>"
        res = db.execute(text("SELECT model, LENGTH(comment) as length_comment FROM phones"))
        resString += '<table><tr><th>model</th><th>length comment</th></tr>'
        for row in res:
            resString += f'<tr><td>{row.model}</td><td>{row.length_comment}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q4</h3>"
        res = db.execute(text("SELECT AVG(weight) FROM phones WHERE owner='Brad'"))
        resString += '<table><tr><th>Average Phone\'s weight</th></tr>'
        for row in res:
            resString += f'<tr><td>{row[0]}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q5</h3>"
        res = db.execute(text("SELECT SUM(price) AS sum_price, owner FROM phones WHERE owner='Brad' OR owner='Roland' GROUP BY owner"))
        resString += '<table><tr><th>Owner</th><th>Total price</th></tr>'
        for row in res:
            resString += f'<tr><td>{row.sum_price}</td><td>{row.owner}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q6</h3>"
        res = db.execute(text("SELECT MAX(price) FROM phones WHERE owner='Richard'"))
        resString += '<table><tr><th>Price</th></tr>'
        for row in res:
            resString += f'<tr><td>{row[0]}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q7</h3>"
        res = db.execute(text("SELECT MIN(price) FROM phones WHERE owner='Frank'"))
        resString += '<table><tr><th>Price</th></tr>'
        for row in res:
            resString += f'<tr><td>{row[0]}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q8</h3>"
        res = db.execute(text("SELECT COUNT(*), owner FROM phones WHERE owner='Brad' OR owner='Stacy' GROUP BY owner"))
        resString += '<table><tr><th>owner</th><th>Total amount</th></tr>'
        for row in res:
            resString += f'<tr><td>{row[0]}</td><td>{row[1]}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q9</h3>"
        res = db.execute(text("SELECT COUNT(*), owner FROM phones GROUP BY owner"))
        resString += '<table><tr><th>owner</th><th>Total amount</th></tr>'
        for row in res:
            resString += f'<tr><td>{row[1]}</td><td>{row[0]}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q10</h3>"
        res = db.execute(text("SELECT COUNT(*), brand FROM phones GROUP BY brand"))
        resString += '<table><tr><th>brand</th><th>Total amount</th></tr>'
        for row in res:
            resString += f'<tr><td>{row[1]}</td><td>{row[0]}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q11</h3>"
        res = db.execute(text("SELECT brand, ROUND(AVG(price)) AS avg_price, COUNT(*) AS amt FROM phones GROUP BY brand HAVING avg_price < 125"))
        resString += '<table><tr><th>brand</th><th>Average Price</th><th>Phone Amount</th></tr>'
        for row in res:
            resString += f'<tr><td>{row.brand}</td><td>{row.avg_price}</td><td>{row.amt}</td></tr>'
        resString += '</table>'

        resString += '<br><br>'

        resString += "<h3>Q12</h3>"
        res = db.execute(text("SELECT brand, COUNT(*) AS amt FROM phones WHERE weight > 170 GROUP BY brand HAVING amt > 3"))
        resString += '<table><tr><th>brand</th><th>Phone Amount</th></tr>'
        for row in res:
            resString += f'<tr><td>{row.brand}</td><td>{row.amt}</td></tr>'
        resString += '</table>'
    resString += "<script>setTimeout(() => { window.scrollTo(0, document.body.scrollHeight); }, 100)</script>"

    return resString

if __name__ == "__main__":
    app.run(debug=True)
