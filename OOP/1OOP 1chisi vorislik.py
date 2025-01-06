class Person:
    def __init__(self , name,phone,email):
        self.phone=phone
        self.email = email
        self.name = name
    def info(self):
        return f"ismi : {self.name} phone:{self.phone} email:{self.email} "

class Student(Person):
#birinchi otasiniki kiyin o'ziniki
    def __init__(self, name,phone,email , id,group):
#super yoki person
        super().__init__(name,phone,email)
        self.id=id
        self.group=group

#pastda id yoki gruppa chiqarish uchun
    def info(self):
        return f"ismi : {self.name} phone:{self.phone} email:{self.email} id:{self.id} guruh:{self.group}"

class Teacher(Person):
    pass

student=Student("Ali" , 998974441122 , "jhgfegyas@guydhfb.sdfsdf" , 1342 ,59)

print(student.info())    #Personda(otasida) yozilgan metodni ishlatadi o'zida bo'lmasa

