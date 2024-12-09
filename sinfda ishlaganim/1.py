from calendar import month


class BMW:
    def __init__(self, model , brand , yil):
        self.model=model
        self.brand=brand
        self.yil=yil
    def info(self):
        return f"modeli : {self.model} brandi:{self.brand} yili:{self.yil} "

class Mercedens(BMW):
    def __init__(self, model , brand , yil , rangi):
        super().__init__( model , brand , yil)
        self.rangi=rangi
    def info(self):
        return f"modeli : {self.model} brandi:{self.brand} yili:{self.yil} rangi:{self.rangi} "


class Chevrolet(BMW):
    def __init__(self, model , brand , yil , ot_kuchi ):
        super().__init__( model , brand , yil)
        self.ot_kuchi=ot_kuchi
    def info(self):
        return f"modeli : {self.model} brandi:{self.brand} yili:{self.yil} ot kuchi:{self.ot_kuchi} "
