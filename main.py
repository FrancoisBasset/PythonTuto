#!/usr/bin/env python3

from controls.filters import filter_names1, filter_names2, filter_names3
from controls.functions import *
from classes.my_empty_class import MyEmptyClass
from controls.testmatch import find_language, find_point, find_color
from classes.point import Point
from classes.color import Color
from controls.math import *

def ok():
    pass

def f(a, L=[]):
    L.append(a)
    return L

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

def foo(name, /, **kwds):
    return "name" in kwds

def bar(pos, *, kwd):
    print(pos, kwd)

def sep(a, b):
    print(a, b)

somme = lambda a, b : a + b
square = lambda a : a * a

if __name__ == "__main__":
    compare(-5)
    compare(0)
    compare(1)
    compare(2)
    loop()
    filter_names1()
    filter_names2()
    filter_names3()
    loop_range()
    print(list(my_range(10)))
    prime_number()
    even_or_not()
    ok()

    print(MyEmptyClass)
    print(MyEmptyClass())

    find_language("Oui")
    find_language("Non")
    find_language("No")
    find_language("Yes")

    find_point(Point(0, 0))
    find_point(Point(0, 5))
    find_point(Point(5, 0))
    find_point(Point(40, 70))

    find_color(Color("red"))
    find_color(Color("green"))
    find_color(Color("blue"))
    
    print(add(10, 9))
    print(diff(10, 9))
    print(fois(10, 9))
    print(divide(10, 9))

    print_char("ok", 2, "end")
    print_char("s", 5, "fin")

    print("a" in "bonjour")
    print("b" in "bonjour")
    print(5 in [1, 2, 3, 4])
    print(5 in [1, 2, 3, 4, 5])

    print(f(1))
    print(f(2))
    print(f(3))

    say(100, luminosity=30, month="December")
    say()

    params("Nico", "a", "b", "c", distro="Debian", desktop="KDE")

    standard_arg(1)
    standard_arg(arg=1)

    pos_only_arg(1)

    kwd_only_arg(arg=1)

    combined_example(1, 2, kwd_only=3)
    combined_example(1, standard=2, kwd_only=3)

    print(foo(1, name="name"))

    bar(pos=1, kwd=2)

    a = [5, 6]
    sep(*a)

    print("Somme :", somme(4, 8))
    print("Somme :", somme(5, 9))

    print("Square :", square(8))
