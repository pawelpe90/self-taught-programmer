
class PublicPrivateExample:
    def __init__(self):
        self.public = "bezpieczny"
        self._unsafe = "niebezpieczny"


    def public_method(self):
        # klient może używać tej metody
        pass


    def _unsafe_method(self):
        # ta metoda nie powinna być 
        # używana poza klasą
        pass
