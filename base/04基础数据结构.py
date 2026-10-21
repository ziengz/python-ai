# 演示列表的API
from numpy.ma.core import append

name_list = ['小明', '小红', '小刚', '小丽', '小强', '小芳', '小亮', '小红']

# 查询相关方法：
# index()：查询指定数据所在位置下标(下标从0开始)，如果不存在直接报错
index = name_list.index("小刚")
print(index)

# count()：统计数据在当前列表中出现的次数
count = name_list.count("小红")
print(count)

# in、not in判断是否在列表中存在
hasName = "小李" not in name_list
print(hasName)
hasName = "小强" in name_list
print(hasName)

# 增加函数
# append()增加指定数据到列表中
if "小周" not in name_list:
    name_list.append("小周")
print(name_list)

# extend()函数，将一个序列追加到另一个序列中
name2_list = ['小李','小王']
name_list.extend(name2_list)
print(name_list)

# insert() 在指定位置新增数据
name_list.insert(2,"小灰灰")
print(name_list)

# pop()删除指定下标的数据，默认是删除最后一个数据，删除返回删除的元素
element = name_list.pop()
print(element)
print(name_list)

# remove()函数，删除指定元素，如果不存在也不会报错，无效果
name_list.remove("小强")
print(name_list)

# 修改操作
name_list[2] = "小美"
print(name_list)

# reverse反转函数
name_list.reverse()
print(name_list)

# sort()排序函数，reverse设置是否反转，True（反转）倒序，False（不反转）正序
num_list = [3, 7, 10, 56, 2, 9, 4, 5]
num_list.sort(reverse=True)
print(num_list)

# 列表循环遍历
for name in name_list:
    print(name)

print('*'*100)
i = 0
while i < len(name_list):
    print(name_list[i])
    i+=1

"""
💡 题目：给定一个连续递增的整数列表，找出中断的位置。
例如：[1, 2, 3, 5, 6, 8] 中，3→5 断了，6→8 也断了。
"""

def find_break_pos(list):
    for i in range(len(list)-1):
        if list[i]+1 != list[i+1]:
            print(f"{list[i]}->{list[i+1]}存在断点")


test_list = [1, 2, 3, 5, 6, 8]
find_break_pos(test_list)

# 元组
# 格式:
#   变量名称 = (元素1,元素2,元素3......)
#   变量名称 = (元素1,) : 如果元组中只有一个元素, 必须在后面添加一个逗号 否则编译器会自动转换为 数据的本身类型, 而不是元组类型
tuple1 = ('小明',)
user_tuple = ('小明','小刚','小李',20,30,40,True,False)
print(user_tuple)
print(type(user_tuple))

print(user_tuple[0])
print(user_tuple[1])

# 遍历
# for i in user_tuple:
#     print(i)

# 获取某个元素在元组中索引值
print(user_tuple.index('小刚'))

# 获取某个元素在元组中出现的次数
print(user_tuple.count('小刚'))

# 获取元组长度
print(len(user_tuple))

# 计算嵌套元组中所有数字的总和
# 1- 初始化嵌套元组
tuple1 = (
    (2, 3, 4),
    (3, 5, 7),
    (3, 4, 6)
)

sum = 0
for i in tuple1:
    for j in i:
       sum += j
print(sum)

# 给定一个元组 my_tuple，里面包含 2, 3, 4, 5, 6, 7, 8, 9, 10 元素，要求找出其中所有大于 5 的数字，并放入一个新列表中。
# 输出结果为：[6, 7, 8, 9, 10]

my_tuple = (2, 3, 4, 5, 6, 7, 8, 9, 10)
my_list = []
for i in my_tuple:
    if i > 5:
        my_list.append(i)
print(my_list)

# set集合  也可以存储不同类型的元素
name_set = {'小明','小红','小刚','小明','小刚','小丽'}
print(name_set) # 去重 和 无序 打印会发现每次都是不一样的
print(type(name_set))

for name in name_set:
    print(name)

# 增操作
name_set.add('小李')
print(name_set)

# 删操作
name_set.remove('小刚')
print(name_set)

# 查操作
print('小明' in name_set)
print('小李' not in name_set)


num_set = {3,4,True,'小明',False}
num_set.add('小红')
print(type(num_set))


# 仅适用于数组中只有一个奇数次出现数字
def find_one_odd(list):
    res = 0
    for i in list:
        res ^= i
    return res

list1 = [1,2,2,3,3]
res = find_one_odd(list1)
print(f"{res}为奇数次数字")

# 适用于多个的
# 找出数组中出现奇数次的数字
source_list = [4, 1, 2, 1, 2, 3, 5, 5]

from collections import Counter
def find_any_odd(list):
    cnt = Counter(list)
    # return [k for k,v in cnt.items() if v%2==1]
    # 等价于以下内容
    result = []
    for k,v in cnt.items():
        if v % 2 == 1:
            result.append(k)
    return result

print(find_any_odd(source_list))

"""
💡 题目：统计列表中每个数字出现的次数，并去重后排序输出。
输入: [4, 2, 2, 8, 3, 3, 1, 4, 3]
"""
source_list = [4, 2, 2, 8, 3, 3, 1, 4, 3]
source_set = []

def get_count(list):
    cnt = Counter(list)
    for k,v in cnt.items():
        source_set.append(k)
        print(f"{k}出现次数：{v}次")

get_count(source_list)
source_set.sort(reverse = False)
print(source_set)


"""
💡 题目：判断一个列表中的数字是否能组成连续序列。
例如：[4, 2, 3, 1] → True（可以重排成 [1,2,3,4]）
      [5, 3, 2, 6] → False（范围是 2~6，缺了 4）
"""
def isCountinous(list):
    list.sort(reverse = False)

    flag = False
    lack_num = []
    for i in range(len(list)-1):
        if list[i]+1 != list[i+1]:
            lack_num.append(list[i]+1)
            flag = True
    if not flag:
        print(f"可以重排成{list}")
    else:
        print(f"范围是{list[0]}~{list[len(list)-1]},缺少{lack_num}")

list1 = [2,4,1,3]
isCountinous(list1)
list2 = [3,5,2,1,6]
isCountinous(list2)


"""
💡 题目：给你一个 1 到 n 的数组，但缺少了一些数字。
       找出所有 1~n 范围内消失的数字。
输入: [4, 3, 2, 7, 8, 2, 3, 1]  (n=8，但数组里缺了 5, 6)
"""

def find_lack_num(list):
    n = len(list)
    new_set = set(list)

    lack_num = []
    for i in range(1,n):
        if i not in new_set:
            lack_num.append(i)
    return lack_num

list = [4, 3, 2, 7, 8, 2, 3, 1]
lack_num = find_lack_num(list)
print(f"n={len(list)},但数组中缺少了{lack_num}")

# 字典
# 字典的增操作
person = {'name': '小明', 'age': 19}
# 添加birthday关键字 (这种方法如果存在对应键，则修改，不存在则添加)
person['birthday'] = '2004-08-24'
print(person)

# 字典删除操作
del person['age']
print(person)

# clear()方法，清楚字典中所有元素
person.clear()
print(person)

# 字典修改操作  字典名称[key] = value
person = {'name': '小明', 'age': 19, 'address': '上海市浦东新区'}
person['age'] = 20
print(person)

# 提取字典中所有键
print(person.keys())
# 提取字典中所有value
print(person.values())
# 使用items提取数据
print(person.items())

"""
    给定一个字符串my_string，现在要求统计每个字符出现的次数: 形成结果: {'字符':出现次数,'字符2':次数}

    例如: 'abcdecf' ==> {'a':1,'b':1,'c':2,'d':1,'e':1,'f':1}
"""
my_string = 'abcdefg'
my_dict = {}
for i in my_string:
    if i in my_dict.keys():
        my_dict[i]+=1
    else:
        my_dict[i] = 1
print(my_dict)