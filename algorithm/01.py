#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:EnzoLuo

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def twoSum(nums, target):
    rs = []
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[i] + nums[j] == target:
                rs.append(i)
                rs.append(j)
                return rs
    return rs


def main():
    nums = [3, 2, 4]
    rs = twoSum(nums, 6)
    print(rs)


if __name__ == '__main__':
    main()
