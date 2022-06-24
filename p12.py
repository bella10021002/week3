num=[]
cou=[]
use_in =input("請輸入一整數序列:")
use_sp=use_in.split(" ")
ans_int=map(int,use_sp)
ans_list=list(ans_int)
myset = set(ans_list)
for item in myset:
    num.append(item)
    cou.append(ans_list.count(item))
location=cou.index(max(cou))
number=str(num[location])


if max(cou)>=3:
        print("過半元素為:" + number)
else:
        print("過半元素為:No")