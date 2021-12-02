import math

def frange(x,y,z):
    yield x
    while x+z < y:
        x = round(x+z,10)
        yield x

for x in frange(1, 5, 0.5):
    print(x)
