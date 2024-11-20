import sqlite3

con = sqlite3.connect("people.db")
cursor = con.cursor()


sql3 = '''
SELECT * FROM people
'''

cursor.execute(sql3)

print(cursor.fetchall())

