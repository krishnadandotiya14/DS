my_str = "aabacbebebe"
k = 3

def longest_substring_k_repeated_char(my_str,k):
    chmap = {}
    out = ''
    i,j=0,0
    while j<len(my_str):
        key = my_str[j]
        if key in chmap:
            chmap[key] += 1
        else:
            chmap[key] = 1

        if len(chmap) < k:
            j += 1

        elif len(chmap) == k:
            if j-i+1 > len(out):
                out = my_str[i:j+1]
            j += 1

        elif len(chmap) > k:
            while len(chmap) > k:
                if my_str[i] in chmap:
                    chmap[my_str[i]] -= 1
                    if chmap[my_str[i]] == 0:
                        del chmap[my_str[i]]       # Remove that key
                i += 1
            j += 1
    return out

print(longest_substring_k_repeated_char(my_str,k))