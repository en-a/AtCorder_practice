#ナッツ
N=int(input())
Ai=list(map(int, input().split()))
 
j=0
 
for i in Ai:
    if i>=10:
        
        j+=i-10
 
print(j)