class Texnikalar:
    def __init__(self,brend,model,type):
        self.brend=brend
        self.model =model
        self.type =type
    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type} "
class PK(Texnikalar):
    def __init__(self,brend,model, type, video_card, ram, display):
        Texnikalar.__init__(brend,model,type)
        self.video_card=video_card
        self.ram =ram
        self.display =display
    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type}  videokarta : {self.video_card} ram:{self.ram} display:{self.display} "
class TV(Texnikalar):
    def __init__(self,brend,model,type,size, display):
        Texnikalar.__init__(brend,model,type)
        self.size = size
        self.display = display

    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type}  razmer : {self.size} display:{self.display} "
class Phone(Texnikalar):
    def __init__(self,brend,model,type, size, sim_count):
        Texnikalar.__init__(brend,model,type)
        self.size =size
        self.sim_count =sim_count

    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type}  size: {self.size} sim_count:{self.sim_count} "



class Texnika:
    def __init__(self, brend, model, type):
        self.brend = brend
        self.model = model
        self.type = type

    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type} "
class Cars(Texnika):
    def __init__(self, brend, model, type,battery_life, chargin_time):
       Texnika.__init__(brend, model, type)
       self.battery_life=battery_life
       self.chargin_time=chargin_time
    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type} battery_life : {self.battery_life} chargin_time:{self.chargin_time} "
class Moto(Texnika):
    def __init__(self, brend, model, type,motor, color):
       Texnika.__init__(brend, model, type)
       self.motor=motor
       self.color=color
    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type} motor : {self.motor} color:{self.color} "
class Fura(Texnika):
    def __init__(self, brend, model, type,motor, height, long, wieght):
       Texnika.__init__(brend, model, type)
       self.motor=motor
       self.height=height
       self.long = long
       self.wieght = wieght
    def Texnikalar_info(self):
        return f"brendi : {self.brend} modeli:{self.model} turi:{self.type} motor : {self.motor} height:{self.height} long : {self.long} wieght:{self.wieght} "




#1
# class A1:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def A1(self):
#         return f"a : {self.a} b:{self.b} c:{self.c} "
# class B1(A1):
#     def __init__(self,a,b,c,d,e):
#         A1.__init__(a,b,c)
#         self.d=d
#         self.e=e
#     def B1(self):
#         return f"d : {self.d} e:{self.e}"
# #2
# class A2:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def A2(self):
#         return f"a : {self.a} b:{self.b} c:{self.c} "
# class B2(A2):
#     def __init__(self,a,b,c,d,e):
#         A2.__init__(a,b,c)
#         self.d=d
#         self.e=e
#     def B2(self):
#         return f"d : {self.d} e:{self.e} "
# class C1(A2):
#     def __init__(self,a,b,c,f,g):
#         A2.__init__(a,b,c)
#         self.f=f
#         self.g=g
#
#     def C1(self):
#         return f"f : {self.a} g:{self.b} "
# #3
# class A3:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def A3(self):
#         return f"a : {self.a} b:{self.b} c:{self.c} "
# class B3:
#     def __init__(self,f,g,h):
#         self.f=f
#         self.g=g
#         self.h=h
#     def B3(self):
#         return f"f : {self.f} g:{self.g} h:{self.h} "
# class C2(A3,B3):
#     def __init__(self,a,b,c,f,g,h,d,e):
#         A3.__init__(self,a,b,c)
#         B3.__init__(self,f,g,h)
#         self.d=d
#         self.e=e
#     def C2(self):
#         return f"d : {self.d} e:{self.e} "
# #4
# class A4:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def A4(self):
#         return f"a : {self.a} b:{self.b} c:{self.c} "
# class B4(A4):
#     def __init__(self,a,b,c,f,g,h):
#         A4.__init__(a,b,c)
#         self.f=f
#         self.g=g
#         self.h=h
#     def B4(self):
#         return f"f : {self.f} g:{self.g} h:{self.h} "
# class C3(B4):
#     def __init__(self,f,g,h,d,e):
#         B4.__init__(f,g,h)
#         self.d=d
#         self.e=e
#     def C3(self):
#         return f"d : {self.d} e:{self.e} "
#



# class A1:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def A1(self):
#         return f"a : {self.a} b:{self.b} c:{self.c} "
# class B1(A1):
#     def __init__(self,a,b,c,d,e):
#         A1.__init__(a,b,c)
#         self.d=d
#         self.e=e
#     def A1(self):
#         return f"d : {self.d} e:{self.e}"
#
# class A2:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def A2(self):
#         return f"a : {self.a} b:{self.b} c:{self.c} "
# class B2(A2):
#     def __init__(self,a,b,c,d,e):
#         A2.__init__(a,b,c)
#         self.d=d
#         self.e=e
#     def A2(self,number):
#         return f"d : {self.d} e:{self.e} Raqam : {number}"

# item=C2(1,2,3,4,5,6,7,8)
# print(item.e)
