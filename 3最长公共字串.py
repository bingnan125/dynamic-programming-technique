# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 21:30:24 2018

@author: asus
"""

#最长公共子串
def findLongest(A,B):    
    #新建一个m行n列的矩阵     
    n=len(A)
    m=len(B)
    matrix = [0] * m * n    
    #1、矩阵的第一行，即matrix[0][i]，代表str1[0]与str2[0...n]的最长公共子串.    
    # str2[0]只有一个字符，所以matrix[i][0]最大为1    
    for i in range(n):    
        if A[i] == B[0]:    
            matrix[i] = 1    
    #2、矩阵的第一列，matrix[i][0]最大为1    
    for i in range(m):    
        if B[i] == A[0]:    
            matrix[i*n] = 1    
    #3、其他位置    
    long_num = max(matrix)
    
    for i in range(1,m):    
        for j in range(1,n):    
            if B[i] == A[j]:    
                matrix[i*n+j] = matrix[(i-1)*n+j-1]+1    
                if long_num<matrix[i*n+j]:    
                    long_num = matrix[i*n+j]    
    return long_num

A = 'xy'
B = 'azm'
findLongest(A,B)
  

def findLongSeq(A,B):
    import numpy as np
    n=len(A)
    m=len(B)
    mat = np.zeros([n,m],dtype=int)
    #矩阵的第一行代表A[0]与B的最长公共子序列
    for i in range(m):
        if A[0]==B[i]:
            for j in range(i,m):
                mat[0,j]=1
    
    #矩阵的第一行代表B[0]与A的最长公共子序列
    for i in range(n):
        if B[0]==A[i]:
            for j in range(i,n):
                mat[j,0]=1
    long_num = np.argmax(mat)
    for i in range(1,m):
        for j in range(1,n):
            if A[j]==B[i]:
                mat[j,i]=mat[j-1,i-1]+1
            if long_num<mat[j,i]:
                long_num = mat[j,i]
    return long_num
A = 'xyxzyxyzzy'
B = 'xzyzxyzxyzxy'
findLongSeq(A,B)
