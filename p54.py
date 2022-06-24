import math
removing = float(input("輸入路程公里數:"))
first = removing - 1.5
price = (first*1000)/250
if first<0:
    print(75)
else:
    print(math.ceil(price)*5+75)