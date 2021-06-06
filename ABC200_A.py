a=int(input())
if 1<=a<=100:
    print("1")
    
elif 101<=a<=999:
    s = str(a)
    if s[-1]=="0":
        print(s[-3])
    else:
        print(int(s[-3])+1)

elif 1000<=a<=3000:
    s = str(a)
    if s[-1]=="0":
        print(int(s[-4])*10+int(s[-3]))
    else:
        print(int(int(s[-4])*10+int(s[-3]))+1)
        
#一番短い解答
#a=int(input())
#print((a+99)//100)