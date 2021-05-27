s=input()

s_1=s.translate(str.maketrans({"6":"9","9":"6"}))

s_2= ''.join(list(reversed(s_1)))

print(s_2)

#反対にするやつ
