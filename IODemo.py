#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random
import threading

from shutil import copyfile

import time

from multiprocessing import Queue, Process

str = '/Users/lizhi/Downloads/imix/市场数据处理V1.12.2配合本币V2.7.11.0升级/imix10t20开发指引'
strPic = '/Users/lizhi/Downloads/E1D0BC0C07FD36044E8706B97DC5182B.png'
with open(str, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        pass
        # print(line.strip())

with open(strPic, 'rb') as f:
    for line in f.readlines():
        pass
        # print(line.strip())

# print(os.uname())
# print(os.environ)
# print(os.path.abspath('.'))
# s = os.path.join('/Users/lizhi/Downloads', 'vue.min.js')
# print(os.path.splitext(s))
# os.mkdir(s)
# os.rmdir(s)


s = os.path.join('/Users/lizhi/Downloads', 'text.txt')
s2 = os.path.join('/Users/lizhi/Downloads', 'text2.txt')
s3 = '/Users/lizhi/Downloads'

# print(s2.find('text'))
# with open(s,'r',encoding='utf-8') as f:
#     with open(s2,'w',encoding='utf-8') as w:
#         for line in f.readlines():
#             w.write(line.strip())

# copyfile(s,s2)

list = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']


# print(list)

def search(filename, filepath):
    if not os.path.isdir(filepath):
        print("错误路径")
        return
    for d in os.listdir(filepath):
        path = os.path.join(filepath, d)
        if os.path.isdir(path):
            if d.find(filename) != -1:
                print(path)
        if os.path.isdir(path):
            search(filename, path)


print()


# search('text.text', '/Users/lizhi/Downloads')

# s4 = os.path.join('/Users/lizhi/Downloads', 'E1D0BC0C07FD36044E8706B97DC5182B.png')
# s5 = os.path.join('/Users/lizhi/Downloads', 'yzzz.png')
# with open(s4,'rb') as f:
#     with open(s5,'wb') as w:
#             w.write(f.read())

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
