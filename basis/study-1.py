#!/usr/bin/python3
# coding:utf-8
# https://segmentfault.com/a/1190000009422887
import sys

# print (sys.platform)
# print (sys.api_version)
# print (sys.prefix)
# print (sys.stderr)

# a = 100
# if a >= 0:
#     print(a)
# else:
#     print (-a)

# 输出hello word

#<60        差
# 60-80      良
# 80-100     优

'''print ("helle word")

isUpdate = True
money = 23.1
say = "ni hao"
print (isUpdate, money, say)'''

# 声明变量

# name = "tianjianyu"
# 上述代码声明了一个变量：变量名为name，变量的值为"tianjianyu"
# 变量的作用是在内存的某个位置保存的一个内容
# 变量定义的规则：
# <1>变量名只能是 字母、数字或下划线的任意组合
# <2>变量名的第一个字符不能是数字
# <3>以下关键字不能声明为变量名
# ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
# <4>ps:下划线分割

# score = input('请你输入一个分数')
# print(score)

# name = input('please enter your name: ')
# print('hello,', name)

# 整数
# 创建
# a = 123
# print(type(a))
# 第二种：

# inputStr = input('请输入一个数')

# try:
#     score = int(inputStr)
# except:
#     score = 0

# if score > 90:
#     print('优秀')
# else:
#     print('差')


# a = int('abc')
# print(type(a))

# 转换

'''age = '18'
# 看下类型
print(type(age))
# 将str转换为int
new_age = int(age)
print(type(new_age))'''


# 2>布尔值（bool）
'''a = True
print(type(a))

b = False
print(type(b))'''

# 转换：-数字转换：
'''a = bool(0)# ''   0 
print(a)

b = bool('a')  #1 a
print(b)'''

'''a = '123'
new_a = bool(a)
print(new_a)

a = ''
new_a = bool(a)
print(new_a)'''

# 3>字符串
# 创建：
'''a = 'tianjianyu'
print(type(a))

b = str('tianjianyu')
print(type(b))
'''

# 转换
'''a = 19
print(type(a))
# print结果为int，为整数
new_a = str(a)
print(type(new_a))
# print结果为str，为字符串'''

# 字符串的拼接：
'''name = 'tianjianyu'
gender = '男'
new_str = name + gender
print(new_str)'''

'''n = 'xmt'
pwd = 999

name = input('please input your name')
password = input('please input your password')

if n == name and pwd == password:
    print('登录成功'+ name + '|' + password)
else:
    print ("登录失败" + name + '|' + password)'''

# 单引号和双引号作用一样？

'''a = 999
new_a = str(a)
print(type(new_a))'''

# 字符串的格式化
'''name = 'user:tianjianyu,gender:%s,age:%s'
new_name = name % ('男', 23)
print(new_name)'''

# 判断子序列是否在字符串中
'''name = 'user:tianjianyu,gender:男,age:23'
if 'tianjianyu' in name:
    print('yes')
else:
    print('no')'''

# 移除空白
'''name = ' tianjianyu '
new_name = name.strip()  # y移除左右
print(new_name)

new_name = name.lstrip()  # 移除左边
print(new_name)

new_name = name.rstrip()  # 移除右边
print(new_name)'''


# 分割
'''user_info = 'tianjianyu boy 23'
new_user_info = user_info.split()
print(new_user_info)'''

# 长度
'''user_info = 'tianjianyu boy 23'
print(len(user_info))
new_user_info = user_info.split()
print(len(new_user_info))
'''

# 索引
'''val = 'tianjianyu'
v = val[0]
print(v)'''

# 切片
'''val = 'tianjianyu'
print(val[0])     #第一个
print(val[0:2])   #第一个到第二个'''
# 字符串功能总结：
# https://segmentfault.com/a/1190000009370652
'''name.upper()
name.lower()
name.split()
name.find()
name.strip()
name.startswith()
name.format()
name.replace()
"xmzncc".join(["as",'bb'])'''
# 额外功能：

'''name[0]
name[0:3]
name[0:3:2]
len(name)'''
# for循环，每个元素是字符

# 列表（list）

# 创建
'''a = ['user', 'age', 'gender']
print(type(a))

a = list(['user', 'age', 'gender'])
print(type(a))'''

# 索引
'''a = ['user', 'age', 'gender']
print(a[0])'''

# 长度
'''a = ['user','age','gender']
print(len(a))
'''
# 切片
'''a = ['user', 'age', 'gender']
print(a[0::2])'''

# 追加：
'''a = ['user','age','gender']
a.append('fuck')
print(a)'''

# 删除
'''a = ['user', 'age', 'gender']
a.remove('user')
print(a)'''

# 更新
'''a = ['user', 'age', 'gender']
a[1] = 'fuck'
print(a)'''

# for循环：
'''
a = ['user', 'age', 'gender']
for item in a:
    print(item)'''

# 字典（dict）

# 创建:
'''a = {
    'name': 'tianjianyu',
    'age': 18
}
print(type(a))'''

# 基本操作：---1，获取索引值：
'''a = {
    'name': 'tianjianyu',
    'age': 18
}
v = a['name']
print(v)'''

# 增加：有--修改；无--添加:
'''a = {
    'name': 'tianjianyu',
    'age': 18
}
a['gender'] = '男'  # 无则添加
print(a)

a['name'] = 'zzz'  # 有则修改
print(a)'''

# 删除：
'''a = {
    'name': 'tianjianyu',
    'age': 18
}
del a['age']
print(a)
'''

# 循环：
'''a = {
    'name': 'tianjianyu',
    'age': 18
}
for item in a.keys():  # 循环key值
    print(item)

for item in a.values():
    print(item)  # 循环value值

for key, value in a.items():  # 循环key,value值
    print(key, value)'''

# 长度：
'''
a = {
    'name': 'tianjianyu',
    'age': 18
}
print(len(a))
'''

'''i = 0
while i < 10:
    i += 1
    if i == 7:
        continue
    print(i)'''


# 自己在内部 写死一个用户名xmt 和密码 666
# 程序接收用户输入用户名  输入密码
# 对比用户输入的用户名和密码是否正确
# 如果正确 打印出: 登录成功 ，欢迎：xxx
# 如果登录失败  打印出： 登录失败  用户名+|+密码
# 注意字符串和整数的拼接
'''n = 'xmt'
psw = '666'
name = str(input('请输入用户名'))
password = str(input('请输入密码'))


if n == name and psw == password:
    print('登录成功')
else:
    print('登录失败'+ name + '|' + password)'''

''' 
age = input('输入你的年龄')
if type(age) is int:
    if age >= 18:
        print('your age is ', age)
        print('adult')
    elif age < 18:
        print('your age is', age)
        print('kid')
else:
    print('输入错误')'''

# list
# names = ['xmt', 'xj', 'xx']

# print(len(names))
# print(names[0], names[1], names[2], names[3], names[4])
# print(names[-1])
# print(names[len(names)-1])

# names.append('xiaoxiaoxiong')
# print(names)

'''nums = range(101)
sum1 = 0
sum2 = 0
for num in nums:
    if num % 2 == 0:
        sum1 = sum1 + num
    else:
        sum2 = sum2 + num
print(sum1,sum2)'''

'''
first = nums[0]
last = nums[-1]
all = (first + last) * len(nums) / 2'''

# print(sum)


'''names = ['xmt','xiongjian','xiaoxiaoxiong']
for name in names:
    print('hello'+name)'''
'''
num = 0
sum1 = 0
sum2 = 0
sum3 = 0
while num < 101:
    if num % 2 == 0:
        sum1 = sum1 + num
    else:
        sum2 = sum2 + num
    
    sum3 = sum3 + num
    num = num + 1

print(sum1, sum2, sum3)'''


# 求1-100 的总和  基数和 偶数和

# for while 两种实现

'''nums = range(101)
sum1 = 0
sum2 = 0

for num in nums:
     if num%2==0:
        sum1 = sum1 + num
     else:
        sum2 = sum2 + num
sum = sum1+sum2
print(sum1,sum2,sum)'''

'''num = 0
sum2 = 0
sum3 = 0

while num < 101:
    if num % 2 == 0:
        sum2 = sum2 + num
    else:
        sum3 = sum3 + num
    num = num + 1

sum1 = sum3 + sum2
print(sum2, sum3, sum1)'''


'''name = 'xmt'
pwd = "123"
time = 1
max_num = 3
while 1 < 2:
    input_name = input('请输入你的用户名：')
    input_pwd = input('请输入你的密码')
    if input_name == name and pwd == input_pwd:
        print('登录成功')
        break
    elif time < max_num:
        time += 1
        print('输入用户名或者密码错误')
    else:
        print('最多输入三次')
        break'''

'''time = 1
while time:
    name = input('请输入您的用户名：')
    pwd = input('请输入您的密码：')
    if name != 'xmt' or pwd != '123':
        if time < 3:
            print('登录失败，请重新输入')
            time += 1
            continue
        print('您的登录次数过多，已锁定')
        break
    else:
        print('登录成功')
        break'''

n = 'xmt'
psw = '123'
time = 1

while True:
    name = input('请输入您的账号')
    password = input('请输入您的密码')
    if n == name and psw == password:
        print('登录成功')
        break
    elif time < 3:
        time += 1
        print('请输入正确的用户名和密码')
    else:
        print('登录次数太多，已锁定')
        break