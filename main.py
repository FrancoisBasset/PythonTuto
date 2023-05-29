#!/usr/bin/env python3

from controls.filters import filter_names1, filter_names2, filter_names3
from controls.functions import compare, loop, loop_range, my_range, prime_number, even_or_not
from controls.MyEmptyClass import MyEmptyClass

def ok():
    pass

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
