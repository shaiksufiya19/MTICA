import sqlite3
carData=[
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (9, 'Ganguly', 99999),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hammer', 41400),
    (7, 'Volkswagen', 21600)
    ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)",carData)
con.commit()
con.close()
print("Values inserted.")
