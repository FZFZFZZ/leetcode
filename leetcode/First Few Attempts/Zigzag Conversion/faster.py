def convert(s, numRows):
    if numRows == 1:
        return s
    
    res = [""] * numRows
    grp = numRows * 2 - 2

    for i in range(len(s)):
        modulo = i % grp
        index = - abs(modulo - numRows + 1) + numRows - 1
        res[index] += s[i]

    return "".join(res)


print(convert("A", 1))

#this version is fast enough
