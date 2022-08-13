my_str = "forxxorfxdofr"
pattern = "for"

# output = [for,orf,ofr] = 3
def count_occurance_anagram(my_str,pattern):
    out = []
    i,j = 0,0
    chmap = {}
    for ch in pattern:
        if ch not in chmap:
            chmap[ch] = 1
        else:
            chmap[ch] += 1
    count = len(chmap)

    while j < len(my_str):
        curr = my_str[j]
        if curr in chmap:
            chmap[curr] -= 1
            if chmap[curr] == 0:
                count -= 1

        if j-i+1 < len(pattern):   j += 1

        elif j-i+1 == len(pattern):
            if count == 0:     # All characters found
                out.append(my_str[i:j+1])
            if my_str[i] in chmap:
                chmap[my_str[i]] += 1
                count += 1
            i += 1
            j += 1
    print(my_str,pattern,out,len(out))

count_occurance_anagram(my_str,pattern)




