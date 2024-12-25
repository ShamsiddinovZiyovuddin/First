class MyContextManager:
    def __enter__(self):
        print("Context ichiga kirdik")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Contextdan chiqyapmiz")
        if exc_type:
            print(f"Xatolik: {exc_value}")
        return True

with MyContextManager() as cm:
  print("Context manager ishlamoqda")
  raise ValueError("Xatoooooooooo")