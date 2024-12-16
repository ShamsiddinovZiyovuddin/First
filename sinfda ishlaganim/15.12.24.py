import time

"""1-misol: Oldingi mavzu"""
# start = 0
# stop = 0
# def time_decorator(func):
#     def before_and_after(*args):
#         global start, stop
#         print("Najot ta'lim o'quvchilari funksiyasi")
#         result = func(*args)
#         print("Bu Natijasi")
#         return result
#     return before_and_after
#
# @time_decorator
# def daraja(a):
#     s = 0
#     for i in range(len(a)):
#         if a[i].isdigit():
#             s += 1
#     print(s)
#
# daraja("10**(80-70)")

"""2-misol: WHILE yordamida ITERATSIYA yaratish"""
# a = {1,9,2,8,3,7,4,6,5}
# a_iter = iter(a)
# s = 0
#
# while True:
#     try:
#         x = next(a_iter)
#         if x % 2 == 0:
#             s += x * x
#     except StopIteration:
#         break
#
# print(s)

"""3-misol: OOPda ITERATOR yaratish"""
# class Counter:
#     def __init__(self,low,high):
#         self.current = high + 1
#         self.low = low - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current -= 1
#
#         if self.current > self.low:
#             return self.current
#         raise StopIteration
#
# for i in Counter(1,20):
#     print(i)

# """4-misol: GENERATOR or YIELD"""
# def try_generator(a,b):
#     for i in range(a+1,b+1):
#         yield i-1 + i
#
# start = 10
# stop = 20
# result = try_generator(start,stop)
# for i in range(stop-start):
#     print(next(result))

"""4-misol: ANONIMUS usul"""
# my_generator = (i for i in range(0,50,4))
# while True:
#     try:
#         print(next(my_generator))
#     except StopIteration:
#         break
