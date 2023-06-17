"""employee module"""

from dataclasses import dataclass

@dataclass
class Employee:
    """Employee class"""
    name: str
    age: int
    salary: float

    def __repr__(self):
        return f"{self.name}, {self.age} ans, {self.salary} €"