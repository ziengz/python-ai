print("hello world")

name = "zzp"
age = 22
score = 100

print(f"姓名:{name},年龄:{age},成绩:{score}")
print("姓名:{0}，年龄:{1}".format(name,age))
print("成绩：{:.2f}".format(score))
print(f"成绩：{score:.2f}")
print(f"学号：{1:06d}")
# phone = input("请输入手机号：")
# print(f"手机号：{phone}，类型：{type(phone)}")
#
# produce_name = input("请输入商品名称：")
# price_str = input("请输入商品价格：")
# count_str = input("请输入购买数量：")
#
# price = float(price_str)
# count = int(count_str)
# total = price * count
# print(f"您购买了{produce_name}，单价：{price:.2f}元，数量：{count}，总价：{total:.2f}")

# 判断奇偶
# num = int(input("请输入一个整数："))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

# 超时打折逻辑
flag = bool(input("是否会员："))
num = float(input("共计消费了："))
total = num
if flag:
    if num >= 200:
        total -= 50
    else:
        total *= 0.9
print(f"需支付{total:.2f}")


