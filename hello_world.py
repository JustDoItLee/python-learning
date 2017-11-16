#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name = input("请开始你的表演:")
# print("准备好你的表演了吗?", name)

# num = 1024 * 768;
# print("1024 * 768 = ", num)
#
# if num > 100:
#     print("大于100")
# else:
#     print(-num)
#
# print("I\'m \"ok\"")
# print(r'"I\'m \"ok\""')
# print('''hi\nboy''')

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
#
# print(n, "\n", f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)
#
# print(ord("上"))
# print(chr(88))
#
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
#
# print(len("cn,dota"))
#
# print('Hello, %s' % 'world')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
#
# s1 = 72
# s2 = 85
# result = '%.1f%%' % ((s2 - s1) / s1 * 100)
# print(result)

# arr = ["ist",2,'3'];
# print(len(arr))
# print(arr[2])
# arr.append("jack")
# print(arr)
# arr.pop(1)
# print(arr)
# arr.insert(2,"lizhi")
# print(arr)

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

# num = 10
# print("this is ", num)
#
# if num < 10:
#     print("小于10")
# elif num == 10:
#     print("等于10")
# else:
#     print("大于10")

# n = input()
# if int(n) > 10:
#     print("true")

# list = list(range(5))
# print(list)
# sum = 0;
# for x in range(101):
#     sum = sum + x
# print(sum)


# d = {}
# d['Jack'] = 90
# print(d['Jack'])

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(n1)

import os

from collections import Iterable
from functools import reduce

import math

import functools
from types import MethodType


def getX(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x;


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# r = move(100, 100, 60, math.pi / 6)
# print(r)

def mulMethod(name, age, **keyWorld):
    print('name:', name, 'age:', age, 'other:', keyWorld)


# mulMethod("lizhi",19,addr='Chaoyang', zipcode=123456)



def person(name, age, *, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


# person(1, 2, city=3, job=4)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# args = [1, 2, 3]
# kw = {'d': 1, 'x': 2}
# f1(*args, **kw);
# f2(*args, **kw);

def fact(n, m):
    if n == 1:
        return m;
    return fact(n - 1, n * m)


# print(fact(5,1))

def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


# move(3,"A","B","C")

# L = list(range(1,100,2))
#
# L = ['1','2','3','4','5']
# print(L[:2])
# print(L[-1])
# print(L[:-2])
# print(L[::-1])

d = {'jack': 12, 'lucy': 13}
# for value in d.values():
#     print(value)

isIns = isinstance(chr(65), Iterable)
# print(isIns)

# for val, index in enumerate(d):
#     print(val, index)

files = [file for file in os.listdir('.')]
# print(files)

lowerStr = [s.lower() for s in ['Jame', 'Wade', 'Curry']]
# print(lowerStr)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
toLower = [s.lower() for s in L1 if isinstance(s, str)]


# print(toLower)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# f = fib(6)
# print(f)
#
# for s in f:
#     print(s)

def yanghui(num):
    L = [1]
    for i in range(num):
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(i)] + [1]


# for t in yanghui(5):
#     print(t)

# f = abs
# print(f(-4))

def name(s):
    return s.capitalize();


# print("str".title()) 变大写 或者s.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(name, L1))


# print(L2)

def prod(L):
    return reduce(lambda x, y: x + y, L)


# print({'java':1,'php':2}['java'])

# print(prod([1,2,3]))

def str2int(s):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def str2float(s):
    s_list = s.split('.')
    float_i = str2int(s_list[0])
    float_f = str2int(s_list[1]) / (10 ** len(s_list[1]))
    return float_i + float_f


# print('str2float(\'123.456\') =', str2float('123.456'))

def trimStr(s):
    return s and s.strip()


# print(list(filter(trimStr, ['A', '', 'B', None, 'C', '  '])))

# print('avc'.rstrip('c'))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n


output = filter(is_palindrome, range(1, 1000))
# print(list(output))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[1]


L2 = sorted(L, key=by_name, reverse=True)


# print(L2)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 5)


# print(f())

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s begin call %s()" % (text, func.__name__))
            ret = func(*args, **kw)
            print("%s end call %s()" % (text, func.__name__))
            return ret

        return wrapper

    if isinstance(text, str):
        return decorator
    else:
        f = text
        text = ''
        return decorator(f)


@log  # ('excute')
def f():
    print("soso!")


# f()

class Student(object):
    def __init__(self, name):
        self.__name = name

    def _getName(self):
        return self.__name


# stu = Student("jack")
# print(stu._getName())
# print(stu.__name)

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('dog is running...')


class Time(object):
    def run(self):
        print('time is running...')


def run(animal):
    animal.run();


dog = Dog();
time = Time();


# run(dog)
# run(time)og

# print(type(run))


def readData(fp):
    pass


def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


class Student(object):
    age = 15;

    def __init__(self, name):
        self.name = name


# s = Student('Bob')
# s.score = 90
# print(s.score,s.name)

# print(Student.age)
# s = Student('mick')
# print(s.age)
# s.age = 16
# Student.age = 17
# print(s.age)
# print(Student.age)

def bindMethod(self, age):
    self.age = age;


def classBindMethod(self, age):
    self.age = age;


# s = Student('jack')
# s.bindMethod = MethodType(bindMethod,s);
# s.bindMethod(10)
# print(s.age)

# Student.classBindMethod = classBindMethod
# s = Student('make')
# s.classBindMethod(12)
# # print(s.age)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         m = j * i
#         print('%s x %s = %-5s' % (j, i, m), end='')
#     print()

# print(hasattr(Student,'age'))
# setattr(Student,'score',1)
# print(getattr(Student,'score'))

class Org(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# s = Student()
# s.score = 1001
# print(s.score)


class Student(object):
    def __init__(self):
        self._birth = 1996

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


# s = Student()
# print(s.age)

class Screen(object):
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("请输入数字");
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("请输入数字")
        self._width = value

    @property
    def resolution(self):
        return self._height * self._width


# s = Screen()
# s.height = 100
# s.width = 80
# print(s.resolution)
