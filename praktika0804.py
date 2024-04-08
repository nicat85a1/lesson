import sqlite3

data = sqlite3.connect('bank.db')
sql = data.cursor()

sql.execute("""
            
            CREATE TABLE IF NOT EXISTS users(
            
            cash INT,
            pin INT

            )
            """)

# sql.execute("INSERT INTO users(cash,pin) VALUES ('5000','6969')")
data.commit()

while input("çıxış? (y/n): ") == "n":
    pincode = int(input("pin kodunuzu daxil edin: "))
    sql.execute("SELECT * FROM users")
    sqluser = sql.fetchall()
    user_exists = any(pincode == user[1] for user in sqluser)
    if user_exists:
        print("Pin kodunuz doğru")
    else:
        print("Pin kodunuz yanlışdır")
        continue
    select = input("Seçim edin: (1)-Balansi yoxla, (2)-Kartdan Pul Cixar, (3)-Karta Medaxil et, (4)-Pini deyish, (5)-Cixish et: ")
    if select == "1":
        sql.execute(f"SELECT cash FROM users WHERE pin = {pincode}")
        user_cash = sql.fetchone()[0]
        print("Balansınız: ", user_cash, "AZN")
    elif select == "2":
        sql.execute(f"SELECT cash FROM users WHERE pin = {pincode}")
        user_cash = sql.fetchone()[0]
        cixaris = int(input("pul çıxar: "))
        if cixaris > user_cash:
            print("Yetersiz bakiye")
        else:
            new_cash = user_cash - cixaris
            sql.execute(f"UPDATE users SET cash = {new_cash} WHERE pin = {pincode}")
            data.commit()
    elif select == "3":
        sql.execute(f"SELECT cash FROM users WHERE pin = {pincode}")
        user_cash = sql.fetchone()[0]
        medaxil = int(input("pul elave et: "))
        new_cash = user_cash + medaxil
        sql.execute(f"UPDATE users SET cash = {new_cash} WHERE pin = {pincode}")
        data.commit()    
    elif select == "4":
        new_pin = int(input("yeni pin kodunuzu daxil edin: "))
        sql.execute(f"UPDATE users SET pin = {new_pin} WHERE pin = {pincode}")
        data.commit()
        print("Pin kodunuz değiştirildi")
    elif select == "5":
        print("Programdan çıxış edildi")
        break
data.close()