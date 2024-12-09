class Carta:
    def __init__(self, nomer, user_name, balans, phone, parol):
        self.nomer = nomer
        self.user_name = user_name
        self.balans = balans
        self.phone = phone
        self.parol = parol


class User:
    def __init__(self, user_name, phone, pasport_id):
        self.user_name = user_name
        self.phone = phone
        self.id = pasport_id
        self.karta = []


class Mehmonxona:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.balans = 0
        self.clients = []


def mehmonxona_register(mehmonxona_Hilton, klientlar):
    while True:
        status=False
        print("\n1. Mijozlar ro'yxatini ko'rish\n2. Mijoz qo'shish\n3. Mehmonxona balansini ko'rish\n4. Chiqish")
        a = int(input("Qaysi amalni bajarmoqchisiz: "))

        if a == 1:
            for i in range(len(klientlar)):
                user = klientlar[i]
                print(f"{i + 1}. Ism: {user.user_name}, Telefon_raqam: {user.phone}, Id: {user.id}")
            b = input("Mijozning Idsi orqali to'liq ma'lumotni ko'rish-1 \n boshqa raqam-chiqish: ")
            if b == "1":
                c = int(input("Klient Idsini kiriting: "))

                for user in klientlar:
                    if user.id == c:
                        print(f"Ism: {user.user_name}, Telefon: {user.phone}, ID: {user.id}")

                        break
                else:
                    print("Bunday IDga ega mijoz topilmadi.")
            else:
                print("bunday mijoz mavjud")
                break

        elif a == 2:
            ism = input("Yangi mijoz ismini kiriting: ")
            telefon = int(input("Telefon raqamini kiriting: "))
            Id = int(input("IDni kiriting: "))
            user = User(ism, telefon, Id)
            klientlar.append(user)


            kun = int(input("Nechchi kunga turmoqchisiz: "))
            umumiy_narx = kun * mehmonxona_Hilton.price

            nomer = int(input("Karta raqamini kiriting: "))
            karta = None
            for j in klientlar:
                user.karta=[card1,card2]
                for g in j.karta:
                    if g.nomer == nomer:
                        karta = g
                        break
                if karta:
                    break

            if karta:
                count=3
                while count>0:
                    count-=1
                    parol = int(input("Parolni kiriting: "))
                    if parol == karta.parol:
                        status=True

                        if karta.balans >= umumiy_narx:
                            karta.balans -= umumiy_narx
                            mehmonxona_Hilton.balans += umumiy_narx
                            mehmonxona_Hilton.clients.append(user)
                            print("To'lov amalga oshirildi.")
                            break
                        else:
                            print("Kartada mablag' yetarli emas.")
                            break
                    else:
                        print("Parol noto'g'ri.")
                else:
                    status2=True
                    print("Karta bloklandi.")
                    break

            elif a == 3:
                print(f"Mehmonxona balansi: {mehmonxona_Hilton.balans}$")

            elif a == 4:
                print("Dastur tugatildi.")
                break

            else:
                print("Bunday jarayon topilmadi.")



card1 = Carta(1234567890987654, "Ziyo", 100000, 998971112233, 1111)
card2 = Carta(1234567890987655, "Ali", 200000, 998971112234, 1112)

users=[]
mehmonxona = Mehmonxona("Alpomish", 2000)

mehmonxona_register(mehmonxona, users)

