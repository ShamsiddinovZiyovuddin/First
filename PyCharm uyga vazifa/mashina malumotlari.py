import json
import os


def add_car():
    while True:
        cars={}
        a= input("mashina qushish uchun 1 yoki uchirish uchun 2 , malumotlarni kurish uchun 3 , 0ni chiqish uchun kiriting  :")
        if a=="1":
            if os.path.exists("malumot1.json"):
              with open("malumot1.json", "r") as file:
                    cars = json.load(file)

            cars_number = input("mashina davlat raqamini kiriting :")
            nom= input("mashina nomi :")
            yil=input("yili :")
            rang=input("mashinangiz rangini kiriting :")
            cars[cars_number]={
                'nom':nom,
                'yil':yil,
                'rang':rang
            }

            with open("malumot1.json", 'w') as file:
                json.dump(cars, file, indent=4)
        elif a=="2":
            car= input("o'chirish uchun davlat raqamini kiriting : ")
            if os.path.exists("malumot1.json"):
              with open("malumot1.json", "r") as file:
                    cars = json.load(file)
                    if car in cars.keys:
                        cars.pop(car)
                    else:
                        print("bunday raqam topilmadi , yana harakat qilib kuring")
                    print("                 malumot o'chirildi              ")
                    print(cars)
                    with open("malumot1.json", 'w') as file:
                        json.dump(cars, file, indent=4)

        elif a == "3":
            if os.path.exists("malumot1.json"):
                with open("malumot1.json", 'r') as file:
                    cars = json.load(file)
                    print(cars)
        else:
            break


add_car()