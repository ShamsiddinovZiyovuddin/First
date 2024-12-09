# class Student:
#     total_ages=0
#     def __init__(self,ism,familiya,age):
#         self.ism=ism
#         self.familiya=familiya
#         self.age=age
#         Student.Students_age+=age
#     @classmethod
#
#     # class ichidagi narsalarni ishlatsa bo'ladi
#
#     def Students_age(cls):
#         return f"total_ages : {cls.Students_age()}"
#
# class Car:
#     total_cars = 0
#
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_cars += 1
#
#     @classmethod
#     def get_total_cars(cls):
#         return f"Total cars: {cls.total_cars , cls.get_total_cars()}"
#
# #diskrunktor
#     def __del__(self):
#         del car2
# # Foydalanish
# car1 = Car("Toyota", "Camry")
# car2 = Car("Honda", "Civic")
# print(Car.get_total_cars())  # Total cars: 2
# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
#     @staticmethod
#     def summ(a:list):
#         return sum(a)
#
# class MathUtils2:
#     @staticmethod
#     def minus_abs(a, b):
#         return abs(a - b)
#
#     @staticmethod
#     def summ(a: list):
#         return sum(a)
#
# # Foydalanish
# print(MathUtils.add(5, 10))  # 15
# print(MathUtils.summ([1,2,3,7,7,8,8]))

# class Cars:
#
#     def __init__(self, name , model , rangi , ot_kuchi):
#         self.name=name
#         self.model=model
#         self.rangi=rangi
#         self.ot_kuchi=ot_kuchi
#
#     def info(self):
#         return f"Mashina nomi:{self.name} , modeli:{self.model} , {self.rangi} rangli , ot kuchi:{self.ot_kuchi}"
#
# car=Cars("Audi", "6" , "oq" , "850")
# print(car.info())
class Cars:
    def __init__(self, name , model , rangi , ot_kuchi , narxi):
        self.name=name
        self.model=model
        self.rangi=rangi
        self.ot_kuchi=ot_kuchi
        self.narxi=narxi
    # @classmethod
    # def urtacha(cls ): xato
    #     x=0
    #     for i in cars:
    #         x+=i.narxi
    #         return f"umumiy narx = {cls.urtacha()}"
car1=Cars("Audi", "6" , "oq" , "850", 12000)
car2=Cars("Audi", "7" , "oq" , "950" , 15000)
car3=Cars("Audi", "8" , "oq" , "1150" , 20000)
cars=[car1,car2,car3]
print(Cars.urtacha())



