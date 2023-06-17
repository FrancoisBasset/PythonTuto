class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self):
        """Return 'Hello world'"""
        return "Hello world"

    def __repr__(self):
        return f"{self.i} {self.x}, {self.y}"
