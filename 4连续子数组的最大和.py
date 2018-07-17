# -*- coding: utf-8 -*-
"""
一个数组有N个元素，求连续子数组的最大和
问题描述：
一个数组有N个元素，求连续子数组的最大和。例如[-1,2,1]的最大连续子数组为[2,1]，和为3
输入描述：
输入为两行，第一行一个整数N，表示一共有N个元素；第二行为N个数，即每个元素，元素之间以空格分隔
输出描述：
所有连续子数组中和最大的值
"""
#采用动态规划的方法
#记dp[i]为以第i个元素结尾的连续子数组的最大和，因此dp[i]=max{dp[i-1]+a[i],a[i]}
N = int(input())
line = input()
line = list(map(int,line.split(' ')))

d = [0]*N
d[0]=line[0]
for i in range(1,N):
    d[i]=max(d[i-1]+line[i],line[i])
print(max(d))
