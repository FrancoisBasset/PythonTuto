def compare(x):
    #x = int(input("Please enter an integer : "))

    if x < 0:
        print(x, "Negative changed to zero")
        x = 0
    elif x == 0:
        print(x, "Zero")
    elif x == 1:
        print(x, "Single")
    else:
        print(x, "More")

def loop():
    words = ["cat", "window", "swim"]
    for w in words:
        print(w, len(w))

def loop_range():
    for i in range(5):
        print(i, end=" ")

    print()

    print("-".join([str(i) for i in range(5)]))

    a = ["Mary", "has", "a", "little", "lamb"]
    for i, word in enumerate(a):
        print(i, word)

    print(sum(my_range(100)))

def my_range(length):
    i = 0

    while i < length:
        yield i
        i += 1

def prime_number():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')

def even_or_not() :
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue

        print("Found an odd number", num)

def print_char(c: str, n: int = 1, end: str = ""):
    """Print char n times"""
    print(f"{c * n}{end}")

def say(volume: int=50, luminosity: int=20, battery: int=10, month: str="January"):
    print("Volume {}\nLuminosity {}\nBattery {}\nMonth {}\n".format(volume, luminosity, battery, month))

def params(name, *ps1, **ps2):
    """print"""
    print(name)
    print(ps1)
    print(ps2)
