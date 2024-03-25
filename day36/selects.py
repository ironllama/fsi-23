from flask import Flask, render_template

app = Flask(__name__)

import sqlalchemy
from sqlalchemy.sql import text

db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23")
# db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")

@app.get("/selects")
def selects():
    allPhones = []

    with db.begin() as conn:
        res = conn.execute(
            text('select * from phones where owner = :owner'),
            { 'owner': 'Stacy'}
        )
        phones = render_template('phone.html', phones=res, title='Q1')
        allPhones.append(phones)

        res = conn.execute(
            text('select * from phones where weight = :weight'),
            { 'weight': 295}
        )
        phones = render_template('phone.html', phones=res, title='Q2')
        allPhones.append(phones)

        res = conn.execute(
            text('select * from phones where brand = :brand'),
            { 'brand': 'Nokia'}
        )
        phones = render_template('phone.html', phones=res, title='Q3')
        allPhones.append(phones)

        res = conn.execute(
            text('select * from phones where brand = :brand1 or brand = :brand2'),
            { 'brand1': 'Nokia', 'brand2': 'Apple' }
        )
        phones = render_template('phone.html', phones=res, title='Q4')
        allPhones.append(phones)

        res = conn.execute(
            text('select * from phones where price = :price'),
            { 'price': 115}
        )
        phones = render_template('phone.html', phones=res, title='Q5')
        allPhones.append(phones)

        res = conn.execute(
            text('select * from phones order by weight'),
        )
        phones = render_template('phone.html', phones=res, title='Q6')
        allPhones.append(phones)

        res = conn.execute(
            text('select * from phones where owner = :owner limit :limit'),
            { 'owner': 'Victoria', 'limit': 5 }
        )
        phones = render_template('phone.html', phones=res, title='Q7')
        allPhones.append(phones)

        res = conn.execute(
            text('select * from phones where owner = :owner and price < :price order by price desc'),
            { 'owner': 'Nina', 'price': 250 }
        )
        phones = render_template('phone.html', phones=res, title='Q8')
        allPhones.append(phones)

        return "<br><br>".join(allPhones)

if __name__ == "__main__":
    app.run(debug=True)
