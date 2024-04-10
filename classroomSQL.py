import sqlite3
import random
import hashlib

data = sqlite3.connect('aviator.db')
sql = data.cursor()
sql.execute("""
            
            CREATE TABLE IF NOT EXISTS users(
            
            login VARCHAR(20),
            password VARCHAR(16),
            cash INT

            )
            """)
# 20 ve 16 limitleri sqlite'de tam olaraq işləmir.
data.commit()

def choice_func():

    def get_valid_log(prompt):
        while True:
                value = input(prompt)
                if len(value) > 20:
                    print("Please enter no more than 20 characters?")
                else:
                    return value
                
    def get_valid_pass(prompt):
        while True:
                value = input(prompt)
                if len(value) > 16:
                    print("Please enter no more than 16 characters?")
                else:
                    return value
                
    def get_valid_int(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print("Please enter a value greater than 0.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    choice = input("Seçim edin (1) Qeydiyyatdan keçin (2) Giriş edin (3) Oyuna başla (4) İstifadəçini bazadan silin (5) Balansı yoxla: ")
    Login = get_valid_log("bir username girin: ")
    Password = get_valid_pass("bir parol girin: ")

    def game():
        login = Login
        sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
        cash_game = sql.fetchone()[0]
        start = input("Oyuna başlamaq üçün ENTER basın! (çıxmaq üçün (Q)): ")
        if cash_game <= 0:
            print("Balansınız yeterli deyil")
        elif not start == '':
            print("çıxış edildi")
        else:
            bet = random.randint(1, 10)
            number_bytes = str(bet).encode()
            hash_object = hashlib.sha256()
            hash_object.update(number_bytes)
            hex_dig = hash_object.hexdigest()
            print("Mərcin doğruluğunu yoxlamaq üçün SHA256 hash'i mərcdən əvvəl göstərilir")
            print(f"Sayının SHA256 hash'i: {hex_dig}")
            guess = get_valid_int("Mərc üçün bir sayı gir: ")
            if guess == bet:
                print(f"Təbrik edirik, 10 azn qazandınız! düzgün say {bet} idi")
                new_cash = cash_game + 10
                sql.execute(f"UPDATE users SET cash = '{new_cash}' WHERE login = '{login}'")
                data.commit()
                print("Balansınız: ", new_cash)
                check = get_valid_int("SHA256 kodunu doğrulamaq istəyirsiz? (düzgün sayını girin): ")
                number_bytes = str(check).encode()
                hash_object = hashlib.sha256()
                hash_object.update(number_bytes)
                hex_dig = hash_object.hexdigest()
                print(f"Sayının SHA256 hash'i: {hex_dig}")
                continue_func = input("Səhifəni yeniləmək istəyirsiz? (y/n): ")
                if continue_func == 'y':
                    game()
                else:
                    print("Oyun sonlandırıldı")
            else:
                print(f"Uduzdun, 5 azn balansından çıxıldı! düzgün say {bet} idi")
                new_cash = cash_game - 5
                sql.execute(f"UPDATE users SET cash = '{new_cash}' WHERE login = '{login}'")
                data.commit()
                print("Balansınız: ", new_cash)
                check = get_valid_int("SHA256 kodunu doğrulamaq istəyirsiz? (düzgün sayını girin): ")
                number_bytes = str(check).encode()
                hash_object = hashlib.sha256()
                hash_object.update(number_bytes)
                hex_dig = hash_object.hexdigest()
                print(f"Sayının SHA256 hash'i: {hex_dig}")
                continue_func = input("Səhifəni yeniləmək istəyirsiz? (y/n): ")
                if continue_func == 'y':
                    game()
                else:
                    print("Oyun sonlandırıldı")

    def login_func():
        login = Login
        password = Password
        sql.execute("SELECT * FROM users")
        sqluser = sql.fetchall()
        user_exists1 = any(login == user[0] for user in sqluser)
        user_exists2 = any(password == user[1] for user in sqluser)
        if user_exists1 and user_exists2:
            print("Giriş uğurlu oldu")
            choice_balance = input("Balansını artırmaq istəyirsinizmi? (y/n): ")
            if choice_balance == 'y':

                def balance():
                    sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
                    user_cash = sql.fetchone()[0]
                    deposit = get_valid_int("Artılacaq məbləği daxil edin: ")
                    new_cash = user_cash + deposit
                    sql.execute(f"UPDATE users SET cash = '{new_cash}'")
                    data.commit()
                    print("Balansınız artırıldı")
                balance()

                if input("Oyun səhifəsinə giriş etmək istəyirsiz? (y/n): ") == 'y':
                    game()
                else:
                    print("Giriş edilmedi")
            else:
                sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
                user_cash = sql.fetchone()[0]
                print("Balansınız: ", user_cash)
                if input("Oyun sehifesine giriş etmək istəyirsiz? (y/n)") == 'y':
                    game()
                else:
                    print("Giriş edilmedi")
        else:
            print("login ve ya parol yanlışdır")

    def singup():
        login = Login
        password = Password
        sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
        if sql.fetchone() is not None:
            print("Bu username artiq istifadə olunub")
        else:
            sql.execute(f"INSERT INTO users(login, password, cash) VALUES ('{login}','{password}','{0}')")
            data.commit()
            print("Qeydiyyatdan keçildiniz")
            if input("Giriş etmək istəyirsinizmi? (y/n): ") == 'y':
                login_func()
            else:
                print("Giriş edilmedi")

    def user_delete():
        login = Login
        sql.execute(f"DELETE FROM users WHERE login = '{login}'")
        print("Hesabınız uğurla silindi")
        data.commit()

    choicecheck = ["1","2","3","4","5"]
    if choice not in choicecheck:
        print("Yanlış seçim")
        choice_func() # Recursion
    else:
        if choice == '1':
            singup()
        elif choice == '2':
            login_func()
        elif choice == '3':
            game()
        elif choice == '4':
            user_delete()
        elif choice == '5':
            login = Login
            sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
            cash_game = sql.fetchone()[0]
            print("Balansınız: ", cash_game)

choice_func()

# finish