#Meta Programming 1clasning boshqa class ustida ishlashi

#  Meta Programming Nimaga Kerak?
#  Dynamic Code Generation
#  Sinf va ob'ektlarni bajarilish vaqtida o‘zgartirish imkonini beradi.
#  Masalan, ORM (Object-Relational Mapping) kabi vositalarda ma’lumotlar
#  bazasi ustunlarini Python sinflariga moslashtirish uchun ishlatiladi.
#
#  Avtomatlashtirish
#  Ko‘p marta takrorlanadigan ishlarni kod ichida avtomatik bajarish imkonini beradi.
#
#  Validatsiya va Nazorat
#  Sinflarga kiritilayotgan o‘zgarishlarni cheklash yoki maxsus qoidalarni
#  amalga oshirish uchun ishlatiladi.
#
#  DSL (Domain-Specific Languages)
#  Ma’lum sohalarga moslashtirilgan dasturlash interfeyslarini yaratish.
#
#
#  Qachon Metaprogrammalashdan Foydalanish Mumkin?
#
#  Murakkab tizimlar: Katta dasturiy ta’minotlar, masalan, web-frameworklar
#  (Django’da metaclass va dekoratorlardan foydalaniladi).
#  Avtomatik kod yozish: Kodning qayta-qayta yozilishini oldini olish.
#  Cheklovlar yoki qoidalarni amalga oshirish: Sinf yoki atributlar ustidan nazorat.


# class Field:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# class ModelMeta(type):
#     def __new__(cls, name, bases, dct):
#         fields = {k: v for k, v in dct.items() if isinstance(v, Field)}
#         dct['_fields'] = fields
#         return super().__new__(cls, name, bases, dct)
#
#
# class Model(metaclass=ModelMeta):
#     def save(self):
#         print(f"Saving: {', '.join(f'{k}={v}' for k, v in self._fields.items())}")
#
#
# class User(Model):
#     username = Field("username")
#     email = Field("email")
# user ={
#     "username":"dsjhfsidufh",
#     "eamil":"sdjfosidh"
# }
#
# # Foydalanish
# user = User()
# user.username = "johndoe"
# user.email = "johndoe@example.com"
# user.save()

# Xulosa: Python’da metaprogrammalash dasturlarni dinamik boshqarish,
# kengaytirish va avtomatlashtirish imkoniyatlarini taqdim etadi.
# Lekin murakkabligi sababli uni ehtiyotkorlik bilan qo‘llash kerak


# Python Exceptions: Nima va Qanday Ishlaydi?

# Exceptions - bu dastur ishlayotgan paytda yuzaga keladigan xatolarni
# boshqarish uchun Python’da ishlatiladigan mexanizm. Exceptions koddagi
# odatiy oqimni buzadi va xatolikni qayd etib, uni hal qilish imkonini beradi.
# Masalan, nolga bo‘lish yoki faylni ochishda xato bo‘lsa, exception ishlatiladi.

# Exception’ning Asosiy Tuzilishi

# Xato yuzaga kelishi: raise operatori yordamida yoki Python ichki xatoliklarni ko‘taradi.
# Xatoni tutib olish: try-except bloki orqali xatolikni qayd etish va muammoni hal qilish.
# Oddiy misol:
# try:
#     x = 10 / 0  # ZeroDivisionError
# except ZeroDivisionError as e:
#     print(f"Error occurred: {e}")
#
# Exception’ning Tuzilish Bloklari
# try - Kodning xato yuzaga kelishi mumkin bo‘lgan qismini belgilaydi.
# except - Xatolikni ushlaydi va unga javob beradi.
# else - Agar try ichidagi kod muvaffaqiyatli bo‘lsa, ishlaydi.
# finally - Har doim bajariladi (xatolik bo‘lishidan qat’i nazar).
#
# try:
#     number = int(input("Son kiriting: "))
#     result = 100 / number
# except ValueError:
#     print("Faqat son kiriting!")
# except ZeroDivisionError:
#     print("Nolga bo‘lish mumkin emas!")
# else:
#     print(f"Natija: {result}")
# finally:
#     print("Bu kod har doim ishlaydi.")
#
# Exception Sinflari va Hierarxiyasi
# Python’da barcha exceptions BaseException klassidan kelib chiqadi. Ko‘p ishlatiladigan sinflar:
#
# Exception: Barcha umumiy xatoliklar uchun asosiy sinf.
# ArithmeticError: Matematik xatoliklar (ZeroDivisionError, OverflowError).
# IOError: Fayl va kiritish/chiqarish xatolari.
# KeyError: Lug‘atdagi mavjud bo‘lmagan kalitga murojaat qilish.
# IndexError: Ro‘yxatdagi mavjud bo‘lmagan indeksga murojaat qilish.
#
#
# try:
#     my_dict = {"a": 1}
#     print(my_dict["b"])  # KeyError
# except KeyError as e:
#     print(f"Kalit topilmadi: {e}")
#
#
# Exceptions Nimaga Kerak?
# Xatoliklarni boshqarish: Dasturning to‘xtab qolishini oldini olish.
# Muammoni aniqlash: Xato haqida ma’lumot olish.
# Toza kod: Xatoliklarni boshqarish uchun alohida mexanizm yaratadi.
# Foydalanuvchi xatolariga moslashuvchanlik: Notog‘ri foydalanuvchi
# kiritmalari bilan ishlash.
#
#
# # Python’da xatoliklar sintaksis xatoliklari va runtime xatoliklari sifatida
# # ikkiga bo‘linadi. Quyida Python xatoliklarining asosiy turlari va ularning
# # qanday yuzaga kelishi tushuntiriladi:
#
# #  Sintaksis xatoliklari (Syntax Errors)
# # Sintaksis xatoliklari dastur yozilishida qoidalarga zid kod yozilganida yuzaga keladi.
# # Bunday xatolar dastur bajarilishidan oldin aniqlanadi.
#
# # if True
# #     print("Hello")  # Sintaksis xatosi: ":" yetishmayapti
#
# # Runtime xatoliklari (Exceptions)
# # Runtime xatoliklar dastur bajarilayotgan paytda yuzaga keladi.
# # Ular quyidagi asosiy turlarga bo‘linadi:
#
# # a. Logic Errors (Mantiqiy Xatolar)
# # Dastur mantiqida noto‘g‘ri natijaga olib keladigan xatolar.
# # Bu xatolarni Python avtomatik aniqlamaydi.
#
# def calculate_area(length, width):
#     return length + width  # Xato: Ko‘paytirish o‘rniga qo‘shish ishlatilgan
#
#
# # b. Standard Exceptions (Standart Istisnolar)
# # TypeError
# # Xato turdagi ma’lumotlar bilan ishlaganda yuzaga keladi.
#
# print("5" + 5)  # Matnni raqam bilan qo‘shib bo‘lmaydi
#
# # ValueError
# # Ma’lumot turi to‘g‘ri bo‘lsa-da, qiymat noto‘g‘ri bo‘lsa.
#
# int("hello")  # Stringni integerga aylantirib bo‘lmaydi
#
# # IndexError
# # Ro‘yxatdagi noto‘g‘ri indeksga murojaat qilinganda.
# numbers = [1, 2, 3]
# print(numbers[5])  # Ro‘yxatda bunday indeks yo‘q
#
# # KeyError
# # Lug‘atda mavjud bo‘lmagan kalitga murojaat qilinganda.
#
# my_dict = {"a": 1}
# print(my_dict["b"])  # Kalit mavjud emas
#
# # ZeroDivisionError
# # Nolga bo‘lish operatsiyasi bajarilganda.
# print(10 / 0)
#
# # AttributeError
# # Ob’ekt noto‘g‘ri atributga murojaat qilganda.
# my_list = [1, 2, 3]
# my_list.push(4)  # Ro‘yxatda `push` metodi yo‘q
#
# # IOError / FileNotFoundError
# # Fayl yoki resurs mavjud bo‘lmaganda.
#
# open("nonexistent_file.txt")
#
#
# # 3. Foydalanuvchi Yaratuvchi Xatoliklar (Custom Exceptions)
# # O‘ziga xos xatolarni aniqlash va qo‘shimcha nazorat mexanizmi yaratish uchun ishlatiladi.
# class CustomError(Exception):
#     pass
#
#
# def check_positive(number):
#     if number < 0:
#         raise CustomError("Number must be positive!")
#
#
# try:
#     check_positive(-5)
# except CustomError as e:

#     print(f"Xatolik: {e}")
#
# # https://api.example.com/unknown-resource
#
# {
#     "error": "Resource not found"
# }
# HTTP protokoli orqali ishlatiladigan xatolik kodlari (status codes) mijoz
# (frontend) va server (backend) o‘rtasida qanday muammo yuzaga kelganini
# tushuntirish uchun ishlatiladi. Bu kodlar quyidagi asosiy toifalarga bo‘linadi:

# 1xx – Informatsion Xabarlar
# Bu kodlar ma’lumot so‘rovining hali davom etayotganligini bildiradi.
#
# 100 Continue: So‘rovni davom ettirish mumkin.
# 101 Switching Protocols: Protokol o‘zgarishi amalga oshirilgan.

# 2xx – Muvaffaqiyatli Javoblar
# Bu kodlar so‘rov muvaffaqiyatli amalga oshirilganini bildiradi.
#
# 200 OK: So‘rov muvaffaqiyatli bajarildi.
# 201 Created: Resurs muvaffaqiyatli yaratilgan.
# 204 No Content: Javobda hech qanday kontent yo‘q, lekin so‘rov muvaffaqiyatli.

# 3xx – Yo‘naltirishlar
# Bu kodlar mijozni boshqa manzilga yo‘naltirish kerakligini bildiradi.
#
# 301 Moved Permanently: Resurs yangi manzilga doimiy ko‘chirilgan.
# 302 Found: Resurs vaqtinchalik boshqa manzilda joylashgan.
# 304 Not Modified: Kontent o‘zgarmagan, oldingi keshlangan versiyasidan foydalanish mumkin.

# 4xx – Mijoz Tomonidan Xatolar
# Bu kodlar mijoz tomonidan noto‘g‘ri so‘rov yuborilganini bildiradi.
#
# 400 Bad Request: Noto‘g‘ri so‘rov, server uni tushuna olmaydi.
# 401 Unauthorized: Avtorizatsiya talab qilinadi.
# 403 Forbidden: Ruxsat yo‘q, resursga kirish mumkin emas.
# 404 Not Found: So‘ralgan resurs topilmadi.
# 405 Method Not Allowed: HTTP metodi ruxsat etilmagan.
# 408 Request Timeout: Mijozning so‘rovi vaqtida bajarilmadi.
# 429 Too Many Requests: Juda ko‘p so‘rov yuborildi.

# 5xx – Server Tomonidan Xatolar
# Bu kodlar serverdagi ichki muammolar yoki noto‘g‘ri sozlamalarni bildiradi.
#
# 500 Internal Server Error: Server ichki xato tufayli so‘rovni bajara olmadi.
# 501 Not Implemented: Server so‘ralgan funksionallikni qo‘llab-quvvatlamaydi.
# 502 Bad Gateway: Oraliq serverdan noto‘g‘ri javob olindi.
# 503 Service Unavailable: Server vaqtincha mavjud emas.
# 504 Gateway Timeout: Oraliq server javob bermadi.
# 505 HTTP Version Not Supported: HTTP versiyasi qo‘llab-quvvatlanmaydi.
