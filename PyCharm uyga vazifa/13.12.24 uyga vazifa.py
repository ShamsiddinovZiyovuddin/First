import time

def ishlash_vaqti(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Funksiya {execution_time:.1f} sekundda bajarildi.")
        return result
    return wrapper

# Misol uchun foydalanish:
@ishlash_vaqti
def misol_funksiya():
    for _ in range(1000000):
        pass

misol_funksiya()

def fibonacci(n):
    """n-chi Fibonacci sonini qaytaradi"""
    if n <= 0:
        return "Iltimos, musbat butun son kiriting."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
