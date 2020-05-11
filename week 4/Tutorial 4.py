# exercises
# 1

day_number = int(input("daynumber?: "))

if day_number == 0:
    print("Sun")
elif day_number == 1:
    print("Mon")
elif day_number == 2:
    print("Tue")
elif day_number == 3:
    print("Wed")
elif day_number == 4:
    print("Thu")
elif day_number == 5:
    print("Fri")
elif day_number == 6:
    print("Sat")

# 2
day_number2 = int(input("daynumber?: "))
length_stay = int(input("Length of your stay?: "))

return_day = (length_stay % 7) + day_number

if day_number2 == 0:
    print("Sun")
elif day_number2 == 1:
    print("Mon")
elif day_number2 == 2:
    print("Tue")
elif day_number2 == 3:
    print("Wed")
elif day_number2 == 4:
    print("Thu")
elif day_number2 == 5:
    print("Fri")
elif day_number2 == 6:
    print("Sat")

# 3
# a a < b
# b a <= b
# c a <= b and day != 3
# d a <= b and day == 3

# 4
# a 3 equals 3
# b 3 unequal to 3
# c 3 greater or equal to 4
# d 3 true if 3 is not smaller than 4

# 6
numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in numbers:
    if i >= 75:
        print("First")
    if i >= 70 and i < 75:
        print("Upper Second")
    if i >= 60 and i < 70:
        print("Second")
    if i >= 50 and i < 60:
        print("Third")
    if i >= 45 and i < 50:
        print("F1 Supp")
    if i >= 40 and i < 45:
        print("F2")
    if i < 40:
        print("F3")

# 7
side1 = float(input("side1? "))
side2 = float(input("side2? "))

side3 = (side2 ** 2 + side1 ** 2) ** 0.5
print(side3)

# 8
side_1 = float(input("side1? "))
side_2 = float(input("side2? "))
side_3 = float(input("hypotenuse? "))

threshold = 0.0001
if (side_1 ** 2 - side_2 ** 2) ** 0.5 > side_3 + threshold or (side_1 ** 2 - side_2 ** 2) ** 0.5 < side_3 - threshold:
    print("false")
else:
    print("true")

# 1
for _ in range(1000):
    print("We like Python's turtles")
# 2

months = ["January", "February", "March", "April"]

for b in months:
    print("One of the months of the year is", b)

# 3
import turtle

screen = turtle.Screen()
Tess = turtle.Turtle()

Tess.left(3645)  # will spin 3645 degrees

screen.exitonclick()

# 4
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in numbers:
    print(i)
    print(i, i ** 2)

# c
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0

for i in numbers:
    total = total + i
    print(total)

# d
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in numbers:
    for j in numbers:
        product = i * j
        print(product)
# 5
import turtle

p = int(input("sides"))
screen = turtle.Screen()
casper = turtle.Turtle()

for sides in range(p):
    casper.forward(100)
    casper.right(360 / p)

screen.exitonclick()

# 6

import turtle

screen = turtle.Screen()
casper = turtle.Turtle()
angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in angles:
    casper.right(i)
    casper.forward(100)

screen.exitonclick()

# 7 dont get the question
# 8
# angle= 360/18

# 10
import turtle

screen = turtle.Screen()
casper = turtle.Turtle()

for i in range(5):
    casper.forward(100)
    casper.right(144)

screen.exitonclick()
#1
list = [160, -43, 270, -97, -43, 200, -940, 17, -86]
odd = 0
for i in list:
    if i % 2 != 0:
        odd = odd + 1
print(odd)

#2
list = [160, -43, 270, -97, -43, 200, -940, 17, -86]
sum = 0

for i in list:
    if i % 2 == 0:
        sum = sum + i
print(sum)
# 3
list = [160, -43, 270, -97, -43, 200, -940, 17, -86]
sum = 0

for i in list:
    if i % 2 != 0:
        sum = sum + i
print(sum)

#4
list = ["January", "February", "March", "April"]
wordlen5 = 0
for i in list:
    if len(i) == 5:
        wordlen5 = wordlen5 + 1
print(wordlen5)

#5
list = [160, -43, 270, -97, -43, 200, -940, 17, -86]
count = 0
skipped = False

for i in list:
    if i % 2 == 0 and not skipped:
        skipped =  True
        continue
    count = count + i
print(count)

#6
list = ["casper", "lisanne" ,"sam", "erik"]
count = 0

for i in list:
    if i == "sam":
        count = count + 1
        print(count)
        break
    count = count + 1

#7
n = float(input("of what number do you want the sqrt?:"))
approximation = float(input("what is your best guess?"))
better = (approximation + n/approximation)/2
print(better)

for i in range(6):
    better = (better + n/better)/2
    print(better)

#8
n = int(input("n"))
for n in range(n):
    T = (n)*(n + 1) / 2
    print(T)
#9
x = int(input("number:"))

if x >= 2:
    for n in range(2, x):
        if x % n == 0:
            print(False)
            break
    else:
        print(True)
else:
    print(False)

#10
import turtle
screen = turtle.Screen()
casper = turtle.Turtle()

list = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for right, forward in list:
    casper.forward(forward)
    casper.right(right)

screen.exitonclick()

#11

import turtle
screen = turtle.Screen()
casper = turtle.Turtle()


list = [(0, 100), (90, 100), (135, 141.42), (-135,100), (-90,100), (135,70.71), (90, 70.71), (90, 141.42)]
casper.speed(2)

for left, forward in list:
    casper.left(left)
    casper.forward(forward)

screen.exitonclick()

