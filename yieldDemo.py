#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def countdown(n):
    print("Counting down from", n)
    while n >= 0:
        newvalue = (yield n)
        print('newvalue:', newvalue)
        print('n:', n)
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


# c = countdown(5)
# for x in c:
#     print ('x:',x)
#     if x == 5:
#         c.send(3)
#         # c.send(2)

n = 0


def yieldGen():
    global n
    n = n + 1
    print("start")
    yield 1
    print("end")


c = yieldGen()
for i in c:
    print(i)

print(n)

n = n + 1
print(n)
