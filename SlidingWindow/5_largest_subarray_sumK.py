arr = [4,1,1,1,2,3,5]
sum = 5

def largest_subarray_sumK(arr,sum):
    out = []
    temp = 0
    i,j = 0,0
    while j < len(arr):
        temp += arr[j]
        #print("-",temp)

        if temp < sum:
            j += 1

        elif temp == sum:
            #print(arr[i:j+1])
            if j-i+1 > len(out):
                out = arr[i:j+1]
            j += 1

        elif temp > sum:
            while temp > sum:
                temp = temp - arr[i]
                #print("TEMP-- ",temp)
                i += 1
            j += 1
    return out

print(largest_subarray_sumK(arr,sum))