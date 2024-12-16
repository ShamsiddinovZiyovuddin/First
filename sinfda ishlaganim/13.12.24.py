# def f():
#     count=0
#
#     def f1():
#         nonlocal count
#         count+=1
#         return count
#     return f1
# f2=f()
# print(f2())
# print(f2())
# print(f2())
# import json
# from collections import namedtuple
#
# with open("13.12.24.json", "r") as file:
#     humans = json.load(file)
# Person=namedtuple('Person',['ism','familiya','phone',])
# a=
# b=
# c=
# human=Person(ism=a,familiya=b,phone=c)
#
# print(human.ism)
# print(human.familiya)
# print(human.phone)
# from GetrterSetter import student


# def person(func):
#     def person_name():
#         print("=========================")
#         func()
#         print("=========================")
#     return person_name()
# @person
# def manager_name():
#     print("bu Ziyovuddinning xonasi")
#
# def adding(func):
#
#     def add(*args,**kwargs):
#         print("funksiya ishladi")
#         result=func(*args,**kwargs)
#         print(f"Natija : {result}")
#         return result
#     return add
#
# def add_func(a):
#     s=0
#     for i in range(a):
#         s+=i
#     return s
#
# print(add_func(8))