# -*- coding: utf-8 -*-
"""
有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走
请设计一个算法，计算小团有多少种走法，给定两个正整数int x,int y,请返回小团的走法数目
"""
"""
输入描述：
输入包括一行,逗号隔开的两个正整数x和y,取值范围[1,10]
输出描述：
输出包括一行，走法数目
"""
#使用动态规划法:递推方程为d[i][j]=d[i-1][j]+d[i][j-1]
x,y = map(int,input().split(' '))
d = [[0]*(y+1) for i in range(x+1)]
d[0][0]=0
for i in range(x+1):
    d[i][0]=i
for j in range(y+1):
    d[0][j]=j
for i in range(1,x+1):
    for j in range(1,y+1):
        d[i][j]=d[i-1][j]+d[i][j-1]
print(d[-1][-1])