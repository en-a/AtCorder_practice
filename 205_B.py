N=int(input())
l=list(map(int,input().split()))
l.sort()

for i in range(0,N-1):
    if not(l[i]<l[i+1]):
            print("No")  
            break
    elif i==N-1:
        if l[len(l)-2]<l[len(l)-1]:
            print("Yes")

