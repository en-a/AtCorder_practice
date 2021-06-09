N,K=map(int,input().split())

J=0
for l in range(1,N+1):

    for i in range(1,K+1):
        m=l*100+i
        J+=m
        
print(J)    
    