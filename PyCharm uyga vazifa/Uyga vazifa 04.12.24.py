#o'tkan mavzu boycha getter setter qilish har biri uchun
class Student:
   def __init__(self,name,phone,email,user_name,pasport_seriya):
       self.name=name
       self.phone =phone
       self.email=email
       self.user_name =user_name
       self.pasport_seriya=pasport_seriya

class Name_Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('name', None)
    def __set__(self, instance, value):
        instance.__dict__['name'] = value

class Person:
    name = Name_Descriptor()

    def __init__(self, name):
        self.name = name

class Phone_Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('phone', None)

    def __set__(self, instance, value):
        instance.__dict__['phone'] = value

class Person_phone:
    phone = Phone_Descriptor()

    def __init__(self, phone):
        self.phone = phone

class Email_Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('email', None)

    def __set__(self, instance, value):
        instance.__dict__['email'] = value

class Person_email:
    email = Email_Descriptor()

    def __init__(self, email):
        self.email = email


class User_name_Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('user_name', None)

    def __set__(self, instance, value):
        instance.__dict__['user_name'] = value

class Person_User_name:
    user_name = User_name_Descriptor()

    def __init__(self, user_name):
        self.user_name = user_name


class Pasport_seriya_Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('pasport_seriya', None)

    def __set__(self, instance, value):
        instance.__dict__['pasport_seriya'] = value

class Person_Pasport_seriya:
    pasport_seriya = Pasport_seriya_Descriptor()

    def __init__(self, pasport_seriya):
        self.pasport_seriya = pasport_seriya
