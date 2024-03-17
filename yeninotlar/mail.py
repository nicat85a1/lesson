import smtplib

content = "Hello, how are you?"

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('nicat85a1@gmail.com', 'password')

mail.sendmail('nicat85a1@gmail.com', 'nicat85a123@gmail.com', content)