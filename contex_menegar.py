









from contextlib import contextmanager

@contextmanager
def file_manager(f_name,mode):
    f=None
    try:
        if not "." or "," or "!" or "@" or "#" or "_" or "-" in f_name:
            raise NameError
        print(f"Faylf'{f_name}' ochilyapti...")
        f=open(f_name,mode)
        yield f

    finally:
        if f:
            print(print(f"Faylf'{f_name}' yopilyapti..."))
            f.close()

with file_manager('test.py','r') as file:

        f=file.read()
        print(f)
