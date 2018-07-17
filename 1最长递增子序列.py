# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:19:32 2018

@author: asus
"""

#最长递增子序列(可以归为求最长公共子序列)
"""不太理解
def findLongest(arr):
    n = len(arr)
    m = [0]*n
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            if arr[i] < arr[j] and m[i] <= m[j]:
                m[i] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result
 
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(findLongest(arr))
"""
def findLongest(arr):
    max_sum,cur_sum= -0xffffff,0
    for val in arr:
        if cur_sum<=0:
            cur_sum=val
        else:
            cur_sum +=val
        if cur_sum>max_sum:
            max_sum = cur_sum
    return max_sum
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(findLongest(arr))

#最长公共子序列  
def LCS(str1,str2):  
    #字符串为空则返回  
    if str1=='' or str2=='':  
        return  ''  
    #字符串长度  
    m=len(str1)  
    n=len(str2)  
    #初始化lcs  
    lcs=[[0] for i in range(0,m+1)]  
    lcs[0]=[0 for j in range(0,n+1)]  
    #  
    for i in range(m):  
        for j in range(n):  
            lcs[i+1].append(lcs[i][j]+1 if str1[i]==str2[j] else max(lcs[i][j+1],lcs[i+1][j],))  
    #for i in range(m+1):  
        #print lcs[i]  
    i=m-1  
    j=n-1  
    common_substr = u''  
    #回溯得到LCS  
    while True:  
        if i == -1 or j == -1:  
            break  
        if str1[i] == str2[j]:  
            common_substr = u"%s%s" % (str1[i], common_substr)  
            i = i - 1  
            j = j -1  
        else:  
            if lcs[i][j+1] > lcs[i+1][j]:  
                i = i-1  
            else:  
                j = j-1  
    print(common_substr)   
#最长递增子列  
def LIS(list1):
    list2=sorted(list1)#排序  
    #print list1,list2  
    return LCS(list1,list2)
LCS("GCGCAATG","GCCCTAGCG")  
LIS([2, 1, 6, 3, 5, 4, 8, 7, 9])