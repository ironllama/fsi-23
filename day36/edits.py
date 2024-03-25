from flask import Flask, render_template

app = Flask(__name__)

import sqlalchemy
from sqlalchemy.sql import text

db = sqlalchemy.create_engine('mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23')
# db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")

@app.get('/edits')
def edits():
    returnStr = ''

    with db.begin() as conn:
        res = conn.execute(
            text("""
                INSERT INTO phones (model, brand, owner, price, weight, comment)
                VALUES ('s8', 'Samsung', 'Alexis', 173, 'Good for watching videos', 80)
                """),
        )
        returnStr += f'<h3>Q1: {res.rowcount}</h3>'        

        res = conn.execute(
            text('INSERT INTO phones (model, brand, owner, price, weight, comment) VALUES (:model, :brand, :owner, :price, :weight, :comment)'),
            {
                'brand': 'Apple',
                'model': 'Iphone 12',
                'owner': 'Alex',
                'weight': 164,
                'comment': 'my company provided a phone i don’t need this one anymore, brand new',
                'price': 700,
            }
        )
        returnStr += f'<h3>Q2: {res.rowcount}</h3>'

        res = conn.execute(
            text("""
                UPDATE phones SET price=690 WHERE owner='Alex' AND model='Iphone 12'
                """),
        )
        returnStr += f'<h3>Q3: {res.rowcount}</h3>'        

        res = conn.execute(
            text('UPDATE phones SET comment=comment + :comment WHERE owner=:owner'),
            # If you are using the pymysql driver, use CONCAT instead of '+'
            # text('UPDATE phones SET comment=CONCAT(comment, :comment) WHERE owner=:owner'),
            {
                'comment': ' And listening to music',
                'owner': 'Alexis',
           }
        )
        returnStr += f'<h3>Q4: {res.rowcount}</h3>'

        res = conn.execute(
            text('DELETE FROM phones WHERE owner=:owner AND model=:model'),
            {
                'model': 's8',
                'owner': 'Alexis',
            }
        )
        returnStr += f'<h3>Q5: {res.rowcount}</h3>'

    return returnStr

if __name__ == '__main__':
    app.run(debug=True)
