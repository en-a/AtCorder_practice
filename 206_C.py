#timeout２問だけ

import math
import collections
 
N=int(input())
l = list(map(int, input().split()))
d=[k for k, v in collections.Counter(l).items() if v > 1]
 
n=0
a=0
 
def saihen(x):
    s=[n for n in l if n!=x] #かぶりを抜いたリスト
    n=(len(l)-len(s))*len(s)
    return n
 
for i in d:
    n=saihen(i)
    a+=n
    
s=set(l)
 
for j in d:
    s.remove(j)
 
print((a+(len(l)-1)*len(s))//2)