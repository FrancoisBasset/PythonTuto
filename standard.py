"""Standard"""

import os
import glob
import sys
import math
import random
import statistics
from urllib.request import urlopen
from datetime import date
import zlib
import doctest

print(os.getcwd())
os.system("ls")
print()

#os.remove("arch")
#os.remove("debian")
#os.remove("fedora")
#os.remove("mint")
#os.remove("slackware")
#os.remove("ubuntu")
os.system("rm -rf __pycache__")

os.system("ls")

files = glob.glob("*.py", recursive=True)
print(files)

sys.stderr.write('Warning, log file not found starting a new one\n')

print(math.sqrt(64))
print(math.pow(10, 8))

distros = ["arch", "debian", "fedora", "mint", "slackware", "ubuntu"]

print(random.choice(distros))
print(random.choices(distros, k=3))
print(random.random())
print(random.randint(1, 5))
print(random.sample(range(100), 10))
print(random.randrange(6))

print(statistics.mean([10, 12, 14]))
print(statistics.median([10, 15, 8, 17, 9, 11, 8]))

with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt") as response:
    for l in response:
        print(l.decode().strip())

now = date.today()

print(now.strftime("%d et %m et %Y"))

s = b"witch which has which witches wrist watch"
cs = zlib.compress(s, 9)

print(len(s))
print(len(cs))

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

doctest.testmod()
