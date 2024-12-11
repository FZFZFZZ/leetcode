def reverse(x):
    bound = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
    split = []
    sign = 1
    if x < 0:
        x = -x
        sign = -1
    while (x != 0):
        split.append(x % 10)
        x = x // 10
    length = len(split)
    if length > 10:
        return 0
    elif length <= 9:
        res = 0
        for items in split:
            res += items * (10 ** (length - 1))
            length -= 1
        return sign * res
    else:  
        for i in range(length):
            if split[i] < bound[i]:
                break
            if split[i] > bound[i]:
                return 0
        res = 0   
        for items in split:
            res += items * (10 ** (length - 1))
            length -= 1
        return sign * res

print(reverse(563847412))