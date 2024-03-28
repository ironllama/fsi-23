from sqlalchemy import create_engine, text
from random import randrange

engine = create_engine('mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23')

with engine.begin() as db:
    print("PART 1 -- OWNERS:")

    # print("\n\tAdding owner_id to 'phones'")
    # db.execute(text("ALTER TABLE phones ADD COLUMN owner_id INT AFTER owner"))

    # print("\n\tCreating table 'owners'")
    # db.execute(text("""
    #                       CREATE TABLE owners (
    #                         id INT AUTO_INCREMENT PRIMARY KEY,
    #                         lastname VARCHAR(255),
    #                         firstname VARCHAR(255),
    #                         phone_number VARCHAR(255)
    # )"""))

    # print("\n\tTransferring data from 'phones' into table 'owners':")
    # db.execute(text("INSERT INTO owners (firstname) SELECT DISTINCT(owner) FROM phones"))

    # print("\n\tUpdate table 'owners'")
    # names = {
    #     "Terry": "Bradshaw",
	#     "Brad": "Pitt",
    #     "Stacy": "PitaChips",
    #     "Richard": "Branson",
    #     "Alex": "Oh",
    #     "Roland": "Deschain",
    #     "Frank": "Thetank",
    #     "Victoria": "Secret",
    #     "Vincent": "Cassel",
    #     "Nina": "Ricci",
    #     "Brandon": "Langdon",
    #     "Nancy": "Drew"
    # }
    # res = db.execute(text("SELECT id, firstname FROM owners WHERE firstname != 'Rose'"))
    # for row in res:
    #     new_row = { 'id': row.id, 'last': names.get(row.firstname), 'phone': '010' + str(randrange(10_000_000, 99_999_999))}
    #     print("NEW:", new_row)
    #     db.execute(text("UPDATE owners SET lastname=:last, phone_number=:phone WHERE id=:id"), new_row)

    # print("\n\tUpdate table 'phones' with the proper ids")
    # db.execute(text("UPDATE phones SET owner_id=(SELECT id FROM owners WHERE owners.firstname = phones.owner)"))

    # print("\n\tDelete the owner column from phones")
    # db.execute(text("ALTER TABLE phones DROP COLUMN owner"))

    # print("\n\tAdding new owner to owners who doesn't appear in phones")
    # db.execute(text("INSERT INTO owners (firstname, lastname, phone_number) VALUES ('Rose', 'Sunday', '01039483282')"))

    # print("\n\tAdding new row to phones without owner")
    # db.execute(text("INSERT INTO phones (model, brand, price, weight, comment) VALUES ('iphone14', 'Apple', 1505, 200, 'exclusivity first on the market')"))

    # print("\n\tJOINS -- WHERE")
    # res = db.execute(text("SELECT CONCAT(firstname, ' - ', model) FROM phones, owners WHERE phones.owner_id = owners.id LIMIT 40, 20"))
    # for row in res:
    #     print(row[0])

    # print("\n\tJOINS -- JOIN")
    # res = db.execute(text("SELECT CONCAT(firstname, ' - ', model) FROM phones JOIN owners ON phones.owner_id = owners.id LIMIT 40, 20"))
    # for row in res:
    #     print(row[0])

    # print("\n\tJOINS -- LEFT JOIN")
    # # res = db.execute(text("SELECT CONCAT(firstname, ' - ', model) FROM phones LEFT JOIN owners ON phones.owner_id = owners.id LIMIT 40, 20"))
    # # for row in res:
    # #     print(row[0])
    # res = db.execute(text("SELECT firstname, model FROM phones LEFT JOIN owners ON phones.owner_id = owners.id LIMIT 40, 20"))
    # for row in res:
    #     print(f"{row[0] if row[0] else ''} - {row[1]}")

    # print("\n\tJOINS -- RIGHT JOIN")
    # # res = db.execute(text("SELECT CONCAT(COALESCE(firstname, ''), ' - ', model) FROM phones RIGHT JOIN owners ON phones.owner_id = owners.id LIMIT 40, 20"))
    # # for row in res:
    # #     print(row[0])
    # res = db.execute(text("SELECT firstname, model FROM phones RIGHT JOIN owners ON phones.owner_id = owners.id LIMIT 40, 20"))
    # for row in res:
    #     print(f"{row[0]} - {row[1] if row[1] else ''}")


    # print("PART 1 -- BRANDS:")

    # print("\n\tAdding brand_id to 'phones'")
    # db.execute(text("ALTER TABLE phones ADD COLUMN brand_id INT AFTER brand"))

    # print("\n\tCreating table 'brands'")
    # db.execute(text("""
    #                       CREATE TABLE brands (
    #                         id INT AUTO_INCREMENT PRIMARY KEY,
    #                         brand_name VARCHAR(255)
    # )"""))

    # print("\n\tTransferring data from 'phones' into table 'brands':")
    # db.execute(text("INSERT INTO brands (brand_name) SELECT DISTINCT(brand) FROM phones"))

    # print("\n\tUpdate table 'phones' with the proper ids")
    # db.execute(text("UPDATE phones SET brand_id=(SELECT id FROM brands WHERE brands.brand_name = phones.brand)"))

    # print("\n\tDelete the brand column from phones")
    # db.execute(text("ALTER TABLE phones DROP COLUMN brand"))

    # print("\n\tAdding new row to phones without brand")
    # db.execute(text("INSERT INTO phones (model, price, weight, comment) VALUES ('iphone12', 1505, 200, 'No brand')"))
    
    # print("\n\tAdding new row to brands without an existing phone")
    # db.execute(text("INSERT INTO brands (brand_name) VALUES ('Gigabyte')"))

    # print("\n\tAdding new row to phones without brand")
    # db.execute(text("INSERT INTO phones (model, price, weight, comment) VALUES ('iphone12', 1505, 200, 'No brand')"))

    print("\n\tJOINS -- WHERE")
    res = db.execute(text("SELECT CONCAT(model, ' - ', brand_name) FROM phones, brands WHERE phones.brand_id = brands.id LIMIT 40, 20"))
    for row in res:
        print(row[0])

    print("\n\tJOINS -- JOIN")
    res = db.execute(text("SELECT CONCAT(model, ' - ', brand_name) FROM phones JOIN brands ON phones.brand_id = brands.id LIMIT 40, 20"))
    for row in res:
        print(row[0])

    print("\n\tJOINS -- LEFT JOIN")
    res = db.execute(text("SELECT brand_name, model FROM phones LEFT JOIN brands ON phones.brand_id = brands.id LIMIT 40, 20"))
    for row in res:
        print(f"{row[0] if row[0] else ''} - {row[1]}")

    print("\n\tJOINS -- RIGHT JOIN")
    res = db.execute(text("SELECT brand_name, model FROM phones RIGHT JOIN brands ON phones.brand_id = brands.id LIMIT 40, 20"))
    for row in res:
        print(f"{row[0]} - {row[1] if row[1] else ''}")
