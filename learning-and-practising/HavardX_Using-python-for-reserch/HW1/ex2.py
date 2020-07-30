# a
import math
print(math.pi/4)

# b
import random

random.seed(1) # Fixes the see of the random number generator.

def rand():
    rand = random.uniform(-1,1)
    return rand

rand()

# c
def distance(x, y):
    dis = math.sqrt(((x[0]-y[0])**2) + ((x[1]-y[1])**2))
    return dis

# d
def in_circle(x, origin = (0,0)):
    if len(x) != 2:
        return "x is not two-dimensional!"
    elif distance(x, origin) < 1:
        return True
    else:
        return False

# e
random.seed(1)

inside = []
points = []
R = 10000

for i in range(R):
    point = (rand(), rand())
    inside.append(in_circle(point))

print(sum(inside)/R)

# f
difference = math.pi/4 - sum(inside)/R
