from Team_Projekt.class_Goods import goods
from Team_Projekt.class_User import users
from project.class_Goods import good1


def Shop():
    while True:
        client_phone = input("Kliyentning telefon raqami : ")
        for client in users:
            if int(client_phone) == client.phone:
                new_client = client

        print("No  Mahsulot nomi  Narxi (so'm)  Muddati")
        for i in range(1, len(goods)):
            print(f"{i}".ljust(3), f"{goods[i].name}".ljust(14), f"{goods[i].cost}".ljust(13),
                  f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}")

        status=input("qaysi mahsulotni sotib olmoqchisiz:")
        if status=="1":
            status2=input("qancha sotib olasiz:")
            narx=status2*good1.cost
            new_client.karzinka+=f"{status2}ta {good1}"
        elif status=="2":
