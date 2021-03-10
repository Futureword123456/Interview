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
# list1 = (1,5,3)
# print(sum(list1))

#
# def leftRotate(arr, d, n):
#     for i in range(d):
#         leftRotatebyOne(arr, n)
#
#
# def leftRotatebyOne(arr, n):
#     temp = arr[0]
#     for i in range(n - 1):
#         arr[i] = arr[i + 1]
#     arr[n - 1] = temp
#
#
# def printArray(arr, size):
#     for i in range(size):
#         print("%d" % arr[i], end=" ")
#
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr, 2, 7)
# printArray(arr, 7)
# arr1 = []
# arr = [8, 2, 3, 4, 5, 6, 7]
# for i in arr:
#     arr1 = arr[:]
# print(arr)

# # print(list(str1))
# str2 = ""
# for i in range(1, len(str1) + 1):
#     # print(i)
#     if i != 2:
#         str2 = str2 + str1[i - 1]
# # print(str2)
# lst = []
# str1 = 'abcdefg'
# for i in range(1,len(str1)+1):
#     lst.append(i)
# lst.pop(2)
# print(lst)

# print(str1[0:len(str1)])
# print(len(str1))
# print(str1.replace(str1,"1"))
key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
# for i,j in key_value.items():
#     v = key_value[i]
#     print(i,j)
#
# for i in key_value:
#     """i是key"""
#     v = key_value[i]
#     """v是value"""
#     print(v)
"""key_value[5]是根据key来取到相应的value"""
print(key_value[5])