ans=["red","blue","red","green"]
n=0
while n<=10:
    q=input("依序輸入四個顏色(中間以空白隔開):").split()
    if q==ans:
        print("正確答案")
        exit()
    else:
        if q[0]=="red":
            a=1
        elif q[0]=="blue" or q[0]=="green":
            a=2
        else:
            a=3
        
        if q[1]=="blue":
            b=1
        elif q[1]=="red" or q[1]=="green":
            b=2
        else:
            b=3

        if q[2]=="red":
            c=1
        elif q[2]=="blue" or q[2]=="green":
            c=2
        else:
            c=3

        if q[3]=="green":
            d=1
        elif q[3]=="blue" or q[3]=="red":
            d=2
        else:
            d=3
    print(a,b,c,d)
    n+=1
print("挑戰失敗")