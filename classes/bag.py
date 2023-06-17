class Bag:
    """Bag class"""
    def __init__(self):
        self.data = []

    def add(self, x):
        """Add element in bag"""
        self.data.append(x)

    def add_twice(self, x):
        """Add twice element in bag"""
        self.add(x)
        self.add(x)
    
    def __repr__(self):
        return f"{len(self.data)} {self.data}"
