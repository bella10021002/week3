one=input("輸入N及M為:")
one_del=one.split(' ')
N=one_del[0]
M=one_del[1]
two=input("輸入正矩陣第一列為:")
two_del=two.split(' ')
three=input("輸入正矩陣第二列為:")
three_del=three.split(' ')
for i in range(0,3,1):
    print("輸出陣列數值第"+str(i+1)+"列為:"+ two_del[i]+" "+three_del[i])