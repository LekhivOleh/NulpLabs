from math import *
x = 0.4
while x < 0.81:
    if x < 0.5:
        print(x, "\t", (fabs(log(x)))**7)
        x += 0.02
        x = round(x, 2)
    elif (x >= 0.5) and (x < 0.7):
        print(x, "\t", 1/tan(x+x**3))
        x += 0.02
        x = round(x, 2)
    elif x >= 0.7:
        print(x, "\t", log(sin(x), 5))
        x += 0.02
        x = round(x, 2)

print("_____________________________________")
print("_______________2 part________________")
print("_____________________________________")

x = 0.1
m = 20
answer = 1
d = 0.001

if x == 0:
    print(x, "\t", 0.00)
    x += 0.05

while x <= 0.5:
    n = 1
    temp_mult = 1
    while temp_mult >= d:
        temp_mult *= ((m + n - 1) * pow(x, n)) / factorial(n)
        answer += temp_mult
        n += 1
    print(x, "\t", answer)
    answer = 1
    x += 0.05
    x = round(x, 3)