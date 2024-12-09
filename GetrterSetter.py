class Car:

    def __init__(self, brand , model ):
        self.brand=brand
        self.model=model
#o'zgaruvchiday muomala qilish imkoniyatini beradi kommentdagi bilan bu birxil
    @property
    def info(self):
        return self.model

    @info.setter
    def info(self, info):
        self.model=info


    # def get_model(self):
    #     return self.model
    #
    # def set_model(self , info):
    #     self.model=info

car1=Car("BMV" , "X7")
# car1.set_model("x6")
# print(car1.get_model())
car1.info="X6"
# print(car1.info)
class Student:

    def __init__(self , yosh):
        self.yosh=yosh

    @property
    def info(self):
        return self.yosh

    @info.setter
    def info1(self , info):
        self.yosh=info

    def tekshiruv(self , info):
        self.yosh=info
        if 104>info>0:
            print("yoshingiz tug'ri")
        else:
            print("yoshingiz notug'ri ")

student=Student(15)
student.info1=18
print(student.info)
print(student.tekshiruv())