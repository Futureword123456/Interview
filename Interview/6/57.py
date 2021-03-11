# -*- coding: utf-8 -*-
# @Time : 2021/3/11 0011
# @Author : yang
# @Email : 2635681517@qq.com
# @File : 57.py
"""Python 二分查找"""


# 返回 x 在 arr 中的索引，如果不存在返回 -1
# l表示起始位置，r表示结束位置
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:
        """取中间的位置"""
        mid = int(l + (r - l) / 2)
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # 不存在
        return -1


if __name__ == "__main__":
    # 测试数组
    arr = [2, 3, 4, 5, 9, 6, 2, 10, 40]
    x = 10
    # 函数调用
    result = binarySearch(arr, 1, len(arr), x)
    if result != -1:
        print(result)
        print(arr[result])
    else:
        print("元素不在数组中")
