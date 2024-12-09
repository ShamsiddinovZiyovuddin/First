# 1. References (Havolalar)
# Python’da o‘zgaruvchilar obyektlarga havola qiladi (reference).
# Bu degani, o‘zgaruvchilar o‘zlari qiymatni to‘g‘ridan-to‘g‘ri saqlamaydi,
# balki qiymat saqlangan xotira joyiga havola qiladi.

# a = [1, 2, 3]  # 'a' ro'yxat obyektiga havola qiladi
# b = a  # 'b' ham xuddi shu obyektga havola qiladi
#
# b.append(4)  # 'b' orqali o'zgartirish asl obyektni o'zgartiradi
# print(a)  # [1, 2, 3, 4]

# a va b bir xil obyektga havola qilmoqda. Bu sababli, birida
# o‘zgarish kiritish boshqasida ham aks etadi.

# Havolalarni tushunish mutable va immutable obyektlarni o‘zgartirishda muhim.

# 1. Mutable obyektlar
# O‘zgaruvchan obyektlar bo‘lib, ularning qiymatini joyida (in-place) o‘zgartirish mumkin.
# Bu obyektlarga xotirada bir xil manzil saqlangan holda o‘zgarish kiritiladi.
# Asosan, ro‘yxatlar (lists), lug‘atlar (dictionaries), va to‘plamlar (sets)
# o‘zgaruvchan obyektlardir.


# Ro'yxat - mutable obyekt
# my_list = [1, 2, 3]
# print(my_list)  # [1, 2, 3]
#
# my_list[0] = 10  # Elementni o'zgartirish
# print(my_list)  # [10, 2, 3]
#
# Xotira manzili o'zgarmaydi
# print(id(my_list))  # Masalan: 139987839662080

# Xususiyatlar:
# Obyektning qiymatini joyida o‘zgartirish mumkin.
# Agar boshqa o‘zgaruvchi bir xil obyektga havola qilsa, ikki o‘zgaruvchi
# ham o‘zgarishlarni ko‘radi.

# a = [1, 2, 3]
# b = a  # 'b' ham xuddi shu obyektga havola qiladi
# b.append(4)
# print(a)  # [1, 2, 3, 4] - 'a' ham o'zgardi

# 2. Immutable obyektlar
# O‘zgarmas obyektlar bo‘lib, ularning qiymatini o‘zgartirib bo‘lmaydi.
# Agar o‘zgartirishga urinsangiz, Python yangi obyekt yaratadi va o‘zgaruvchini
# yangi obyektga havola qiladi.
# Asosan, raqamlar (int, float), matnlar (strings), va tuzilmalar (tuples)
# o‘zgarmas obyektlardir.

# String - immutable obyekt
# my_str = "hello"
# print(my_str)  # hello
#
# my_str = my_str + " world"  # Yangi obyekt yaratildi
# print(my_str)  # hello world
#
# # Xotira manzili o'zgaradi
# print(id(my_str))  # Yangi manzil masalan: 139987839663296

# Xususiyatlar:
# Obyektni o‘zgartirishning o‘zi mumkin emas, lekin o‘zgaruvchiga yangi
# qiymat berib, yangi obyektga havola qilish mumkin.
# Bu obyektlar havolalar orqali bo‘lishilgan bo‘lsa ham, bitta o‘zgaruvchidagi
# o‘zgarish boshqasiga ta’sir qilmaydi.

# a = "hello"
# b = a  # 'b' ham xuddi shu obyektga havola qiladi
# b = b + " world"  # Yangi obyekt yaratildi
# print(a)  # hello - 'a' o'zgarmaydi
# print(b)  # hello world

# 5. Nega bu tushuncha muhim?
# Havolalar bilan ishlashda: Mutable obyektlarning qiymati o‘zgartirilsa,
# barcha havolalar ta’sir ko‘radi.
# Performance (Ishlash tezligi): Immutable obyektlar o‘zgartirilmaydiganligi sababli,
# xotira boshqaruvi osonlashadi va ular ko‘proq xavfsiz hisoblanadi.

# Xato yuzaga kelish ehtimoli: Mutable obyektlar bilan ishlashda kutilmagan o‘zgarishlar
# yuzaga kelishi mumkin, shuning uchun ular bilan ehtiyotkorlik talab etiladi.


# 2. Dynamic Typing (Dinamik tiplashtirish)
# Python dinamik tipga ega dasturlash tili. Bu shuni anglatadiki:

# O‘zgaruvchilarni e’lon qilishda ularning tipini ko‘rsatish shart emas.
# O‘zgaruvchining tipi uning qiymatiga qarab avtomatik aniqlanadi.
# Tipni istalgan vaqtda o‘zgartirish mumkin.

# x = 10  # 'x' int tipidagi obyektni havola qiladi
# x = "Python"  # Endi 'x' str tipidagi obyektga havola qiladi


# 3. Garbage Collection (Axlatni yig‘ish)
# Python garbage collector (axlat yig‘uvchi) tizimiga ega, bu xotira boshqaruvini
# avtomatik ravishda amalga oshiradi. U foydalanilmayotgan obyektlarni aniqlab,
# ularning xotirasini bo‘shatadi.

# Python’da garbage collection reference counting va cycle detection mexanizmlariga
# asoslanadi:
# Obyektga havola qiluvchi o‘zgaruvchilar soni 0 ga tushsa, obyekt xotiradan o‘chiriladi.
# Agar obyektlar o‘zaro bog‘langan bo‘lsa (cycle), garbage collector
# ularni ham aniqlab tozalaydi.

# import gc
#
# gc.collect()  # Garbage collectionni majburiy chaqirish
#
# n = None




# Metaklasslar nima?
# Metaklass – bu sinfni yaratish jarayonini boshqaruvchi sinf.
# Odatda, Python’da barcha oddiy sinflar type orqali yaratiladi.
# Shunday qilib, type Python’da standart metaklass hisoblanadi.

# Boshqacha qilib aytganda, metaklasslar – bu "sinf yaratadigan sinf".
# Agar oddiy sinf obyektlarni yaratish uchun ishlatilsa, metaklass sinflarni
# yaratish uchun ishlatiladi.

# Nega metaklasslar kerak?
# Metaklasslar odatda quyidagi maqsadlarda ishlatiladi:

# Sinflarni avtomatik ravishda o‘zgartirish yoki tekshirish:
# Sinf yaratilayotgan paytda uning atributlarini o‘zgartirish yoki tekshirish.
# Masalan, ma'lum bir qoidaga muvofiq barcha atributlarning nomlarini avtomatik o'zgartirish.
# Sinflarga qo'shimcha funksionallik qo‘shish:
# Sinfning barcha metodlariga biror narsa qo‘shish yoki atributlar
# bilan ishlashni avtomatlashtirish.
# Kengaytiriladigan frameworklar yaratish:
# Django, SQLAlchemy kabi kutubxonalar metaklasslardan foydalangan
# holda murakkab ma'lumot tuzilmalarini yaratadi.


# Metaklasslar qanday ishlaydi?
# Python’da har bir sinf aslida obyekt hisoblanadi, va u ham biror sinf tomonidan yaratiladi.
# Shu sinfni yaratadigan sinf metaklass hisoblanadi.

# class MyMeta(type):
#     def __new__(cls, name, bases, dct):
#         print(f"Sinf yaratilyapti: {name}")
#         return super().__new__(cls, name, bases, dct)
#
# type metaklassdan meros olingan.
# __new__ – bu sinfni yaratish jarayonini boshqaradi.
# class MyClass(metaclass=MyMeta):
#     pass

# Python MyClassni yaratishni boshlaydi.
# MyMeta.__new__ metodi ishga tushadi va sinf yaratish jarayoniga ta'sir qiladi.

# Metaklassning asosiy metodlari
# __new__(cls, name, bases, dct):

# Sinfni yaratishdan oldin chaqiriladi.
# Parametrlari:
# cls: Metaklassning o'zi.
# name: Yaratilayotgan sinfning nomi.
# bases: sinfning ota sinflari (inheritance)..
# dct: Yaratilayotgan sinfning atributlari lug‘ati.
# __init__(cls, name, bases, dct):

# Sinf yaratilgandan keyin chaqiriladi.
# Yaratilgan sinfni sozlash uchun ishlatiladi.



# Amaliy misollar
# 1. Sinfni yaratishda atributlarni tekshirish
# Metaklass yordamida sinf atributlarini tekshirishingiz mumkin:


# class AttributeValidationMeta(type):
#     def __new__(cls, name, bases, dct):
#         if 'required_attribute' not in dct:
#             raise TypeError(f"{name} sinfida 'required_attribute' mavjud emas!")
#         return super().__new__(cls, name, bases, dct)
#
# To'g'ri foydalanish
# class MyValidClass(metaclass=AttributeValidationMeta):
#     required_attribute = "Something"
#
# Noto'g'ri foydalanish
# class MyInvalidClass(metaclass=AttributeValidationMeta):
#     pass  # Bu xato beradi!
#
#
# 2. Sinf atributlarini avtomatik o‘zgartirish
# Metaklass sinfning atributlarini yaratish vaqtida o‘zgartirishi mumkin:
# class UpperCaseAttributesMeta(type):
#     def __new__(cls, name, bases, dct):
#         uppercase_attrs = {
#             k.upper(): v for k, v in dct.items() if not k.startswith("__")
#         }
#         return super().__new__(cls, name, bases, uppercase_attrs)
#
# class MyClass(metaclass=UpperCaseAttributesMeta):
#     name = "John"
#     age = 30
#
# print(dir(MyClass))
# ['AGE', 'NAME', ...]

# Metaklasslardan ehtiyot bo‘lib foydalanish
# Metaklasslar kuchli vosita bo‘lsa-da, ular:

# Kod murakkabligini oshirishi mumkin – sodda echimlar mavjud bo'lsa, metaklass ishlatmaslik yaxshiroq.
# Dasturchilar uchun tushunish qiyin bo‘lishi mumkin – metaklasslarni noto'g'ri
# ishlatish kodni murakkablashtiradi.


# Agar siz frameworklar yoki murakkab tizimlar yaratishni rejalashtirsangiz,
# metaklasslar juda foydali bo'lishi mumkin. Ammo, oddiy loyihalarda
# ulardan kamroq foydalanish tavsiya etiladi.


