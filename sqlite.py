import sqlite3

data = sqlite3.connect('example.db')
sql = data.cursor()
sql.execute("""
            
            CREATE TABLE IF NOT EXISTS data(
            name VARCHAR(50),
            age INT,
            height INT,
            weight INT,
            deneme VARCHAR(50)
            )
            
            """)
sql.execute("INSERT INTO data(name) VALUES ('orxan')")
data.commit()

"""sql.execute("SELECT * FROM data")

for i in sql.fetchall():
    print(i)"""

data.close()