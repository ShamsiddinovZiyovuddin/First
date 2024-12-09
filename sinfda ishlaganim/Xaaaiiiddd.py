import re

def extract_info():
    def get_input(prompt, pattern, error_msg):
        while True:
            value = input(prompt)
            if re.match(pattern, value):
                return value
            print(error_msg)

    info = {
        'name': get_input("Ismingizni kiriting (Bosh harf katta bo'lishi kerak): ", r"^[A-Z][a-zA-Z]*$", "Ism noto'g'ri!"),
        'phone': get_input("Telefon raqamingizni kiriting (+998 XXX XX XX formatida): ", r"^\+?998[ -]?\d{2}[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}$", "Telefon raqami noto'g'ri!"),
        'email': get_input("Email manzilingizni kiriting: ", r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "Email noto'g'ri!")
    }
    return info

result = extract_info()
print("Kiritilgan ma'lumotlar:", result)