import sqlite3

db = sqlite3.connect('data.db')
sql = db.cursor()
sql.execute("""
            
            UPDATE data SET name = 'alixan' WHERE rowid = 1;
            
            """)
sql.execute("INSERT INTO data(name) VALUES ('orxan')")
db.commit()
db.close()