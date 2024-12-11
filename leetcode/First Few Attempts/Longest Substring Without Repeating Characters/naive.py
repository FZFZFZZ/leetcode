def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    curr = 0
    curr_str = ""
    for char in s:
        if char in curr_str:
            pos = curr_str.find(char)
            curr_str = curr_str[pos + 1:] + char
            curr -= pos
        else:
            curr_str += char
            curr += 1
        
        res = curr if curr > res else res
    return res
    
print(lengthOfLongestSubstring("aab"))

## This naive attempt is efficient enough.