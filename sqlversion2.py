from telethon.sync import TelegramClient
import sqlite3
import bcrypt
import random
import sys
import re

data = sqlite3.connect('RegisterV2.db')
sql = data.cursor()
sql.execute("""
            
            CREATE TABLE IF NOT EXISTS users(
            
            username VARCHAR(20),
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            email VARCHAR(30),
            password VARCHAR(100)

            )
            """)
data.commit()

api_id = '27698576'
api_hash = 'ef3bc9775211e0280f0ad439790391f0'
phone_number = '+15642127988'

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone_number)

def get_valid_usercode(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1000:
                print("please enter the 4 digit code")
            elif value > 9999:
                print("please enter the 4 digit code")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def get_valid_password(prompt):
    while True:
        password = input(prompt)
        if len(password) < 8:
            print("Please enter at least 8 characters")
        elif len(password) > 100:
            print("Please enter no more than 100 characters")
        else:
            return password

def get_valid_username(prompt):
    while True:
        value = input(prompt)
        if len(value) > 20:
            print("Please enter no more than 20 characters?")
        else:
            return value

def get_valid_email(prompt):
    while True:
        value = input(prompt)
        #sql.execute(f"SELECT email FROM users WHERE email = '{value}'") 
        sql.execute("SELECT email FROM users WHERE email = ?", (value,)) # SQL injection fix (string to tuple)
        if sql.fetchone() is not None:
            print("This email is now available") 
        else:
            pattern = r'^[A-Za-z0-9]{1,20}+@[A-Za-z0-9]{1,20}+\.[A-Z|a-z]{2,3}$'
            if not re.match(pattern, value):
                print("Please enter a valid email address") # 20 @ 20 . 3
            else:
                return value
        
def get_valid_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            if len(name) > 20:
                print("Please enter no more than 20 characters?")
            else:
                return name.capitalize()
        else:
            print("Please use letters only.")

username_input = get_valid_username("Please enter username: ")
first_name_input = get_valid_name("Please enter First name: ")
last_name_input = get_valid_name("Please enter Last name: ")
email_input = get_valid_email("Please enter email: ")

def password_confirm():
    password_input = get_valid_password("Enter Password: ")
    password_confirm_input = input("ReEnter Password : ")
    if password_input != password_confirm_input:
        print("Passwords are not compatible")
        return password_confirm()
    else:
        raw_password = password_input.encode('utf-8')
        hashed_password = bcrypt.hashpw(raw_password, bcrypt.gensalt())
        sql_query = """

                        INSERT INTO users(username, first_name, last_name, email, password)
                        VALUES (?, ?, ?, ?, ?)

                        """
        sql.execute(sql_query, (username_input, first_name_input, last_name_input, email_input, hashed_password)) # SQL injection fix
        #sql.execute(f"INSERT INTO users(username,first_name,last_name,email,password) VALUES ('{username_input}','{first_name_input}','{last_name_input}','{email_input}','{hashed_password}')")
        print("Robot olmadığınızı doğrulayın")
        print()
        servercode = random.randint(1000, 9999)
        kullanici_adi = input("Please enter your telegram username (excample: NMKasumov): ")
        async def send_message():
            await client.send_message('https://t.me/'+kullanici_adi, 'Doğrulama Kodunuz: '+str(servercode))
        with client:                
            client.loop.run_until_complete(send_message())  
        luck = 3
        def usercode_func(luck): 
            usercode = get_valid_usercode("Please enter the 4-digit code you received: ")
            if usercode == int(servercode):
                data.commit()
                print("success")
            else:
                print("Kod yanlışdır")
                luck -= 1
                if luck == 0:
                    print("şansınız bitti")
                    sys.exit()
                print(f"{luck} hakkınız kaldı")
                usercode_func(luck)
        usercode_func(luck)

password_confirm()