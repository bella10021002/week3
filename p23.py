n = float(input("輸入正整數(0~100):"))
dx = 0.0001
x = float(0)

if n < 0:
    print("X")
elif n >= 0:
    s = float(0)
    while x < n:
        s = s + (x*x)*dx
        x = x + dx
    print('%.1f'%s)