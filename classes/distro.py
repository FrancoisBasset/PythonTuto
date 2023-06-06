class Distro:
    def __init__(self, name: str, family: str, version: str):
        self.name = name
        self.family = family
        self.version = version

    def __repr__(self):
        return f"{self.name} {self.version} based on {self.family}"
