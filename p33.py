a = int(input("輸入國文成績:"))
b = int(input("輸入英文成績:"))
c = int(input("輸入微積分成績:"))
d = int(input("輸入體育成績:"))
e = int(input("輸入程式設計成績:7"))
avg = (a+b+c+d+e)/5
numbers = [a, b, c, d, e]
max_value = None
for num in numbers:
    if (max_value is None or num > max_value):
        max_value = num

mix_value = None
for num in numbers:
    if (mix_value is None or num < mix_value):
        mix_value = num

print("平均分數:",avg)
print("最高分科目:",max_value,"分")
print("最低分科目:",mix_value,"分")