import sqlalchemy
from sqlalchemy.sql import text

db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23")
# db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/fsi-23")

with db.begin() as conn:
    # response = conn.execute(text("SELECT * FROM phones"))
    # print("RESPONSE:", response)
    
    # # for row in response:
    # #     print(f"One {row[2]} {row[1]} costs ${row[4]}")

    # for row in response:
    #     print(f"One {row.brand} {row.model} costs ${row.price}")

    # response = conn.execute(text("CREATE TABLE fav_colors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, color VARCHAR(255))"))
    # print("RESPONSE:", response)
    
    # response = conn.execute(
    #     text("INSERT INTO fav_colors (name, color) VALUES (:name, :color)"),
    #     [
    #         {'name': 'Peter', 'color': 'red'},
    #         {'name': 'Paul', 'color': 'green'},
    #         {'name': 'Mary', 'color': 'blue'},
    #     ]
    #     )
    # print("RESPONSE:", response.rowcount)

    # response = conn.execute(
    #     text("INSERT INTO phones (model, brand, owner, price, weight, comment) VALUES (:model, :brand, :owner, :price, :weight, :comment)"),
    #     {
    #         'model': 'Iphone X',
    #         'brand': 'Apple',
    #         'owner': 'Brandon',
    #         'price': 150,
    #         'weight': 196,
    #         'comment': 'No scratches perfect state',
    #     }
    #     )
    # print("RESPONSE:", response.rowcount)

    response = conn.execute(
        text("UPDATE Phones SET price = :inPrice, weight = :inWeight WHERE ID = :inID"),
        {
            'inID': 46,
            'inPrice': 100,
            'inWeight': 206,
        }
    )
    print("RESPONSE:", response.rowcount)

