def minWindow(s, t):
    dict = {}
    for char in t:
        dict[char] = []
    
    for i in range(len(s)):
        if s[i] in dict:
            dict[s[i]].append(i)
    
    items = list(dict.values())
    res = []
    for i in range(len(items[0])):
        path = [items[0][i]]
        for j in range(1, len(items)):
            test = path[:]
            smallest = float("infinity")
            for k in range(len(items[j])):
                test.append(items[j][k])
                if (max(test) - min(test)) < smallest:
                    smallest = max(test) - min(test)
                    path = test
                test = test[:-1]
        res.append(path)
    
    i = 0
    j = 0
    smallest = float("infinity")
    for path in res:
        if max(path) - min(path) + 1 < smallest:
            i = min(path)
            j = max(path) + 1
            smallest = max(path) - min(path) + 1
    
    return s[i:j]


    
print(minWindow("ADOBECODEBANC", "ABC"))

#partial solution
