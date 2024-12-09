class Cards:
    def __init__(self, number, password, user, data):
        self.number = number
        self.password = password
        self.user = user
        self.data = data
        self.phone = None

    def __str__(self):
        return "card classining objecti"

    def info(self):
        return f"card number = {self.number} user = {self.user} "


card1 = Cards(9860122345567889, 1234, "ali", 1000000)
card2 = Cards(9860122345567881, 1234, "al1", 1000000)
card3 = Cards(9860122345567882, 1234, "al2", 1000000)
card4 = Cards(9860122345567883, 1234, "al3", 1000000)
card5 = Cards(9860122345567884, 1234, "al4", 1000000)

cards = [card5, card1, card4, card2, card3]


def bankamad():
    status = False
    status3 = False
    card = None
    while True:
        number = int(input("karta raqamni kiriting = "))
        for i in cards:
            # print(type(i.number), "============================")
            if number == int(i.number):
                count = 3
                while count > 0:
                    count -= 1
                    password = int(input("password = "))
                    if i.password == password:
                        status = True
                        card = i
                        break
                    else:
                        print("password xato")
                else:
                    status3 = True
                    print("karta bloklandi")
                    break
        if status == False and status3==False:
            print("bunday karta topilmadi")
        if status or status3:
            break
    if status == True:
        while True:
            status2 = input("1.balansni ko'rosh 2. password edit 3.pull yichish 4. to'ldirish 5. chiqish")
            if status2 == "4":
                miqdor = int(input("pul kiriting = "))
                card.data += miqdor
                print("jarayon yakunlandi ")
            elif status2 == "1":
                print(f"joriy balans = {card.data}")
                print("jarayon yakunlandi ")
            elif status2 == "5":
                print("sizga rahmat ")
                break


bankamad()
