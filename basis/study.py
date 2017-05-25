#!/usr/bin/python
# coding:utf-8
import sys
'''L = [75, 92, 59, 68]
sum = 0
for item in L:
    sum += item
print(sum / len(L))'''

'''for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y'''

'''d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
if 'xj' not in d:
    d['xj'] = 100

for key in d:
    print key

s = set([1, 1, 2, 2, 3, 3])
print(s)'''

'''L = ['Adam', 'Lisa', 'Bart', 'Paul', 'xmt', 'xj']

print(L[0:3])
print(L[:])
print(L[::2])'''


'''
range()函数可以创建一个数列：
range(1, 101)
[1, 2, 3, ..., 100]
请利用切片，取出：

1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。
'''
'''R = range(1, 101)
print(R[0:10])

s3 = []
s5 = []

for num in R:
    if num % 3 == 0:
        s3.append(num)
    if num < 50 and num % 5 == 0:
        s5.append(num)

print(s3)
print(s5)'''

'''
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in L:
    print(index, '-', name)'''

'''d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
print(d.items())
for key, value in d.items():
    print(key, ':', value)
'''


'''def power(x):
    return x * x

print(power(10))
'''


'''def power(x, n=1):
    s = 1
    while n > 0:
        n = n - 1
        s *= x
    return s


print(power(10))
print(power(10, 2))
print(power(10, 3))
print(power(10, 4))'''

# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。


'''def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 9, abs))'''

'''sum = 0


def f(x, y):
    # sum = sum + x * y
    # print(x, y)
    return x + y


l = reduce(f, [1, 3, 5, 7, 9], 0)
print(l)


def is_odd(x):
    return x % 2 == 1


fl = filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
print(fl)'''

'''def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
'''

'''class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


xmt = Student('xmt', 59)
print(xmt.get_name())
print(xmt.get_score())
'''

'''import math

print(math.pow(2, 10), __name__)'''


'''from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
'''

'''import os
from datetime import datetime

pwd = os.path.abspath('.')


print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)

    mtime = datetime.fromtimestamp(
        os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')

    flag = '/'if os.path.isdir(f) else ''

    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))'''


'''import urllib.request
response = urllib.request.urlopen('http://www.baidu.com/')
html = response.read()
print(html)'''



'''import re
print(re.findall("[A-Za-z]", '122133shh23h4h4h4'))'''

from collections import Iterable, Iterator
 
for x in iter([1, 2, 3, 4, 5]):
    print(x)