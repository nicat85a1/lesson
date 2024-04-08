import sqlite3

db = sqlite3.connect('data.db')
sql = db.cursor()
sql.execute("""
            
            ALTER TABLE data
            ADD ADLAR datatype;
            
            """)
sql.execute("INSERT INTO data(name) VALUES ('orxan')")
db.commit()
db.close()