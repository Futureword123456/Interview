# -*- coding: utf-8 -*-
# @Time : 2021/3/12 0012
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 65.py

"""输入三个整数x,y,z，请把这三个数由小到大输出。"""


def Sort(a, b):
    d = 0
    if a > b:
        d = a
    else:
        d = b
    return d


for _ in range(0, 3):
    x = int(input("输入三个数:"))

if __name__ == "__main__":
    pass
