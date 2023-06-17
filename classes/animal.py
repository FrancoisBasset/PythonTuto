class Animal:
    """Animal class"""
    def __init__(self, specie: str):
        self.specie = specie
        self.aliments = []

    def eat(self, aliment):
        """Eat aliment"""
        self.aliments.append(aliment)

    def __repr__(self):
        return "{} {}, he ate {}".format(
            "an " if self.specie[0] in "aeiou" else "a ",
            self.specie,
            ", ".join(self.aliments) if len(self.aliments) > 0 else "nothing"
        )