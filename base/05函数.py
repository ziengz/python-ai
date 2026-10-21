# 推导式
# 变量名 = [表达式 for 变量 in 列表]
# 定义0-9之间的列表
list1 = []
for i in range(10):
    list1.append(i)
print(list1)
# 推导式
list1 = [i for i in range(10)]
print(list1)
# 变量名 = [表达式 for 变量 in 列表 if 条件]
# 生成0-9之间的偶数（i%2 = 0）序列
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)
print(list2)
# 推导式
list2 = [i for i in range(10) if i%2==0]

# 变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]
# 生成教室座位坐标列表3行 × 4列
seats = []
for row in range(3):
    for col in range(4):
        seat = (row,col)
        seats.append(seat)
print(seats)

seats = [(row,col) for row in range(3) for col in range(4)]

# 生成所有 (0-9, 0-9) 的坐标对（排除对角线 i==j）
coords = [(row,col) for row in range(10) for col in range(10) if row != col]
print(coords)

# 用户输入10, 表示要生成 1~10的每一个数字的平方的集合
n = int(input("请输入一个正整数："))
result = [i*i for i in range(1,n+1)]
print(result)

# lambda表达式

def func(str):
    return "你好"+str
print(func("zzp"))

fn = lambda name : "你好" + name
print(fn("zzp"))

# 计算两数相和
fn1 = lambda num1,num2 : num1+num2
print(fn1(1,2))

fn2 = lambda num1,num2 = 10 : num1 + num2
print(fn2(10))

# 带 if判断（三目运算符）的lambda表达式
def func1(name: str):
    a=0
    if name == "小明":
        a=1
    else:
        a=0
    return a

def func2(name:str):
    return 1 if name=="小明" else 0

func3 = lambda name:1 if name=="小明" else 0


print("------------------------------------")
# 在一个列表中, 放置了三个元素, 每一个元素又是一个字典
students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
print(students)

# 按name值升序排列
students.sort(key = lambda i : i["name"])
print(students)

# 按name值降序排列
students.sort(key = lambda i : i['name'],reverse = True)
print(students)