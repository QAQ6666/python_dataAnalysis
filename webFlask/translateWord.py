x = int(input())
y = int(input())
# 获取最小值
if x > y:
    smaller = y
else:
    smaller = x
hcf = 0
for i in range(1, smaller + 1):
    if ((x % i == 0) and (y % i == 0)):
        hcf = i
print(hcf)
print(x * y // hcf)


