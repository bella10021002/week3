import numbers
from re import X
x=""
ans=0
all=[]

number=input("輸入數字:")
long=len(number)
for k in  range(0,long,1): 
    if ans!=0:
        break


    for p in range(k,long,1):
        x= x+str(number[p])


    for i in range(1,int(x)+1,1):
        if int(x) % i ==0:
             ans +=1


    if ans==2 or  ans==1:
        print(x+"最大質數")



    elif k==(len(number)-1) :
       if ans>2:
            print("NO prime found")                 
    else:
        x=""
        ans=0