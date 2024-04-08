import sqlite3

db = sqlite3.connect("data.db")

sql = db.cursor()

sql.execute(""" CREATE TABLE IF NOT EXISTS data(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            age INTEGER,
            email VARCHAR(50)
            
        
    
        ) """)



# sql.execute("INSERT INTO data(name,age,email) VALUES('Ali',45,'test6@gmail.com')")
# db.commit()

# sql.execute("SELECT * FROM data LIMIT 3")
    
# ASC 
# DESC

# sql.execute("SELECT * FROM data ORDER BY name DESC")

# for x in sql:
#     print(x)



# sql.execute("SELECT * FROM data WHERE name = 'Orxan' ")

# for x in sql:
#     print(x)


# sql.execute("SELECT email FROM data  ")

# for x in sql:
#     print(x)


# sql.execute("DROP TABLE data")





# sql.execute("DELETE FROM data WHERE id = 2")

# db.commit()

# name = input("Sil : ")

# sql.execute(f"DELETE FROM data WHERE name = '{name}' ")

# db.commit()

# name = input("Update : ")

# sql.execute(f"UPDATE data SET name = '{name}' WHERE name = 'Fuad' ")

# db.commit()
# print("Databaza Ugurla Yenilendi")


# sql.execute(f"SELECT * FROM data WHERE name = '{name}' ")

# print(sql.fetchall())