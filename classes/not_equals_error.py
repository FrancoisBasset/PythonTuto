class NotEqualsError(Exception):
    def __init__(self):
        self.args = ["Numbers are equals !"]
