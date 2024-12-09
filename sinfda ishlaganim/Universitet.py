#universitet: nomi , adresi , emaili bo'lsin ; Stafniki:first name , last name , age; Studentda:Universitet , firast name ,lst name , age , guruh ;

class Universitet:

    def __init__(self,nom,adres,email):
        self.nom=nom
        self.adres =adres
        self.email =email
    def Universitet_info(self):
        return f"ismi : {self.nom} adres:{self.adres} email:{self.email} "

class Staff(Universitet):

    def __init__(self,nom,adres,email,first_name,last_name,age):
        super().__init__(nom,adres,email)
        self. first_name=first_name
        self.last_name =last_name
        self.age =age

    def Staff_info(self):
        return f"ismi : {self.nom} adres:{self.adres} email:{self.email} first_name : {self.first_name} last_name:{self.last_name} age:{self.age} "
class Student(Staff):

    def __init__(self,first_name,last_name,age,universitet,guruh):
        super().__init__(first_name,last_name,age)
        self.universitet =universitet
        self. guruh=guruh
    def Student_info(self):
        return f"first_name : {self.first_name} last_name:{self.last_name} age:{self.age} universitet:{self.universitet} guruh:{self.guruh}"

class Teacher(Staff):

    def __init__(self,first_name,last_name,age,position,subject):
        Staff.__init__(first_name, last_name, age)
        self. position=position
        self.subject =subject
    def Teacher_info(self):
        return f"first_name : {self.first_name} last_name:{self.last_name} age:{self.age} position : {self.position} subject:{self.subject} "

class Fan(Universitet):

    def __init__(self,nom,adres,email,name,universitet):
        Universitet.__init__(nom,adres,email)
        self.name =name
        self.universitet=universitet
    def Fan_info(self):
        return f"ismi : {self.nom} adres:{self.adres} email:{self.email} name : {self.name} universitet:{self.universitet} "

class Compyuter(Fan):

    def __init__(self,name,universitet,son,tizim,holati ):
        Fan.__init__(name,universitet)
        self.son =son
        self.tizim =tizim
        self.holati =holati
    def Compyuter_info(self):
        return f"name : {self.name} universitet:{self.universitet} son : {self.son} tizim:{self.tizim} holati:{self.holati}"

class Model(Fan):

    def __init__(self,name,universitet,son,tur , xolat):
        Fan.__init__(name, universitet)
        self.son =son
        self.tur =tur
        self. xolat=xolat
    def model_info(self):
        return f"name : {self.name} universitet:{self.universitet} son : {self.son} tur:{self.tur} holati:{self.xolat}"
