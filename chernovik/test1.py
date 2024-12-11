class ABC:
    def __init__(self,name):
        self.name=name

    def info(self):
        return f"ism:{self.name}"
a=ABC("Ali")