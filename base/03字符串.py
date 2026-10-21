from numpy.core.defchararray import lower

text = 'I love Java programming and Java is powerful'

# 把字符串中所有java字符串替换成Python
new_text1 = text.replace("Java","Python")
print(new_text1)

# 把字符串中第一个Java进行替换Python
new_text2 = text.replace("Jave","Python",1)
print(new_text2)

# 把and字符串替换成&
new_text3 = text.replace("and","&")
print(new_text3)

# split
# 分割日期
date_str = "2026-10-17"
date_parts = date_str.split("-")
print(date_parts)

# 分割邮箱
email_str = "example@qq.com"
email_parts = email_str.split("@")
print(f"用户名:{email_parts[0]}")
print(f"域名:{email_parts[1]}")

# join
fruit_list = ['apple', 'banana', 'orange']
result = "-".join(fruit_list)
print(result)

# 生成随机数，包含大小写字母、数字
import random

def generate_code(length):
    # 定义所有可用字符
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    all_chars = uppercase+lowercase+digits
    code = ""
    # 随机选择一个索引位置
    for i in range(length):
        index = random.randint(0,len(all_chars)-1)
        code += all_chars[index]
    return code

print(f"6位随机数：{generate_code(6)}")
print(f"8位随机数：{generate_code(8)}")

# 生成随机数，包含大小写字母、数字，但要求是必须包含数字和字母

def generate_secure_code(length = 6):
    # 定义所有可用字符
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    all_chars = uppercase + lowercase + digits

    while True:
        code = ""
        for i in range(length):
            index = random.randint(0,len(all_chars)-1)
            code += all_chars[index]

        has_letter = any(c in uppercase+lowercase for c in code)
        has_digit = any(c in digits for c in code)

        if has_digit and has_letter:
            return code

print(f"安全验证码：{generate_secure_code(6)}")

# 验证用户输入验证码是否正确
def verify(correct_code,user_code):
    # 不区分大小写
    return lower(correct_code) == lower(user_code)

user_code = "eA0837"
correct_code = "eA0837"
if verify(correct_code,user_code):
    print("验证码正确")
else:
    print("验证码错误")



