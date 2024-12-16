from collections import UserDict

from class_Goods import goods
from class_Shop import supermarkets
from class_User import User
from project.class_Goods import good1
from project.class_User import user1


def Shop():
    while True:
        print("No  Mahsulot nomi  Narxi (so'm)  Muddati")
        for i in range(1, len(goods)):
            print(f"{i}".ljust(3), f"{goods[i].name}".ljust(14), f"{goods[i].cost}".ljust(13),
                  f"{(goods[i]).date[0]}.{goods[i].date[1]}.{goods[i].date[2]}")

        status=input("qaysi mahsulotni sotib olmoqchisiz:")
        if status=="1":
            status2=input("qancha sotib olasiz:")
            narx=status2*good1.cost
            user.karzinka+=f"{status2}ta {good1}"
        elif status=="2":
