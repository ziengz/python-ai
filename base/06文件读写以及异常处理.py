# 自动打开 + 自动关闭文件，不用手动写`f.close()`
# 迭代读取
from fontTools.diff import file_exists

with open("test.txt",'r',encoding='utf-8') as f:
    for line in f:
        print(line.rstrip('\n'))

# read()
print('*'*50)
with open("test.txt",'r',encoding='utf-8')as f:
    context = f.read()
    print(context)

# readline()
print('*'*50)
with open("test.txt",'r',encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.rstrip('\n'))
        line = f.readline()

# readlines()
print('*'*50)
with open("test.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()  # 返回列表
    for i,line in enumerate(lines):
        print(f"第{i+1}行：{line.rstrip('\n')}")

# 分块读取
def read_large_file_by_chunks(filename,chunk_size = 1024):
    with open(filename,'r',encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            # 这里对分块分拣进行处理
            # print(chunk)
def read_large_file_by_line(filename,batch_size = 1024):
    batch = []
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            batch.append(line.rstrip('\n'))
            if len(batch) == batch_size:
                print(batch)
                batch = []
        if batch:
            print(batch)

# 写入
with open("test.txt",'w',encoding='utf-8') as f:
    f.write("第一行")
    f.write("第二行")

# 追加
with open("test.txt",'a',encoding='utf-8')as f:
    f.write("这是追加的一行")

# 模式三，使用print()函数
with open("test.txt",'w',encoding='utf-8') as f:
    print("第一行",file = f)
    print("第二行",file = f)

# 写入列表
lines = ["第一行\n","第二行\n","第三行\n"]
with open("test.txt","w",encoding='utf-8')as f:
    f.writelines(lines)

# 文件指针操作
with open("test.txt",'r',encoding='utf-8') as f:
    print(f.tell())  # 0

    context = f.read(10)
    print(f.tell())  # 10

    # f.seek(offset, whence=0)
    # whence = 0 文件开头    offset ≥0，从开头往后移
    # whence = 1 当前指针位置 文本模式下不支持，二进制模式可用正负
    # whence = 2 文件末尾    二进制模式下 offset 负数就是往前读
    f.seek(5)    # 回到文件开头后第五个字节
    #f.seek(-3,1) # 从当前位置往前3个字节

    # f.seek(-5,2) # 从最后往前5个字节，但是这种方式只能通过二进制模式，即rb

    # 获取文件大小
    f.seek(0,2)
    file_size = f.tell()

def read_csv(filename):
    infos= []
    with open(filename,'r',encoding='utf-8') as f:
        f.readline() # 跳过表头
        for line in f:
            id,name,age,city = line.rstrip('\n').split(',')
            infos.append({
                'id':id,
                'name':name,
                'age':age,
                'city':city
            })
    return infos

infos = read_csv('test_file.csv')
print(infos)

# 写入csv
def write_csv(filename,infos):
    import os
    file_exist = os.path.exists(filename)

    with open(filename,'a',encoding='utf-8') as f:
        if not file_exist:
            f.write('id,name,age,city\n')
        for info in infos:
            line = f"{info['id']},{info['name']},{info['age']},{info['city']}\n"
            f.write(line)

infos = [{'id': '11', 'name': '夏利', 'age': 49, 'city': '山东'}]
write_csv('test_file.csv',infos)
print(read_csv('test_file.csv'))


# 读取json
import json
def read_json(filename):
    with open(filename,'r',encoding='utf-8')as f:
        data = json.load(f)
    return data

def write_json(filename,data):
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(data,f,indent = 2,ensure_ascii=False)




























