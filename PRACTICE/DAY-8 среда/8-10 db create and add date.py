import sqlite3

con = sqlite3.connect("people.db")
cursor = con.cursor()

sql ='''
CREATE TABLE people
    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT, 
    age INTEGER)
'''

sql2 = '''
INSERT INTO people (name, age)
VALUES ('Tom', 38)
'''


cursor.execute(sql)
cursor.execute(sql2)


con.commit()