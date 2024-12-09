import re

def register():
    info = {}

    while True:
        name = input("Ismingizni kiriting (Bosh harf katta bo'lishi kerak): ")
        if re.match(r"^[A-Z][a-zA-Z]*$", name):
            info['name'] = name
            break
        else:
            print("Ism noto'g'ri! Iltimos, bosh harfi katta bo'lgan ism kiriting.")

    while True:
        phone = input("Telefon raqamingizni kiriting (+998 XXX XX XX formatida): ")
        if re.match(r"^\+?998[ -]?\d{2}[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}$", phone):
            info['phone'] = phone
            break
        else:
            print("Telefon raqami noto'g'ri! Iltimos, +998 90 123 45 67 formatida kiriting.")

    while True:
        email = input("Email manzilingizni kiriting: ")
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            info['email'] = email
            break
        else:
            print("Email noto'g'ri! Iltimos, to'g'ri email formatida kiriting.")

    return info

result = register()
print("Kiritilgan ma'lumotlar:", result)
