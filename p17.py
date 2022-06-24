n=input('請輸入第一個矩陣').split(' ')
ans=[]
v=[]
v1=[]
for i in range(0,int(n[0])):
    s=input('輸入第一個矩陣第'+n[0]+'列的值').split(' ')
    v.append(s)
n1=input('請輸入第二個矩陣').split(' ')
for i in range(0,int(n[0])):
    s1=input('輸入第二個矩陣第'+n[0]+'列的值').split(' ')
    v1.append(s1)
if (n!=n1):
    print('兩個矩陣無法相加')
elif(n==n1):
    for s in range(0,int(n[0])):
        for d in range(0,int(n[1])):
            ans.append(int(v[s][d])+int(v1[s][d]))
for ans1 in range(0,int(n[1])):
    print(ans[ans1],end=' ')
print()
for h in range(0,int(n[1])):
    print(ans[h+int(n[1])],end=' ')