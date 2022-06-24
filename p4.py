x = float(input("輸入平面鍾某點的X值:"))
y = float(input("輸入平面鍾某點的Y值:"))
a = int((x*x)+(y*y))
if x == 0 and y == 0:
    print("該點位於原點")
elif x == 0 and y > 0:
    print("該點位於上半平面Y軸上,離原點距離為根號",a)
elif x == 0 and y < 0:
    print("該點位於下半平面Y軸上,離原點距離為根號",a)
elif x > 0 and y == 0:
    print("該點位於右半平面X軸上,離原點距離為根號",a)
elif x < 0 and y == 0:
    print("該點位於左半平面X軸上,離原點距離為根號",a)
elif x > 0 and y > 0:
    print("該點位於第一象限，離原點距離為根號",a)
elif x < 0 and y > 0:
    print("該點位於第二象限，離原點距離為根號",a)
elif x < 0 and y < 0:
    print("該點位於第三象限，離原點距離為根號",a)
elif x > 0 and y < 0:
    print("該點位於第四象限，離原點距離為根號",a)