import re

class Student:
    def __init__(self , ism , yoshi , telegram_user_name , telefon_nomer , pochta , passport_seriya ):
        self.ism=ism
        self.yoshi=yoshi
        self.telegram_user_name=telegram_user_name
        self.telefon_nomer=telefon_nomer
        self.pochta=pochta
        self.passport_seriya=passport_seriya
#har biri uchun Getter Setter qilish

    @property
    def get_ism(self):
        return self.ism
    @get_ism.setter
    def set_ism(self , info):

        regex = r"^[a-z]{3,15}$"
        ism="Ali"
        if re.match(regex,ism ):
            self.ism=info
        # student.ism="Akbar"
        # print(student.ims)

    @property
    def get_yosh(self):
        return self.yosh
    @get_yosh.setter
    def set_yosh(self, info):
        regex = r"^[0-9]{2}?$"
        yosh = "15"
        if re.match(regex, yosh):
            self.yoshi=info
    # student.yosh=18
    # print(student.yosh)

    @property
    def get_telegram_user_name(self):
        return self.telegram_user_name

    @get_telegram_user_name
    def set_telegram_user_name(self,info):
        regex = r"^[a-z0-9_-]{3,15}$"
        telegram_ism = "Ali"
        if re.match(regex,telegram_ism ):
            self.telegram_user_name=info
# student.telegram_user_name="Ali002"
# print(student.telegram_user_name)

    @property
    def get_telefon_nomer(self):
        return self.telefon_nomer
    @get_telefon_nomer.setter
    def set_telefon_nomer(self, info):
        regex = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        telefon_nomer = "+998977180023"
        if re.match(regex, telefon_nomer):
            self.telefon_nomer=info
# student.telefon_raqam=998977180102
# print(student.telefon_raqam)
    @property
    def get_pochta(self):
        return self.pochta

    @get_pochta.setter
    def set_pochta(self, info):
        regex = r"[^\t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        pochta = "zzz@gmail.com"
        if re.match(regex, pochta):
            self.pochta = info

    # student.pochta = "Ali000@gmail.com"
    # print(student.pochta)

    @property
    def get_passport_seriya(self):
        return self.passport_seriya

    @get_passport_seriya.setter
    def set_passport_seriya(self, info):
        #passport uchun topa olmadim
        self.passport_seriya = info

    # student.passport_seriya = "AB606505"
    # print(student.passport_seriya)
student=Student("Ali" , 14 , "Ali_001" ,998991110102 , "Ali001@gmail.com" , "AB5056060 ")
