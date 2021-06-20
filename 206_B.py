N=int(input())
j=0
l=[]

for i in range(1,10**9):
    j+=i
    l.append(j)
    if l[i-1]>=N:
        break

print(len(l))