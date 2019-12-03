# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:58:31 2019
@author: kdandotiya

This python file shows implementation of SELECTION SORT
"""

l = [7,4,5,3,5,4,3,2,5,7,3,2,1,0]
#l = [1,4,3,6,2]


def swap_two_num(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
  

def selection_sort(arr):
    for i in range(len(arr) -1):
        j = i + 1
        while j < (len(arr)) :
            if arr[i] > arr[j]:
                swap_two_num(arr,i,j)
            else:
                pass
            j += 1
    return arr


result = selection_sort(l)
print(result)