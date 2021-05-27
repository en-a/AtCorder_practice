r=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

1<=r<=10**5
1<=len(a)<=r
1<=len(b)<=r
1<=len(c)<=r

m=0
def comb(n):
    for i in range(1,n):   
            for j in range(1 , n):
                yield [i, j]

for d in comb(r+1):
    if a[(d[0]-1)]==b[(c[(d[1]-1)]-1)]:
        m +=1
    else:
        m

print(m)