#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


# main()
# print('END')

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


