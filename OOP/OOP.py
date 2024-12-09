# oop-oyd(o'zbekchada)
# class Student:
#
#     def __init__(self,name,phone,age):
#         self.ims= name
#         self.phone= phone
#         self.age = age
#
# student1= Student("Ali" , 997770102 , 16)
# print(student1.ims, student1.age , student1.phone)

# class Car:
#
#     def __init__(self,model,yili,raqami,ot_kuchi):
#         self.model= model
#         self.yili= yili
#         self.raqami = raqami
#         self.ot_kuchi=ot_kuchi
# Car1=Car("Bugutata",1999 , 123 , 700)
# print(Car1.model , Car1.yili , Car1.raqami , Car1.ot_kuchi )

# class Student:
#
#     def __init__(self,name,phone,age):
#         self.ims= name
#         self.phone= phone
#         self.age = age
#
# student1= Student("Ali" , 997770102 , 16)
# student2= Student("Ali" , 997770102 , 15)
# student3= Student("Ali" , 997770102 , 12)
# student4= Student("Ali" , 997770102 , 19)
# student5= Student("Ali" , 997770102 , 14)
# students=[student1 , student2 , student3 , student4 ,  student5 ]
# for item in students:
#     if item.age >15:
#         print(item.age , item.ims)

# class Car:
#
#     def __init__(self,model,yili,raqami,ot_kuchi):
#         self.model= model
#         self.yili= yili
#         self.raqami = raqami
#         self.ot_kuchi=ot_kuchi
# Car1=Car("Bugutata",2999 , 1234 , 740)
# Car2=Car("Bugutata",2999 , 123 , 740)
# Car3=Car("Bugutata",1999 , 123 , 704)
# Car4=Car("Bugutata",2999 , 1233 , 700)
# Car5=Car("Bugutata",1999 , 1223 , 720)
# Cars=[Car1 , Car2 , Car3 , Car4 , Car5]
# for item in Cars:
#     if item.yili>2000:
#         print(Car1.model , Car1.yili , Car1.raqami , Car1.ot_kuchi )

class Card:

    def __init__(self, nomer , muddat , egasi_ismi , parol , balans):
        self.nomer=nomer
        self.muddat=muddat
        self.egasi_ismi=egasi_ismi
        self.parol=parol
        self.balans=balans

    def __str__(self):
        return "Carta malumotlar Card classning objekti"

    def info(self):
        return f"raqam= {self.nomer } , muddati= {self.muddat} , egasi_ismi= {self.egasi_ismi} , parol= {self.parol} , balans= {self.balans}"

Card1=Card(6264563890928555 , 1810 , "Ali" , 1112 , 100000)
Card3=Card(3283567890523756 , 2311 , "Bakir" , 1311 , 200000)
Card4=Card(1732562490133459 , 2613 , "Saman" , 1411 , 300000)
Card5=Card(6264563890928555 , 1210 , "Diyor" , 1511 , 400000)
Card6=Card(3283567890523756 , 1611 , "Eumaloq" , 6111 , 500000)
Card7=Card(1732562490133459 , 1313 , "Faryod" , 1711 , 600000)
Card8=Card(6264563890928555 , 1740 , "Gofur" , 1181 , 700000)
Card9=Card(3283567890523756 , 3001 , "Bakir" , 1191 , 800000)
Card10=Card(1732562490133459 , 1113 , "SAmandar" , 9111 , 900000)
print(Card1.info())
