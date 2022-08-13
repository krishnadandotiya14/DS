arr = [12,-1,-7,8,-15,30,16,28]
k = 3
# if no negative , put zero in out array
# output = [-1,-1,-7,-15,-15,0]

def first_negative_everywindowsize_k(arr,k):
    if len(arr) < k:
        return 0
    aux_arr = []    # To hold negative numbers
    out = []        # Output array
    i,j = 0,0
    while j < len(arr):
        if arr[j] < 0 :
            aux_arr.append(arr[j])
        if j-i+1 < k:   j += 1

        elif j-i+1 == k:            # Check for ans and move i
            if len(aux_arr) > 0:    # found some negative
                out.append(aux_arr[0])
            else:
                out.append(0)
            if len(aux_arr) > 0 and aux_arr[0] == arr[i]:  # i has negative. pls remove
                aux_arr.pop(0)
            i += 1
            j += 1
    return out

print(first_negative_everywindowsize_k(arr,k))