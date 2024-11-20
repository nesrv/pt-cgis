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


sql3 = '''
SELECT * FROM people
'''

# cursor.execute(sql)
cursor.execute(sql3)

print(cursor.fetchall())

# con.commit()