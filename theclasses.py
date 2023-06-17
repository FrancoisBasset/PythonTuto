from classes.my_class import MyClass
from classes.calculator import Calculator
from classes.dog import Dog
from classes.bag import Bag
from classes.animal import Animal
from classes.giraffe import Giraffe
from classes.employee import Employee
from classes.reverse import Reverse

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local :", spam)
    do_nonlocal()
    print("After nonlocal :", spam)
    do_global()
    print("After global :", spam)

scope_test()
print("In global scope :", spam, "\n")

print(MyClass)
print(MyClass.i)
print(MyClass.f)
c1 = MyClass(1, 2)

MyClass.i += 1

print(c1)
print(c1.i)
print(c1.f)
print(c1.f())

print(MyClass.f(c1))

c1.ok = 5
print(c1.ok)

c = Calculator()
print(c.add(1, 2))

dog = Dog("toutou")
dog.add_trick("assis")
dog.add_trick("debout")
dog.add_trick("couché")
print(dog)

b = Bag()
b.add_twice(5)
b.add(6)
print(b)

g = Giraffe("Sophie")
g.eat("apple")
g.eat("flower")
g.eat("banana")
print(g)

e = Employee("francois", 26, 2500)
print(e)

s = "abc"
it = iter(s)
print(it.__next__())
print(it.__next__())
print(it.__next__())

r = Reverse([1, 2, 3, 4, 5, 6])
for i in r:
    print(i)
