l=list(map(int, input().split()))
 
if l[0]==l[1]:
    print(l[0])
elif 0 in l and 1 in l:
    print(2)
elif 2 in l and 1 in l:
    print(0)
elif 2 in l and 0 in l:
    print(1)  