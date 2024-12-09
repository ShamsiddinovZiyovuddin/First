#malumot va metodni bir birlikda ifodalash (o'zgartiraolmaslik)
#3x modefayr public,protacted,prime

class School:
    def __init__(self,title,classes):
        self.title=title
        self._classes=classes
        self.__students=999

    def info(self):
        return f"title:{self.title} classes:{self._classes} students:{self.__students}"

class Rooms(School):
    def __init__(self,title,classes,students,floor):
        School.__init__(self,title,classes)
        self.floor=floor
    def info(self):
        return f"title:{self.title} classes:{self._classes} students:{self.__students} floor:{self.floor}"

school=School("a4",45)
room=Rooms("a4",45,654,3)
room.info()