b = [98, 80, 102, 110, 126, 120, 115]
h = [79, 66, 68, 74, 83, 80, 78]

sum = 0
for bavg in b:
    sum += bavg

max_value = None
for num in b:
    if (max_value is None or num > max_value):
        max_value = num

mix_value = None
for num in b:
    if (mix_value is None or num < mix_value):
        mix_value = num

sum1 = 0
for havg in h:
    sum1 += havg

max_value1 = None
for num in h:
    if (max_value1 is None or num > max_value1):
        max_value1 = num

mix_value1 = None
for num in h:
    if (mix_value1 is None or num < mix_value1):
        mix_value1 = num

print("血壓平均：{:.2f}".format(sum/7))
print("血壓最大值:", max_value )
print("血壓最小值:", mix_value)

print("心跳平均：{:.2f}".format(sum1/7))
print("心跳最大值:", max_value1 )
print("心跳最小值:", mix_value1) 