from ast import While
from shutil import which
M = int(input("輸入階乘值:"))
s = 1
N = 1
while (s < M):
    s = s*N
    N = N + 1
print("超過M為",M,"的最小階層N值為:",N-1)