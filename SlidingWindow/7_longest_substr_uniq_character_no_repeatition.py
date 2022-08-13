my_str = "pwwkew"
# out = wke

def longest_substring_uniq_char(my_str):
    chmap = {}
    out = ''
    i,j=0,0
    while j<len(my_str):
        key = my_str[j]
        if key in chmap:
            chmap[key] += 1
        else:
            chmap[key] = 1

        if len(chmap) == j-i+1:
            print("Substr: -> ",my_str[i:j+1])
            if j-i+1 > len(out):
                out = my_str[i:j+1]
            j += 1

        elif len(chmap) < j-i+1:
            while len(chmap) < j-i+1:
                if my_str[i] in chmap:
                    chmap[my_str[i]] -= 1
                    if chmap[my_str[i]] == 0:
                        del chmap[my_str[i]]       # Remove that key
                i += 1
            j += 1
    return out

print(longest_substring_uniq_char(my_str))