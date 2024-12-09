#jadval qilishga harakat qil sikl bilan
#malumot(ism,familiya , telefon raqam,email,guruhi) qushish , uchirish , jadval chiqarish
import json
import os
def info_student():
    while True:
        info_students={}
        a=input("malumot qushmoqchi bulsangiz 1 uchirmoqchi bulsangiz 2 , malumot kurmoqchi bulsangiz 3ni kiriting , chiqish uchun 0 : ")
        if a=="1":
            if os.path.exists("studentlar.json"):
                with open("studentlar.json", "r") as file:
                 try:
                    info_students = json.load(file)
                 except:
                     pass

            Ism = input("ismingizni kiriting :")
            familiya = input("familiyangizni kiriting :")
            yosh = input("yoshingiz nechchida? :")
            telefon_raqam = input("telefon raqamingizni kiriting :")
            email = input("elektron adresingizni kiriting :")
            guruh = input("guruhingizni kiriting : ")

            info_students[Ism] = {
                'Ismi':Ism,
                'familiyasi': familiya,
                'yoshi': yosh,
                'telefon_raqami': telefon_raqam,
                'emaili': email,
                'guruhi': guruh
            }

            with open("studentlar.json", 'w') as file:
                json.dump(info_students, file, indent=4)

        elif a == "2":
            Ism = input("o'chirish uchun ismingizni kiriting : ")
            if os.path.exists("studentlar.json"):
                with open("studentlar.json", "r") as file:
                    info_students = json.load(file)
                    if Ism in info_students :
                        info_students.pop(Ism)
                    else:
                        print("bunday oquvchi topilmadi , yana harakat qilib kuring")
                    print("                 malumot o'chirildi              ")
                    print(info_students)
                    with open("studentlar.json", 'w') as file:
                        json.dump(info_students, file, indent=4)
        elif a == "3":
            if os.path.exists("studentlar.json.json"):
                with open("studentlar.json.json", 'r') as file:
                    info_students = json.load(file)
                    print(info_students)
                    print(file)
        else:
            break

info_student()