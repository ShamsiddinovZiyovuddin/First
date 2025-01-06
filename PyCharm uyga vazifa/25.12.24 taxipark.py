from random import random, randint


#5ta marshrut yaratib ko'rsatamiz

class Taxi_park:
    def __init__(self,title,mashinalar):
        self.title=title
        self.balans=0
        self.mashinalar=mashinalar
        self.safarlar=[]

class Car:
    def __init__(self,name,nomer,toifa):
        self.name=name
        self.nomer=nomer
        self.balans=0
        self.toifa=toifa


class Client:
    def __init__(self,phone_number,cards):
        self.cards=cards
        self.phone_number=phone_number

class Card:
    def __init__(self,nomer,muddat,parol,owner_name):
        self.nomer=nomer
        self.muddat=muddat
        self.parol=parol
        self.owner_name=owner_name


class Safarlar:
    def __init__(self,client_phone,mashina_number,place_A,place_B):
        self.client_phone=client_phone
        self.mashina_number=mashina_number
        self.place_A=place_A
        self.place_B=place_B


card1=Card(9860111122223333,1111,1224,"Jasur")
card2=Card(9860111122223333,1111,1224,"Ali")
card3=Card(9860111122223333,1111,1224,"Sanjar")
card4=Card(9860111122223333,1111,1224,"Yusuf")
card5=Card(9860111122223333,1111,1224,"Bekzod")
card6=Card(9860111122223333,1111,1224,"Baxodir")
card7=Card(9860111122223333,1111,1224,"Samandar")
card8=Card(9860111122223333,1111,1224,"Humoyun")
card9=Card(9860111122223333,1111,1224,"Ali2")
card10=Card(9860111122223333,1111,1224,"Ali3")



client_1=Client(998991112233,[card1,card2])
client_2=Client(998991112234,[card3,card4])
client_3=Client(998991112235,[card5,card6])
client_4=Client(998991112236,[card7,card8])
client_5=Client(998991112237,[card9,card10])

clients=[client_1,client_5,client_4,client_2,client_3]

taxi1=Car("Ali4",998971112234,"oddiy")
taxi2=Car("Ali5",998971112235,"oddiy")
taxi3=Car("Ali6",998971112236,"oddiy")
taxi4=Car("Ali7",998971112237,"oddiy")
taxi5=Car("Ali8",998971112238,"oddiy")
taxi6=Car("Ali9",998971122233,"vip")
taxi7=Car("Ali10",998971122232,"vip")
taxi8=Car("Ali11",998971122233,"vip")
taxi9=Car("Ali12",998971122234,"vip")
taxi10=Car("Ali13",998971122235,"vip")
taxi11=Car("Ali14",998971132233,"bizness")
taxi12=Car("Ali15",998971132234,"bizness")
taxi13=Car("Ali16",998971132235,"bizness")
taxi14=Car("Ali17",998971132236,"bizness")
taxi15=Car("Ali18",998971132237,"bizness")

taxi_park=Taxi_park("Taxisee",[taxi1,taxi2,taxi3,taxi4,taxi5,taxi6,taxi7,taxi8,taxi9,taxi10,taxi11,taxi12,taxi13,taxi14,taxi15])

if __name__=="__main__":
    while True:
        status=int(input("(client)telefon raqamingizni kiriting :"))
        for i in clients:
            if status==i.phone_number:
                place_A=input("Chiqish joyi")
                place_B=input("Borish joyi")
                S=randint(300,1000)
                print(f"plase_Bgacha{S}km")
                status3=input("toifani tanlang(oddiy,vip,bizness):")


                taxi_park.safarlar.append(status)
                taxi_park.safarlar.append(place_A)
                taxi_park.safarlar.append(place_B)
                taxi_park.safarlar.append(S)
                taxi_park.safarlar.append(status3)


                taxi_number=randint(1,5)
                if status3=="oddiy":
                    if taxi_number==1:
                        taxi=taxi1
                        print("100.000sum bo'ldi")
                        price = 100.000
                        park_price=price/4
                        taxi_park.balans+=park_price
                        taxi1.balans+=price-park_price

                    elif taxi_number == 2:
                        taxi = taxi2
                        print("100.000sum bo'ldi")
                        price = 100.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 3:
                        taxi = taxi3
                        print("100.000sum bo'ldi")
                        price = 100.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 4:
                        taxi = taxi4
                        print("100.000sum bo'ldi")
                        price = 100.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    else:
                        taxi = taxi5
                        print("100.000sum bo'ldi")
                        price = 100.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price



                elif status3 == "vip":
                    if taxi_number==1:
                        taxi=taxi6
                        print("200.000sum bo'ldi")
                        price = 200.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 2:
                        taxi = taxi7
                        print("200.000sum bo'ldi")
                        price = 200.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 3:
                        taxi = taxi8
                        print("200.000sum bo'ldi")
                        price = 200.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 4:
                        taxi = taxi9
                        print("200.000sum bo'ldi")
                        price = 200.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    else:
                        taxi = taxi10
                        print("200.000sum bo'ldi")
                        price=200.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                elif status3=="bizness":
                    if taxi_number==1:
                        taxi=taxi11
                        print("400.000sum bo'ldi")
                        price=400.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 2:
                        taxi = taxi12
                        print("400.000sum bo'ldi")
                        price = 400.000
                        taxi12.balans += 400.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 3:
                        taxi = taxi13
                        print("400.000sum bo'ldi")
                        price = 400.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    elif taxi_number == 4:
                        taxi = taxi14
                        print("400.000sum bo'ldi")
                        price = 400.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price

                    else:
                        taxi = taxi15
                        print("400.000sum bo'ldi")
                        price = 400.000
                        park_price = price / 4
                        taxi_park.balans += park_price
                        taxi1.balans += price - park_price





