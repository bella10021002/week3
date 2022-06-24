x=1
y=0
ans=[]
use_in=int(input("請輸入第一行正整數為:"))
use_in_two=input("第二行中數列中的數值為:")
use_string=use_in_two.split(" ")
print(use_string)
for i in range(0,use_in,1):
    for j in range(i+1,use_in,1):
        if use_string[i]==use_string[j]:
            x=x+1
    if x>=2 and x>y:
        y=x
        ans.append(use_string[i])
        x=0
ans.reverse()
if ans==[]:
    print("每個數字剛好只出現一次")
else:
    print("最大出現次數的數字為:"+ ans[0])
    print("最大出現次數的數字為:"+ str(y))