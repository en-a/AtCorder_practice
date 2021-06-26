#参考にした
a,b,c,d=map(int,input().split())

a1=a
c1=0
j=0

for _ in range(10**7):
    a1+=b
    c1+=c
    j+=1
    if c1*d>=a1:
        print(j) #試行
        break
else:
    print(-1)
    exit()
