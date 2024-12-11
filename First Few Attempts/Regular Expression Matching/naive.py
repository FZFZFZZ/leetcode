def isMatch(s, p):
    print(s)
    print(p)
    def compare(char_s, char_p):
        if char_p == '.':
            return True
        else:
            return char_s == char_p
    
    len_s = len(s)
    len_p = len(p)
    i = 0
    j = 0
    while i < len_s and j < len_p:
        if j + 1 < len(p) and p[j + 1] == '*':
            return isMatch(s[i:], p[j] + p[j+2:]) or isMatch(s[i:], p[j] + p[j] + p[j+2:])

        elif not compare(s[i], p[j]):
            return False
        
        i += 1
        j += 1

    if p == "" and s != "":
        return False
    elif s == "" and p != "":
        return False
    elif s == "" and p == "":
        return True
    elif compare(s[i-1], p[j-1]) and len_s - i == len_p - j:
        return True
    else:
        return False
    



print(isMatch("aab", "c*a*b"))


# partial solution
