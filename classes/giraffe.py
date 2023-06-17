from classes.animal import Animal
from classes.identity import Identity

class Giraffe(Animal, Identity):
    """Giraffe class"""
    def __init__(self, name):
        Animal.__init__(self, "giraffe")
        Identity.__init__(self, name)

    def __repr__(self):
        return f"{self.name} is {Animal.__repr__(self)}"
