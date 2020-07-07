
class Orange():
    def __init__(self, w, c):
        """waga jest podawana w gramach"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Utworzono!")

    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(6, "pomarańczowy")
print(orange.mold)
orange.rot(10, 29)
print(orange.mold)
