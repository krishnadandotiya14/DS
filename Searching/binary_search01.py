# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:18:57 2019

@author: kdandotiya
"""

# This is a binary Search Code in PY3.7 (not recursive approach)

#Input List
l = [5,3,7,2,38,9,6,75,67,7,36,83,26,76,82,83,82,57]

#Binary Search works for Sorted Input list
ls = sorted(l)

def binary_search(arr,item):
    len_arr = len(arr)
    first = 0
    last = len_arr - 1
    found = False
    
    while first <= last:
        mid = (first + last)//2
        if arr[mid] == item:
            found = True
            return found
        else:
            if arr[mid] > item:
                last = mid - 1
            else:
                first = mid + 1
    return found

print("Input List ->",ls)

result = binary_search(ls,80)
print("Is 80 in input ->",result)

result = binary_search(ls,38)
print("Is 38 in input ->",result)