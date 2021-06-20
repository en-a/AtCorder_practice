import math
n=int(input())
x=n*1.08

x1=math.floor(x)

if 206>x1:
    print("Yay!")
elif 206==x1:
    print("so-so")
else:
    print(":(")