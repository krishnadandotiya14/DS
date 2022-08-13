arr = [0,1,0,1,0,1,1,1,0]
k = 2

# output = 7 = [1,0,1,0,1,1,1]

def longest_1_subarray_replacing_k_zero(arr,k):
    zero_count = 0
    ans = []
    i,j = 0,0
    while j < len(arr):
        if arr[j] == 0:
            zero_count += 1

        if zero_count < k:
            j += 1

        elif zero_count == k:       # ans
            if len(ans) < j-i+1:    # Bigger arry found
                ans = arr[i:j+1]
            j += 1

        elif zero_count > k:
            while zero_count > k:
                if arr[i] == 0:
                    zero_count -= 1
                i += 1
            j += 1
    return ans


print(longest_1_subarray_replacing_k_zero(arr,k))