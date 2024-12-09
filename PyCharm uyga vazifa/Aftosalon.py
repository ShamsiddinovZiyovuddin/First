from random import random
import random
class Avto_salon:
    def __init__(self, name, phone_number, location, ):
        self.name = name
        self.phone_number = phone_number
        self.location = location
        self.baza = []

    @property
    def get_ism(self):
        return self.name
    @get_ism
    def set_ism(self , info):
        self.name=info

    @property
    def get_telefon_raqam(self):
        return self.phone_number

    @get_telefon_raqam
    def set_telefon_raqam(self, info):
        self.phone_number = info

    @property
    def get_lokatsiya(self):
        return self.location

    @get_lokatsiya
    def set_lokatsiya(self, info):
        self.location = info


salon1 = Avto_salon("First_salon", 998974442233, "ali", )
salon2 = Avto_salon("Salon_N1",998974442234 , "ali", )

salonlar = [salon1,salon2]
class Car:
    def __init__(self,marka, model, yili,ot_kuchi,rangi , narxi):
        self.marka=marka
        self.model=model
        self.yili=yili
        self.ot_kuchi=ot_kuchi
        self.rangi=rangi
        self.narxi=narxi

    @property
    def get_marka(self):
        return self.marka

    @get_marka
    def set_marka(self, info):
        self.marka = info

    @property
    def get_model(self):
        return self.model

    @get_model
    def set_model(self, info):
        self.model = info

    @property
    def get_yili(self):
        return self.yili

    @get_yili
    def set_yili(self, info):
        self.yili = info

    @property
    def get_ot_kuchi(self):
        return self.ot_kuchi

    @get_ot_kuchi
    def set_ot_kuchi(self, info):
        self.ot_kuchi = info

    @property
    def get_rangi(self):
        return self.rangi

    @get_rangi
    def set_rangi(self, info):
        self.rangi = info

    @property
    def get_narxi(self):
        return self.narxi

    @get_marka
    def set_narxi(self, info):
        self.narxi = info

car1=Car("BMV" , "X2" , 1956,700 , "oq",12000)
car2=Car("BMV" , "X3" , 1960,750 , "oq",13000)
car3=Car("BMV" , "X4" , 1966,800 , "oq",14000)
car4=Car("BMV" , "X5" , 1976,900 , "oq",15000)
car5=Car("BMV" , "X6" , 1977,1100 , "oq",16000)
car6=Car("BMV" , "X7" , 1987,1200 , "oq",17000)
car7=Car("BMV" , "X8" , 1990,1300 , "oq",18000)
car8=Car("BMV" , "X9" , 1994,1400 , "oq",19000)
car9=Car("BMV" , "Y1" , 1997,1500 , "oq",20000)
ca10=Car("BMV" , "Y2" , 1999,1600 , "oq",21000)