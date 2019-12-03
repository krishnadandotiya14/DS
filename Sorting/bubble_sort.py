# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:40:23 201
@author: kdandotiya

This python file is the implementation of BUBBLE SORT

"""

l = [7,4,5,3,5,4,3,2,5,7,3,2,1,0]
#l = [1,4,3,6,2]

def swap_two_num(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    

def bubble_sort(arr):
    for i in range(len(arr)):
        j = 0
        while j < len(arr) - 1:
            if arr[j] > arr[j+1]:
                swap_two_num(arr,j,j+1)
            j += 1
        #print(arr)
    return arr


result = bubble_sort(l)
print(result)
