arr = [1,3,-1,-3,-5,3,6,7]
k = 3
# out = [3,3,5,5,6,7]

'''
arr = [1,3,-1,-3,-5,3,6,7]
# out = [3, 3, -1, 3, 6, 7]
'''

def maximum_of_subarr_sizek(arr,k):
    out = []
    submax = arr[0]
    auxarr = []  # Its front will always be highest || using it like a double ended queue
    i,j = 0,0
    while j < len(arr):
        if arr[j] >= submax:  # If any greater found, remove all of its left in auxarr
            submax = arr[j]
            while len(auxarr):
                auxarr.pop()
        auxarr.append(arr[j])

        if j-i+1 < k:   j += 1

        elif j-i+1 == k:
            out.append(auxarr[0])           # auxarr front is always having maxx
            if auxarr[0] == arr[i]:         # ith element is max
                auxarr.pop(0)
                submax = max(auxarr)        # Find max in remaining auxarr
                while auxarr[0] != submax:  # Remove any smaller elements left on submax in auxarr
                    auxarr.pop(0)
            i += 1
            j += 1
    print(out)

maximum_of_subarr_sizek(arr,k)