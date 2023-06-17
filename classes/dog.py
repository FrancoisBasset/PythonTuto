from classes.animal import Animal
from classes.identity import Identity

class Dog(Animal, Identity):
    """Dog class"""
    def __init__(self, name):
        Animal.__init__(self, "dog")
        Identity.__init__(self, name)
        self.tricks = []

    def add_trick(self, trick):
        """Add trick"""
        self.tricks.append(trick)

    def __repr__(self):
        return f"{self.name} is {Animal.__repr__(self)}, he can {' '.join(self.tricks)}"
