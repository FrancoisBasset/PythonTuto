class Voiture:
    """Voiture class"""
    def __init__(self, marque, model):
        self.__id = hash(marque + model)
        self._prot = self.__ok()
        self.marque = marque
        self.model = model

    def __ok(self):
        return True

    def __repr__(self):
        return f"{self.__id}"

v1 = Voiture("Renault", "Megane")
print(v1._prot)