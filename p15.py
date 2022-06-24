all=""
x=0
use_in =str(input("輸入一組四位數字為:"))
print(use_in[0])

for i in range(4):
    x=(int(use_in[i])+7)%10
    all=all + str(x)
    x=0
ans=all[2]+all[3]+all[0]+all[1]
print("輸出加密後的數字為:"+ans)