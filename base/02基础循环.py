for row in range(1,10):
    for col in range(1,row+1):
        # print(f'当前行号{row},当前列号{col}')
        print(f'{col} * {row} = {row * col}',end='\t')
    # print()默认输出换行符
    print()

print('#'*100)

for row in range(1,10):
    for col in range(1,row+1):
        # print(f'当前行号{row},当前列号{col}')
        print(f'{col} * {row} = {row * col}',end='\t')
        # 当col为4的时候结束内层循环，跳转到外层循环
        if col == 4:
            # break只能跳出它所在的循环(离他最近的循环)
            break
    # print()默认输出换行符
    print()
print('#'*100)