x = float(input())
if(x<0):
    print(-x / (x** + 1 ))
    exit()
print((x+1) ** 0.5)

if(x<0):
    print(-x / (x** + 1 ))
if(x>=0):
    print((x + 1) ** 0.5)

if(x<0):
    print(-x / (x ** + 1))
else:
    print((x + 1) ** 0.5)

x = -x / (x ** + 1) if x>=0 else (x + 1) ** 0.5

import math
def quadratic(a,b,c):
    key=b**2-4*a*c
    if(a ==0 and b ==0):
        print('无解')
    if(a==0 and b!=0):
        print(-(c/b))
    if key>0:
        x1=(-b+math.sqrt(key))/2*a
        x2=(-b-math.sqrt(key))/2*a
        print(x1,x2)
    if key==0:
        x1=-b/2*a
        x2=x1
        print(x1, x2)
    if key<0:
        key = 4*a*c - b**2
        x1 = (-b / 2 * a) + str(math.sqrt(key) / 2 * a) +'i'
        x2 = (-b / 2 * a) - str(math.sqrt(key) / 2 * a) +'i'
        print(x1, x2)
quadratic(1,3,-4)

userin = str(input("请输入身高（米）和体重\（公斤）【逗号隔开】:"))
userin = userin.split(',')
equation = (float(userin[1]) / float(userin[0]) ** 2)
print('BMI指数为:'+str(equation))
if(equation < 18.5):
    print("BMI指标为: 国际'偏瘦'，国内'偏瘦'")
if(equation >= 18.5 and equation < 25):
    if(equation<24):
        print("BMI指标为: 国际'正常'，国内'正常'")
        exit()
    print("BMI指标为: 国际'正常'，国内'偏胖'")
if(equation >= 25 and equation < 30):
    if (equation < 28):
        print("BMI指标为: 国际'偏胖'，国内'偏胖'")
        exit()
    print("BMI指标为: 国际'偏胖'，国内'肥胖'")
if(equation >= 30):
    print("BMI指标为: 国际'肥胖'，国内'肥胖'")


n = int(input())
if( n % 2 != 0):
    empty = int((n-1)/2)
    for i in range(1,empty+1):
        print(' ' * empty + '*' * ((2 * i) - 1))
        empty -= 1
    print('*'*n)
    empty = 1
    for z in range(int((n - 1) / 2),-1,-1):
        print(' ' * empty + '*' * ((2 * z) - 1))
        empty += 1

n = int(input())
a = str(input())
Sn = ''
for i in range(1,n+1):
    ind = a*i
    Sn = Sn + ind + '+'
print(Sn[:-1])
