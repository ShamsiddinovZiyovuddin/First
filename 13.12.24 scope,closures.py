#Global-global
# decorator - funksiyani argument sifatida olib, uning o’zgartirilgan
# nusxasini qaytaruvchi funksiya.  Decorator bevosita funksiyani
# o’zgartirmasdan, undan oldin va keyin ishlaydigan kodlar qo’shish
# imkonini beradi.


def my_decorator(func):
    def wrapper():
        print("Funktsiyadan oldin ishlayapti")
        func()
        print("Funktsiyadan keyin ishlayapti")

    return wrapper


# @my_decorator
# def say_hello():
#     print("Salom, dunyo!")
#
#
# say_hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(2)
def greet(name):
    print(f"Salom, {name}!")


# greet("Ali")


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Funksiya chaqirildi: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Natija: {result}")
        return result

    return wrapper


@log_decorator
def add(a, b):
    return a + b
#
#
add(3, 5)
