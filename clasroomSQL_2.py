import sqlite3
import bcrypt
import re

import sqlversion2 # https://github.com/nicat85a1/lesson/blob/main/sqlversion2.py kimlik doğrulamalı version 2 (erişim izni gerekli) :)

data = sqlite3.connect('Register.db')
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
        data.commit()
        print("success")

password_confirm()

"""def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    sql.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = sql.fetchone()
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user[4]):
            print("Login successful!")
            return True
        else:
            print("Invalid password. Please try again.")
    else:
        print("Username not found. Please try again.")
    return False
login()""" # decrypt password denemesi