from classes.point import Point
from classes.color import Color

p = Point(10, 150)
print(p.x, p.y)

def find_language(word):
    match word:
        case "Oui" | "Non":
            print(word, "est français")
        case "No":
            print(word, "est anglais ou espagnol")
        case "Yes":
            print(word, "est anglais")
        case "Si":
            print(word, "est espagnol")

def find_point(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"X=0, Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}, Y=0")
        case Point(x=x, y=y):
            print(f"X={x}, Y={y}")
        case _:
            print("Not a point")

def find_color(color):
    match color:
        case Color.RED:
            print("I see red")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues")
            