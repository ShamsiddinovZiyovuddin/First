from os import remove


class Hotel:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
        self.rooms=[]
        self.clients=[]
    def add_client_hotel(self,client_dat:object):
        self.clients.append(client_dat)
    def info_client(self):
        for item in self.clients:
            print(f"ism : {item.name}, telefon raqami: {item.phone}, id : {item.id}")
class Clients:
    cls_client=[[],[],[]]
    def __init__(self,name,phone,id):
        self.name=name
        self.phone=phone
        self.id=id
        Clients.cls_client[0].append(name)
        Clients.cls_client[1].append(phone)
        Clients.cls_client[2].append(id)

    def del_client(self, client_id):
        self.client = [client for client in self.client if client.id != client_id]

class Rooms:
    def __init__(self,eco,biz,luk,number,live):
        self.eco=eco
        self.biz=biz
        self.luk=luk
        self.is_active=False
        self.number=number
        self.client=[]
        self.live=live
    def add_client(self,client):
        self.client.append(self.client)

    def client_data(self):
        for item in self.clients:
            print(f"ism : {item.name}, telefon raqami: {item.phone}, id : {item.id}")
    def del_client(self,client_id):
        self.client=[client for client in self.client if client.id!=client_id]

def add_client():
    name=input("name : ")
    phone=input("phone : ")
    id=input("id : ")
    client=Clients(name,phone,id)
    s=input("qaysi toifadagi xonani tanlaysiz: 1-eko 2-")

xona1=Rooms(True,False,False,101,0)
xona2=Rooms(True,False,False,102,0)
xona3=Rooms(True,False,False,103,0)
xona4=Rooms(True,False,False,104,0)
xona5=Rooms(True,False,False,105,0)
xona6=Rooms(False,True,False,201,0)
xona7=Rooms(False,True,False,202,0)
xona8=Rooms(False,True,False,203,0)
xona9=Rooms(False,True,False,204,0)
xona10=Rooms(False,True,False,205,0)
xona11=Rooms(False,False,True,301,0)
xona12=Rooms(False,False,True,302,0)
xona13=Rooms(False,False,True,303,0)
xona14=Rooms(False,False,True,304,0)
xona15=Rooms(False,False,True,305,0)
x=[xona15,xona14,xona13,xona12,xona11,xona10,xona9,xona8,xona7,xona6,xona5,xona4,xona3,xona2,xona1]

def hotel_work():
    clients_inroom=0
    hotel=Hotel("Hilton",4)
    hotel.rooms+=x
    while True:
        status=input("1. bo'sh xonalarni ko'rish, 2. aktiv xonalar, 3. Tizimdan chiqish")
        if status=="1":
            while True:
                room_status = input("1: eco 2: bus 3: luk 4.klient qushish 5.orqaga -")
                if room_status=="1":
                    for item in hotel.rooms:
                        if not item.is_active and item.eco:
                            print(f"bu ekonom xonamizning raqami : {item.number}")
                elif room_status=="2":
                    for item in hotel.rooms:
                        if not item.is_active and item.biz:
                            print(f"bu business xonamizning raqami : {item.number}")
                elif room_status=="3":
                    for item in hotel.rooms:
                        if not item.is_active and item.luk:
                            print(f"bu luks xonamizning raqami : {item.number}")
                elif room_status=="4":
                        if clients_inroom==3:
                            print("bu xonaga boshqa klient qushib bo'lmaydi")
                            break
                        else:
                            clients_inroom+=1
                            print("kliyenti ma'lumotlarini kiriting")
                            name=input("ism : ")
                            phone=input("phone : ")
                            id=input("id : ")
                            client=Clients(name,phone,id)
                            room_number=input("xonani raqamini kiriting - ")
                            for room in hotel.rooms:
                                if room.number==int(room_number):
                                    room.add_client(client)
                                    print(f"klient {room_number} raqamli xonaga qushildi")
                                    print(room.clients)
                elif room_status=="5":
                    break
        if status=="2":
            while True:
                room_status = input("1. eco 2. bus 3. luk  4.klient uchirish 5.klient qushish 6.chiqish")
                if room_status=="1":
                    for item in hotel.rooms:
                        if not item.is_active and item.eco:
                            print(f"bu ekonom xonamizning raqami : {item.number}")
                elif room_status == "2":
                    for item in hotel.rooms:
                        if not item.is_active and item.biz:
                            print(f"bu business xonamizning raqami : {item.number}")
                elif room_status == "3":
                    for item in hotel.rooms:
                        if not item.is_active and item.luk:
                            print(f"bu luks xonamizning raqami : {item.number}")
                elif room_status == "4":
                    print("kliyent malumotini yozing")
                    uchirish_id=input("Idni kiriting:")
                    if uchirish_id in client.id :

                        print("client o'chirildi")
                        break
                elif room_status=="5":
                    if clients_inroom == 3:
                        print("bu xonaga boshqa klient qushib bo'lmaydi")
                        break
                    else:
                        clients_inroom += 1
                        print("kliyenti ma'lumotlarini kiriting")
                        name = input("ism : ")
                        phone = input("phone : ")
                        id = input("id : ")
                        client = Clients(name, phone, id)
                        room_number = input("xonani raqamini kiriting - ")
                        for room in hotel.rooms:
                            if room.number == int(room_number):
                                room.add_client(client)
                                print(f"klient {room_number} raqamli xonaga qushildi")
                elif room_status == "6":
                    break
client1=Clients("Ali1", 998998887661,123)
client2=Clients("Ali2", 998998887662,124)
client3=Clients("Ali3", 998998887663,125)
client4=Clients("Ali4", 998998887664,126)
client5=Clients("Ali5", 998998887665,127)
client6=Clients("Ali1", 998998887665,128)

#uy ishi : aktiv bo'lgana xonalarni ko'rish ,toifasini kurish ,xonadan klient o'chirish(id orqali),klient qo'shish

hotel_work()