def convert(s, numRows):
    res = []
    for i in range(numRows):
        res.append("")
    
    grp = numRows * 2 - 2
    if grp == 0:
        return s
    for i in range(len(s)):
        modulo = i % grp
        index = int(- abs(modulo - numRows + 1) + numRows - 1)
        res[index] = res[index] + s[i]

    output = "".join(res)
    return output


print(convert("A", 1))
