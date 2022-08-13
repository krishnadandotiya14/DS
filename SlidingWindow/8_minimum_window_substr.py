import sys

mystr = "timetopractice"
sstr = "toc"

# out = toprac || opract

def minimum_window_substr(mystr, sstr):
    chmap = {}
    for i in sstr:
        if i in chmap:
            chmap[i] += 1
        else:
            chmap[i] = 1
    count = len(chmap)
    out = []
    out_len = sys.maxsize
    i, j = 0, 0
    while j < len(mystr):
        ele = mystr[j]
        if ele in chmap:
            chmap[ele] -= 1
            if chmap[ele] == 0:
                count -= 1

        if count == 0:
            if j-i+1 < out_len:
                out_len = j-i+1
                out = mystr[i:j+1]
            while count == 0:
                if mystr[i] in chmap:
                    chmap[mystr[i]] += 1
                    if chmap[mystr[i]] > 0:
                        count += 1
                i += 1
        j += 1
    print(out)

minimum_window_substr(mystr, sstr)


