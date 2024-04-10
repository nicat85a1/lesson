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

    choice = input("Seçim edin (1) Qeydiyyatdan keçin (2) Giriş edin (3) Oyuna başla (4) İstifadəçini bazadan silin (5) Balansı yoxla (6) login və ya parolu dəyiş (7) çıxış: ")
    if choice == '7':
        print("Çıxış edildi")
    else:
        login = get_valid_log("bir username girin: ")
        password = get_valid_pass("bir parol girin: ")

        def game(login):
            sql.execute("SELECT * FROM users")
            sqluser = sql.fetchall()
            user_exists1 = any(login == user[0] for user in sqluser)
            user_exists2 = any(password == user[1] for user in sqluser)
            if user_exists1 and user_exists2:
                sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
                cash_game = sql.fetchone()[0]
                start = input("Oyuna başlamaq üçün ENTER basın! (çıxmaq üçün (Q)): ")
                if cash_game <= 0:
                    print("Balansınız yeterli deyil")
                elif not start == '':
                    print("çıxış edildi")
                else:
                    serverbet = random.randint(1, 10)
                    userbet = random.randint(1, 10)
                    if serverbet == userbet:
                        print(f"Təbrik edirik, 10 azn qazandınız!")
                        new_cash = cash_game + 10
                        sql.execute(f"UPDATE users SET cash = '{new_cash}' WHERE login = '{login}'")
                        data.commit()
                        print("Balansınız: ", new_cash)
                        continue_func = input("Səhifəni yeniləmək istəyirsiz? (y/n): ")
                        if continue_func == 'y':
                            game(login)
                        else:
                            print("Oyun sonlandırıldı")
                    else:
                        print(f"Uduzdun, 5 azn balansından çıxıldı!")
                        new_cash = cash_game - 5
                        sql.execute(f"UPDATE users SET cash = '{new_cash}' WHERE login = '{login}'")
                        data.commit()
                        print("Balansınız: ", new_cash)
                        continue_func = input("Səhifəni yeniləmək istəyirsiz? (y/n): ")
                        if continue_func == 'y':
                            game(login)
                        else:
                            print("Oyun sonlandırıldı")
            else:
                print("login ve ya parol yanlışdır")
                choice_func()

        def login_func(login,password):
            sql.execute("SELECT * FROM users")
            sqluser = sql.fetchall()
            user_exists1 = any(login == user[0] for user in sqluser)
            user_exists2 = any(password == user[1] for user in sqluser)
            if user_exists1 and user_exists2:
                print("Giriş uğurlu oldu")
                choice_balance = input("Balansını artırmaq istəyirsinizmi? (y/n): ")
                if choice_balance == 'y':
                    sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
                    user_cash = sql.fetchone()[0]
                    deposit = get_valid_int("Artılacaq məbləği daxil edin: ")
                    new_cash = user_cash + deposit
                    sql.execute(f"UPDATE users SET cash = '{new_cash}' WHERE login = '{login}'")
                    data.commit()
                    print("Balansınız artırıldı")
                    sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
                    user_cash = sql.fetchone()[0]
                    print("Balansınız: ", user_cash)
                    if input("Oyun səhifəsinə giriş etmək istəyirsiz? (y/n): ") == 'y':
                        game(login)
                    else:
                        print("Giriş edilmedi")
                else:
                    sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
                    user_cash = sql.fetchone()[0]
                    print("Balansınız: ", user_cash)
                    if input("Oyun sehifesine giriş etmək istəyirsiz? (y/n)") == 'y':
                        game(login)
                    else:
                        print("Giriş edilmedi")
            else:
                print("login ve ya parol yanlışdır")
                choice_func()

        def singup(login,password):
            sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
            if sql.fetchone() is not None:
                print("Bu username artiq istifadə olunub")
            else:
                sql.execute(f"INSERT INTO users(login, password, cash) VALUES ('{login}','{password}','{0}')")
                data.commit()
                print("Qeydiyyatdan keçildiniz")
                if input("Giriş etmək istəyirsinizmi? (y/n): ") == 'y':
                    login_func(login,password)
                else:
                    print("Giriş edilmedi")

        def user_delete(login):
            sql.execute("SELECT * FROM users")
            sqluser = sql.fetchall()
            user_exists1 = any(login == user[0] for user in sqluser)
            user_exists2 = any(password == user[1] for user in sqluser)
            if user_exists1 and user_exists2:
                sql.execute(f"DELETE FROM users WHERE login = '{login}'")
                print("Hesabınız uğurla silindi")
                data.commit()
            else:
                print("login ve ya parol yanlışdır")

        choicecheck = ["1","2","3","4","5","6","7"]
        if choice not in choicecheck:
            print("Yanlış seçim")
            choice_func() # Recursion
        else:
            if choice == '1':
                singup(login,password)
            elif choice == '2':
                login_func(login,password)
            elif choice == '3':
                game(login)
            elif choice == '4':
                user_delete(login)
            elif choice == '5':
                sql.execute("SELECT * FROM users")
                sqluser = sql.fetchall()
                user_exists1 = any(login == user[0] for user in sqluser)
                user_exists2 = any(password == user[1] for user in sqluser)
                if user_exists1 and user_exists2:
                    sql.execute(f"SELECT cash FROM users WHERE login = '{login}'")
                    cash_game = sql.fetchone()[0]
                    print("Balansınız: ", cash_game)
                else:
                    print("login ve ya parol yanlışdır")
            elif choice == '6':
                sql.execute("SELECT * FROM users")
                sqluser = sql.fetchall()
                user_exists1 = any(login == user[0] for user in sqluser)
                user_exists2 = any(password == user[1] for user in sqluser)
                if user_exists1 and user_exists2:
                    update_user = input("Dəyişmək: (1) username (2) parol (3) hərikisi: ")
                    updatecheck = ["1","2","3"]
                    if update_user not in updatecheck:
                        print("Yanlış seçim")
                        choice_func() # Recursion
                    else:
                        if update_user == '1':
                            newLogin = get_valid_log("Yeni username daxil edin: ")
                            sql.execute(f"UPDATE users SET login = '{newLogin}' WHERE login = '{login}'")
                            data.commit()
                            print("login uğurla dəyişdirildi")
                            choice_func()
                        elif update_user == '2':
                            newPassword = get_valid_pass("Yeni parol daxil edin: ")
                            sql.execute(f"UPDATE users SET password = '{newPassword}' WHERE login = '{login}'")
                            data.commit()
                            print("şifrə uğurla dəyişdirildi")
                            choice_func()
                        elif update_user == '3':
                            newLogin = get_valid_log("Yeni username daxil edin: ")
                            newPassword = get_valid_pass("Yeni parol daxil edin: ")
                            sql.execute(f"UPDATE users SET login = '{newLogin}' WHERE login = '{login}'")
                            sql.execute(f"UPDATE users SET password = '{newPassword}' WHERE login = '{login}'")
                            data.commit()
                            print("login və şifrə uğurla dəyişdirildi")
                            choice_func()
                else:
                    print("login ve ya parol yanlışdır")
                    choice_func() 
choice_func()


# finish