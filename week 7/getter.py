class Person:
    def getGender(self):
        pass


class Male(Person):
    def getGender(self):
        return "Male"



class Female(Person):
    def getGender(self):
        return "Female"

aMale = Male()
aFemale = Female()