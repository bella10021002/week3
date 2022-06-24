use_in=input("輸入值為:")
use_string=use_in.split(",")
number=[]
min=""
max=""
for i in range (0,len(use_string),1):

    number.insert(i,int(use_string[i]))
number.sort()
for i in range(0,len(number),1):
    min=min + str(number[i])

number.reverse()
for i in range(0,len(number),1):
    max=max + str(number[i])
ans=int(max)-int(min)

print("最大值數列與最小值數列差值為:" + str(ans))