a=(input("請輸入傳送密碼(6位數):"))
if len(a)<6:
    print("密碼長度不足6個字元,請重新輸入")
else:
    b=list(a)
    b1=int(b[0])
    b2=int(b[1])
    b3=int(b[2])
    b4=int(b[3])
    b5=int(b[4])
    b6=int(b[5])
    c=(b1*4%7,b2*4%7,b3*4%7,b4*4%7,b5*4%7,b6*4%7)
    print("解密後的密碼:",c)