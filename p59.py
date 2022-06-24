money = int(input("輸入金額:"))
a = money // 100
b = (money%100)//50
c = ((money%100)%50)//10
d = (((money%100)%50)%10)//5
e = ((((money%100)%50)%10)%5)//1
print(a+b+c+d+e)