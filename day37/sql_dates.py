from sqlalchemy import create_engine, text

engine = create_engine('mariadb+mariadbconnector://root:@127.0.0.1:3306/fsi-23')

with engine.begin() as db:
    print("\nQ1:")
    # res = db.execute(text("SELECT username, message, created_date FROM chatmessages WHERE DATE(created_date)=CURDATE()"))
    res = db.execute(text("SELECT username, message, created_date FROM chatmessages WHERE created_date >= CURDATE()"))
    print("CREATED_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.username}\t{row.message}")
    
    print("\nQ2:")
    res = db.execute(text("SELECT username, message, created_date FROM chatmessages WHERE TIME(created_date) = '15:27:36'"))
    print("CREATED_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.username}\t{row.message}")

    print("\nQ3:")
    res = db.execute(text("SELECT username, message, created_date FROM chatmessages WHERE HOUR(created_date) BETWEEN 12 AND 14"))
    print("CREATED_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.username}\t{row.message}")

    print("\nQ4:")
    res = db.execute(
        text("INSERT INTO chatmessages (username, message, created_date) VALUES (:user, :mess, :date)"),
        [
            { 'user': 'Jessica', 'mess': 'Who let the dogs out?', 'date': '2024-03-24 16:23:12' },
            { 'user': 'Kevin', 'mess': 'Woot, woot, woot!', 'date': '2024-03-24 16:23:34' },
            { 'user': 'Jessica', 'mess': 'lol', 'date': '2024-03-24 16:24:01' },
        ]
    )

    print("\nQ5:")
    res = db.execute(text("SELECT username, message, created_date FROM chatmessages WHERE '2024-03-24' <= created_date AND created_date < '2024-03-25'"))
    print("CREATED_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.username}\t{row.message}")

    print("\nQ6:")
    res = db.execute(text("SELECT username, message, created_date FROM chatmessages WHERE DATE(created_date) = (CURDATE() - INTERVAL 2 DAY) AND TIME(created_date) = '15:27:36'"))
    print("CREATED_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.username}\t{row.message}")

    print("\nQ7:")
    res = db.execute(text("SELECT username, message, CONCAT(DAY(created_date), '/', MONTH(created_date), '/', YEAR(created_date)) as created_date FROM chatmessages LIMIT 20"))
    print("CREATED_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.username}\t{row.message}")

    print("\nQ8:")
    res = db.execute(text("SELECT username, message, DATE_FORMAT(created_date, '%d/%m/%Y') AS created_date FROM chatmessages LIMIT 15"))
    print("CREATED_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.username}\t{row.message}")

    print("\nQ8:")
    res = db.execute(text("ALTER TABLE chatmessages ADD COLUMN expire_date DATETIME"))
    res = db.execute(text("UPDATE chatmessages SET expire_date=(created_date + INTERVAL 2 MONTH)"))
    res = db.execute(text("SELECT username, message, created_date, expire_date FROM chatmessages LIMIT 10"))
    print("CREATED_DATE\t\tEXPIRE_DATE\t\tOWNER\tMESSAGE")
    for row in res:
        print(f"{row.created_date}\t{row.expire_date}\t{row.username}\t{row.message}")
