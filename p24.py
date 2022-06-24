list1 = []

n = int(input("請輸入陣列大小"))
for i in range(n):
    list1.append(input().split( ))
for z in range(n):
    for y in range(n):
        list1[z][y] = int(list1[z][y])
    
max1 = 0
max2 = 0
max3 = 0
for j in range(n):
    for k in range(n):
        if list1[j][k] > max1:
            max1 = list1[j][k]

for a in range(n):
    for b in range(n):
        if list1[a][b] > max2 and list1[a][b] < max1:
            max2 = list1[a][b]

for c in range(n):
    for d in range(n):
        if list1[c][d] > max3 and list1[c][d] < max1 and list1[c][d] < max2:
            max3 = list1[c][d]

print("最大值為:",max1 + max2 + max3)
for e in range(n):
    for f in range(n):
        if list1[e][f] == max1:
            max1place = str("(")+str(e+1)+str(",")+str(f+1)+str(")")
        if list1[e][f] == max2:
            max2place = str("(")+str(e+1)+str(",")+str(f+1)+str(")")
        if list1[e][f] == max3:
            max3place = str("(")+str(e+1)+str(",")+str(f+1)+str(")")
print("位置為"+max1place+max2place+max3place)