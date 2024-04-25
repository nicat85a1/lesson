# task 1
from telethon.sync import TelegramClient
import random
import sys

def get_valid_usercode(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 100000: # if len(value) != 6:
                print("please enter the 6 digit code")
            elif value > 999999:
                print("please enter the 6 digit code")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter numbers only.")

api_id = '27698576'
api_hash = 'ef3bc9775211e0280f0ad439790391f0'
phone_number = '+15642127988'

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone_number)

print("Robot olmadığınızı doğrulayın")
print()
servercode = random.randint(100000, 999999)
kullanici_adi = input("Please enter your telegram username (excample: NMKasumov): ")
async def send_message():
    await client.send_message('https://t.me/'+kullanici_adi, 'Doğrulama Kodunuz: '+str(servercode))
with client:                
    client.loop.run_until_complete(send_message())  
luck = 3
def usercode_func(luck): 
    usercode = get_valid_usercode("Please enter the 6-digit code you received: ")
    if usercode == int(servercode):
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

# task json

"""import json

{'adult': False, 'backdrop_path': '/vcrgU0KaNj5mKUCIQSUdiQwTE9y.jpg', 'belongs_to_collection': {'id': 1241, 'name': 'Harry Potter Collection', 'poster_path': '/eVPs2Y0LyvTLZn6AP5Z6O2rtiGB.jpg', 'backdrop_path': '/4gV0rKUjB1nLUdZB4zIltLvNZZr.jpg'}, 'budget': 250000000, 'genres': [{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}], 'homepage': 'https://www.warnerbros.com/movies/harry-potter-and-deathly-hallows-part-1/', 'id': 12444, 'imdb_id': 'tt0926084', 'original_language': 'en', 'original_title': 'Harry Potter and the Deathly Hallows: Part 1', 'overview': "Harry, Ron and Hermione walk away from their last year at Hogwarts to find and destroy the remaining Horcruxes, putting an end to Voldemort's bid for immortality. But with Harry's beloved Dumbledore dead and Voldemort's unscrupulous Death Eaters on the loose, the world is more dangerous than ever.", 'popularity': 233.894, 'poster_path': '/iGoXIpQb7Pot00EEdwpwPajheZ5.jpg', 'production_companies': [{'id': 174, 'logo_path': '/IuAlhI9eVC9Z8UQWOIDdWRKSEJ.png', 'name': 'Warner Bros. Pictures', 'origin_country': 'US'}, {'id': 437, 'logo_path': '/nu20mtwbEIhUNnQ5NXVhHsNknZj.png', 'name': 'Heyday Films', 'origin_country': 'GB'}], 'production_countries': [{'iso_3166_1': 'GB', 'name': 'United Kingdom'}, {'iso_3166_1': 'US', 'name': 'United States of America'}], 'release_date': '2010-10-06', 'revenue': 954305868, 'runtime': 146, 'spoken_languages': [{'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}], 'status': 'Released', 'tagline': 'One Way… One Fate… One Hero.', 'title': 'Harry Potter and the Deathly Hallows: Part 1', 'video': False, 'vote_average': 7.774, 'vote_count': 16625}

# düzəlişlər _ ' to " _ 's to \'s _ False to false

json_str = '{"adult": false, "backdrop_path": "/vcrgU0KaNj5mKUCIQSUdiQwTE9y.jpg", "belongs_to_collection": {"id": 1241, "name": "Harry Potter Collection", "poster_path": "/eVPs2Y0LyvTLZn6AP5Z6O2rtiGB.jpg", "backdrop_path": "/4gV0rKUjB1nLUdZB4zIltLvNZZr.jpg"}, "budget": 250000000, "genres": [{"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}], "homepage": "https://www.warnerbros.com/movies/harry-potter-and-deathly-hallows-part-1/", "id": 12444, "imdb_id": "tt0926084", "original_language": "en", "original_title": "Harry Potter and the Deathly Hallows: Part 1", "overview": "Harry, Ron and Hermione walk away from their last year at Hogwarts to find and destroy the remaining Horcruxes, putting an end to Voldemort\'s bid for immortality. But with Harry\'s beloved Dumbledore dead and Voldemort\'s unscrupulous Death Eaters on the loose, the world is more dangerous than ever.", "popularity": 233.894, "poster_path": "/iGoXIpQb7Pot00EEdwpwPajheZ5.jpg", "production_companies": [{"id": 174, "logo_path": "/IuAlhI9eVC9Z8UQWOIDdWRKSEJ.png", "name": "Warner Bros. Pictures", "origin_country": "US"}, {"id": 437, "logo_path": "/nu20mtwbEIhUNnQ5NXVhHsNknZj.png", "name": "Heyday Films", "origin_country": "GB"}], "production_countries": [{"iso_3166_1": "GB", "name": "United Kingdom"}, {"iso_3166_1": "US", "name": "United States of America"}], "release_date": "2010-10-06", "revenue": 954305868, "runtime": 146, "spoken_languages": [{"english_name": "English", "iso_639_1": "en", "name": "English"}], "status": "Released", "tagline": "One Way… One Fate… One Hero.", "title": "Harry Potter and the Deathly Hallows: Part 1", "video": false, "vote_average": 7.774, "vote_count": 16625}'

my_json = json.loads(json_str)
print(my_json['imdb_id'])
print(my_json['adult'])"""


# task 2

"""import os

def get_valid_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            if len(name) > 20:
                print("Please enter no more than 20 characters?")
            else:
                return name.capitalize()
        else:
            print("Ad girin")

def one():
    name = get_valid_name("Enter your name: ")
    with open("C:/Users/user/Desktop/sql.txt", "r+") as file:
        data = file.read()
        data2 = data.split()
        say = 0
        for i in data:
            if i == " ":
                say += 1
        if name in data2:
            print("bu ad adi artiq movcuddur")
            one()
        else:
            if say < 5:
                file.write(name+" ")
                print("ad əlavə olundu")
            else:
                print("max 5 ad yazıla bilər")

def two():
    file = open("C:/Users/user/Desktop/sql.txt", "r")
    data = file.read()
    print(data)
    name = get_valid_name("Enter your name: ")
    if name in data:
        new_data = data.replace(name+" ", "")
        file = open("C:/Users/user/Desktop/sql.txt", "w")
        file.write(new_data)
        print("ad silindi")

def three():
    file = open("C:/Users/user/Desktop/sql.txt", "r")
    data = file.read()
    print(data)
    name = get_valid_name("Enter your name: ")
    change_name = get_valid_name("Enter your new name: ")
    if name in data:
        new_data = data.replace(name, change_name)
        file = open("C:/Users/user/Desktop/sql.txt", "w")
        file.write(new_data)
        print("ad redakte olundu")
    return

def four():
    if os.path.exists("C:/Users/user/Desktop/sql.txt"):
        os.remove("C:/Users/user/Desktop/sql.txt")
        print("File deleted")
    else:
        print("The file does not exist")
        return

choice = input("Yeni ad (1) Adi sil (2) Adi redakte et (3) faylı sil (4): ")

if choice == "1":
    one()
elif choice == "2":
    two()
elif choice == "3":
    three()
elif choice == "4":
    four()"""