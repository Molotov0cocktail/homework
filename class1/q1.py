perweight = 35
times = 64
sum = 0
for i in range(times):
    sum += 2**(i)
weight = sum * perweight / 1000000
print(f"总重量是：{weight}吨")