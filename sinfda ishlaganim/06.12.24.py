class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class NameDeskriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('name',None)

    def __set__(self, instance, value):

        instance.__dict__['name']=value

class IdDeskriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get('id',None)

    def __set__(self, instance, value):
        instance.__dict__['id'] = value

class Person:
    name=NameDeskriptor()
    id=IdDeskriptor()

    def __init__(self,name,id):
        self.name=name
        self.id=id

person=Person("Ali",123454)
# person.name=
# person.id=
print(f"ism{person.name} id:{person.id}")


try:
    del person.name  # Invalid, raises AttributeError
except AttributeError as e:
    print(e)