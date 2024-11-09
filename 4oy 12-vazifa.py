import re

user_id = 0

while True:
    user_id += 1
    name = input("Ismingizni kiriting: ")
    lastname = input("Familiyangizni kiriting: ")
    age = input("Yoshingizni kiriting: ")

    while not age.isdigit():
        print("Yosh butun son bo'lishi kerak!")
        age = input("Yoshingizni kiriting: ")
    age = int(age)

    phone = input("Telefon raqamingizni kiriting (+998 xx xxx xx xx): ")
    while not re.match(r"^\+998\d{9}$", phone):
        print("Telefon raqam +998 bilan boshlanib, 9 ta raqamdan iborat bo'lishi kerak!")
        phone = input("Telefon raqamingizni kiriting (+998 xx xxx xx xx): ")

    email = input("Email manzilingizni kiriting: ")
    address = input("Yashash manzilingizni kiriting: ")

    with open("users_info.txt", "a") as file:
        file.write(f"ID: {user_id}, Name: {name}, Lastname: {lastname}, Age: {age}, Phone: {phone}, Email: {email}, Address: {address}\n")

    print("Ma'lumotlar saqlandi va faylga yozildi.")
