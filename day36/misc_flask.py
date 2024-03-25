from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@localhost:3306/fsi-23")
# db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")

@app.get("/phones")
def phones():
    returnStr = ""

    with db.begin() as conn:
        response = conn.execute(text("SELECT * FROM phones"))
        for phone in response:
            # returnStr.append(f"One {phone[2]} {phone[1]} costs ${phone[4]}")
            # returnStr.append(f"One {phone.brand} {phone.model} costs ${phone.price}")
            returnStr += f"""
            <p>
                <strong>Phone</strong>: { phone.model } <br />
                The owner of this phone is: { phone.owner }, and sells the phone at the price of { phone.price } dollars! <br />
                This phone brand is { phone.brand } and weight { phone.weight }g at maximum.<br />
                { phone.owner } had given this comment { phone.model}: <em>{ phone.comment }</em>
            </p>
            """

        returnStr += "\n<br><br>\n"

        response = conn.execute(text("SELECT model FROM phones"))
        for phone in response:
            returnStr += f"{phone.model}<br>"

        returnStr += "\n<br><br>\n"

        response = conn.execute(text("SELECT model, owner FROM Phones WHERE owner='Stacy'"))
        for phone in response:
            returnStr += f"{phone.model} belongs to {phone.owner}.<br>"

        returnStr += "\n<br><br>\n"

        response = conn.execute(text("SELECT model, owner FROM Phones WHERE owner='Stacy' AND price < 50"))
        for phone in response:
            returnStr += f"{phone.model} belongs to {phone.owner}.<br>"

        returnStr += "\n<br><br>\n"

        response = conn.execute(text("SELECT * FROM Phones ORDER BY price"))
        for phone in response:
            returnStr += f"{phone.model} costs ${phone.price}<br>"

        returnStr += "\n<br><br>\n"

        response = conn.execute(text("SELECT * FROM Phones ORDER BY price DESC"))
        for phone in response:
            returnStr += f"{phone.model} costs ${phone.price}<br>"


        returnStr += "\n<br><br>\n"

        response = conn.execute(text("SELECT * FROM Phones LIMIT 0, 10"))
        for phone in response:
            returnStr += f"{phone.model}<br>"

        returnStr += "\n<br><br>\n"

        # Do not accept uncontrolled variables in your SQL statements.
        # response = conn.execute(text(
        #     f"SELECT model, price, owner FROM Phones WHERE owner='{request.args.get('owner', '')}'"
        # ))

        # Instead, use a parameterized query, with param names using colons(:)
        response = conn.execute(
            text(f"SELECT model, price, owner FROM Phones WHERE owner=:person"),
            { "person": request.args.get('owner', '')}
            )
        
        for phone in response:
            returnStr += f"{phone.owner}: {phone.model} (${phone.price})<br>"


        returnStr += "\n<br><br>\n"

        # Force scrolling to the bottom of the page
        returnStr += "<script>setTimeout(() => { window.scrollTo(0, document.body.scrollHeight); }, 500)</script>"

    return returnStr
