# -*- coding: utf-8 -*-
# @Time : 2021/3/7 0007
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test.py
# import math
#
# for i in range(0,11):
#     print(i)
#
# print(math.pow(3, 3))
import time

#
# # 定义装饰器
# def time_calc(func):
#     def wrapper(*args, **kargs):
#         start_time = time.time()
#         f = func(*args, **kargs)
#         exec_time = time.time() - start_time
#         print("func.name:{}\texec_time:{}".format(func.__name__, exec_time))
#         return f
#
#     return wrapper
#
#
# # 使用装饰器
# @time_calc
# def add(a, b):
#     return a + b
#
#
# @time_calc
# def sub(a, b):
#     return a - b
#
#
# sum = add(1, 3)
# part = sub(23, 1)
list1 = (1,5,3)
print(sum(list1))