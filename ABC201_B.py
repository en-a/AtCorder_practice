#2番名高い山
import numpy as np

N = int(input())
l = []
for i in range(N):
    a,b=input().split()
    l.append([a, int(b)])

m=[l[j][1] for j in range(N)]
m.sort(reverse=True)

#インデックス番号取得
for x, y in enumerate(l):
    try:
        pos = (x,y.index(int(m[1]))) #xがインデックス、yが要素.今回は[~,~]
        print(l[pos[0]][0]) 
        break
    except ValueError:
        pass
  