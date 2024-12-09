#with open("new_file","w") as file:
#    for i in range(11):
#        print()
#        file.write(f"\n {i}")

import json
import re
import os
from os import write
from unittest import expectedFailure

def add_card():

    a=input("karta qushmoqchimisiz 1 yoki 2 karta uchirmoqchimisiz :")
    if a=="1":
        karts={}
        if os.path.exists("malumot.json"):
            with open("malumot.json", "r") as file:
                karts = json.load(file)
            try:
                karts = json.load(file)
            except:
                karts={}
        while True:
            kart_number = input("karta raqam kiriting(37 bilan boshlansin , 16 ta raqam) :")
            if re.match(r"(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)", kart_number):
                karts['kart_number'] = kart_number
                break
            else:
                print("Email noto'g'ri! Iltimos, to'g'ri email formatida kiriting.")

        ism= input("ismingiz :")
        balans=input("balans :")
        karts[kart_number]={
            'ism':ism,
            'balans':balans
        }

        with open("malumot.json", 'w') as file:
            json.dump(karts, file, indent=4)
        return karts

    if a=="2":
        kart_number = input("o'chirish uchun karta raqamini kiriting : ")
        if os.path.exists("malumot.json"):
            with open("malumot.json", "r") as file:
                karts = json.load(file)
                karts.pop(kart_number)
                print(karts)
                with open("malumot.json", 'w') as file:
                    json.dump(karts, file, indent=4)

add_card()