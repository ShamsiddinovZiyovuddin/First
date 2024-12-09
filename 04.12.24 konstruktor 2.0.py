# # Descriptor class
class NameDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # print("================", instance)
        # print("================", instance.__dict__)
        # print("================", owner)
        return instance.__dict__.get('name', None)

    def __set__(self, instance, value):

        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        if len(value) < 3:
            print("salom")
            raise ValueError("Name must be at least 3 characters long!")

        instance.__dict__['name'] = value

    def __delete__(self, instance):
        raise AttributeError("Name attribute cannot be deleted!")

# # Main class using the descriptor
class Person:
    name = NameDescriptor()  # Attach the descriptor to the `name` attribute

    def __init__(self, name):
        self.name = name  # Triggers the descriptor's __set__ method


person = Person("123")
person.name ="23"
print(person.name)

# # Example usage
# # try:
# #     person = Person("Ali")  # Valid name
# #     print(person.name)  # Triggers the descriptor's __get__ method
# #
# #     person.name = "Bo"  # Invalid, raises ValueError
# # except ValueError as e:
# #     print(e)
#
# # try:
# #     del person.name  # Invalid, raises AttributeError
# # except AttributeError as e:
# #     print(e)
#

