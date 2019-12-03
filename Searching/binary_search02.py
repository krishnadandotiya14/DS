# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:18:57 2019

@author: kdandotiya
"""

# This is a binary Search Code in PY3.7 Using recursion approach

#Input List
#l = [5,3,7,2,38,9,6,75,67,7,36,83,26,76,82,83,82,57]

l = [6,5,4,3,2,1]
#Binary Search works for Sorted Input list
ls = sorted(l)

def binary_search_recursion(arr,item):

    if len(arr) == 0:
        return False
    else:
        mid = (len(arr))//2
        print("arr -->",arr)
        print("mid index -->",mid)
        if arr[mid] == item:
            return True
        
        else:        
            if arr[mid] > item:
                 return binary_search_recursion(arr[:mid],item)
            else:
                 return binary_search_recursion(arr[mid+1:],item)


print("Input List ->",ls)
result = binary_search_recursion(ls,8)
print("Is 8 in input ->",result)
print("====================================")

result = binary_search_recursion(ls,7)
print("Is 7 in input ->",result)
print("====================================")

result = binary_search_recursion(ls,6)
print("Is 6 in input ->",result)
print("====================================")

result = binary_search_recursion(ls,5)
print("Is 5 in input ->",result)
print("====================================")

result = binary_search_recursion(ls,4)
print("Is 4 in input ->",result)
print("====================================")

result = binary_search_recursion(ls,3)
print("Is 3 in input ->",result)
print("====================================")

result = binary_search_recursion(ls,2)
print("Is 2 in input ->",result)
print("====================================")

result = binary_search_recursion(ls,1)
print("Is 1 in input ->",result)
print("====================================")
