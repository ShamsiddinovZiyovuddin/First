#readdan tashqari boshqa funksiyalarini ishlatib ko'rish
#masalan(append)


from contextlib import contextmanager

@contextmanager
def file_manager(f_name,mode):
    f=None
    try:
        print(f"Faylf'{f_name}' ochilyapti...")
        f=open(f_name,mode)
        yield f

    finally:
        if f:
            print(print(f"Faylf'{f_name}' yopilyapti..."))
            f.close()

with file_manager('test.py','w') as file:
        file.write("a=14")
        #f=file.read
        #print(f)