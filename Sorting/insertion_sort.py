# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:19:53 2019
@author: kdandotiya

This python file shows implementation of INSERTION SORT
"""

l = [7,4,5,3,5,4,3,2,5,7,3,2,1,0]
#l = [1,4,3,6,2]


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]        #Select first Unsorted Element
        j = i - 1
        while (j >=0 and arr[j] > key):
            ''' This loop shifts all element to right
            to create position for unsorted element'''
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key      #This inserts unsorted element to its correct position.
    return arr
    

result = insertion_sort(l)
print(result)
