#Stop iteration sonlar tugasa chiqadi (hato)!!!
# 1.Iterator va generator
# Python'da iterator va generator ma'lumotlarni ketma-ket olish uchun mo'ljallangan
# mexanizmlar bo'lib, ular katta hajmdagi ma'lumotlarni
# samarali ishlatishga yordam beradi. Quyida ularning ta'rifi va
# ishlatilish maqsadi haqida tushuncha beriladi:

# python da Sequence va Iterable ning farqi:
# s = {4,1,6}
# Iterable: Elementlar ketma-ket olinadigan har qanday obyekt
# (masalan, set, dict, yoki generator).
# Sequence: Tartiblangan va indeks orqali murojaat qilinadigan
# iterable (masalan, list, tuple, yoki str).
# print(s)  # → {1,4,6}

## Iterator nima?

# **Iteratorlar** - iterable ustidagi iteratsiyani boshqaradigan obyektlar.
# Iterator iterable dagi joriy elementni va keyingi elementni doim bilib turadi.

# Iterable dan iterator yaratish uchun uni iter() funksiyasiga solamiz:
# 1- m
# a = [1, 2, 4]
# a_iter = iter(a)
# print(a_iter)
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))

# print(type(a_iter))
# print(type(a_iter))
# #
# s = 0
# try:
#     s += next(a_iter)
#     s += next(a_iter)
#     s += next(a_iter)
#     s += next(a_iter)
# except StopIteration:
#     print(s)
#     print("tugadi")
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
# for item in a_iter:
#     print(item)
# # 2- m
# d = [34,5,6,7,5]
# d_iter = iter(d)
#
# while True:
#     try:
#         print(next(d_iter))
#     except StopIteration:
#         break

# 2.Fayl obyekti iteratormi?
# f = open('test2.py')
# print(next(f))
# print(next(f))

# Iteratorni OOP da qurish:
# class Counter:
#     def __init__(self, low, high):
#         self.current = low - 1
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#
#         if self.current < self.high:
#             return self.current
#         raise StopIteration
# class Counter:
#     def __init__(self, start, stop):
#         self.start = start + 1
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start -= 1
#
#         if self.start > self.stop:
#             return self.start
#         raise StopIteration
#
#
# #
# #
#
# for elem in Counter(10, -10):
#     print(elem)
# print(type(Counter(1, 10)))


# Generator -iterator qaytaruvchi funksiya bo’lib, iterator
# yaratishning oson yo’li hisoblanadi.
# 1-m
def try_generator(y):
    n = y
    n += 1
    print("bajarildi")
    yield n

    n *= 2
    print("bajarildi 2")
    yield n

    n += 10
    print("bajarildi 3")
    yield n


result = try_generator(3)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(result)

# for item in result:
#     print(item)


# generator va for sikli:
# def for_gen(start, stop):
#     for i in range(start, stop):
#         yield i
# # #
# result = for_gen(1, 5)
# # #
# print(result)
# #
# for item in result:
#     print(item)
# def gen_for(a, b):
#     s = 0
#     for i in range(a, b, -1):
#         s += i
#         yield s
# r = gen_for(10,5)
# for item in r:
#     print(item)
# # Anonim generator yaratish
# my_list_com =  [num for num in range(1000)]
# print(my_list_com)

# my_generator = (num for num in range(10))
# print(my_generator)
# for i in my_generator:
#     print(i)


# class Counter:
#     def __init__(self, start, stop):
#         self.start = start - 1
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start < self.stop:
#             return self.start
#         raise StopIteration
#
#
# a = Counter(1, 10)
# for item in a:
#     print(item)
