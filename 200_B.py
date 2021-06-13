#200倍の数値
N, M = map(int, input().split())
l = []
l.append(N)

for i in range(M):
    
    if l[i] % 200 == 0:
        l.append(int(l[i]/200))
    else:
        l.append(l[i]*1000+200)

print(l[M])