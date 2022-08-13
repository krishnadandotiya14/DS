import sys
arr = [2,5,1,8,2,9,3,1]
k = 3
# output =  [8,2,9] = 19 ANS

def maximum_sum_subarray_sizek(arr,k):

    if len(arr) < k:
        return None
    i,j = 0,0
    temp = 0
    subarr = []
    max_sum = -sys.maxsize+1     # - infinite
    while j < len(arr):
        temp = temp + arr[j]
        if j-i+1 < k:
            j += 1
        elif j-i+1 == k:        # got subarray of size k . Check for answer
            if temp > max_sum:
                max_sum = temp
                subarr = arr[i:j+1]
            # adjust i and temp for next window
            temp = temp - arr[i]
            i += 1
            j += 1
    print(arr," -> ",max_sum,subarr)

maximum_sum_subarray_sizek(arr,k)