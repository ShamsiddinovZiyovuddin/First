import os
import json
from stringprep import in_table_c4

from funksiya_json import create_data
def car_Crud():
    while True:
        cars={}
        status=input(" 1-C  \n 2-R  \n 3-redakt \n 4-malumot ko'rish :")
        if status=="1":
            if os.path.exists("mashina_salon.json"):
                try:
                    cars=create_data(None , "mashina_salon.json" , "r")
                except Exception as e:
                    print(e)
            car_number=input("raqam C = ")
            color = input("color = ")
            model = input("model = ")
            cars[car_number]={
              'color':color,
              'model':model
            }
            create_data(cars , "mashina_salon.json" , "w")
        if status=="2":
            car_number = input("o'chirish uchun raqamni kiriting : ")
            if os.path.exists("mashina_salon.json"):
                with open("mashina_salon.json", "r") as file:
                    cars = json.load(file)
                    if car_number in cars:
                        cars.pop(car_number)
                    else:
                        print("bunday raqam topilmadi , yana harakat qilib kuring")
                    print("                 malumot o'chirildi              ")
                    print(cars)
                    create_data(cars,"mashina_salon","w")
        if status == "3":
           if os.path.exists("mashina_salon.json"):
               with open("mashina_salon.json", "r") as file:
                    cars = json.load(file)
                    car_number=input(" mashina numerini kiriting :")
                    x=input(" qaysi malumotni uzgartirmoqchisiz? :")
                    data=input(" yangi malumot kiriting: ")
                    cars[car_number][x]=data
                    create_data(cars,"mashina_salon.json" , "w")
        if status=="4":
            if os.path.exists("mashina_salon.json"):
                try:
                    cars=create_data(None , "mashina_salon.json" , "r")
                    for item in cars:
                        print(f"mashina raqami{[item]}" , f"model={[cars][item]['model']}" , f"color={[cars][item]['color']}" )
                except Exception as e:
                    print(e)

car_Crud()