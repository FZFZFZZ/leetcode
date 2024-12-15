
'''
Common Approach (Sliding Window):

Use Two Pointers (left and right indices):

Expand right pointer to include more characters until the window includes all needed characters from t.
Once you have all characters of t in the current window, try shrinking it from the left side to find the smallest possible window that still contains all t characters.
Character Counting:

Maintain a frequency count of the characters in t.
Keep track of how many of those required characters have been found in the current window of s.
Result Tracking:

Update your result whenever you find a smaller valid window than what you have recorded so far.
'''

# My Own Attempt

def minWindow(s, t):
    def containsT(l, r):
        check = t[:]
        for char in s[l: r + 1]:
            if char in check:
                pos = check.find(char)
                check = check[:pos] + check[pos + 1:]
        
        return check == ""
    l, r = 0, 0
    resL, resR = 0, 0
    minLen = float("infinity")
    while r < len(s) and l <= r:
        if containsT(l, r):
            while containsT(l, r) and l <= r:
                l += 1
            if r - l + 2 < minLen:
                resL = l - 1
                resR = r 
                minLen = r - l + 2
        r += 1
    return s[resL: resR + 1]

print(minWindow("ADOBECODEBANC", "AABB"))
            
            

# Official answer using dictionary
def minWindow(self, s, t):
    def frequency_map(iterable):
        freq = {}
        for item in iterable:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return freq
    
    # Frequency map of characters in t
    t_freq = frequency_map(t)
    
    # Number of unique characters in t that need to be present in the window
    required = len(t_freq)
    
    # Frequency map of characters in the current window
    window_freq = {}
    
    # 'formed' tracks how many distinct characters in the window 
    # match the required frequency from t_freq
    formed = 0
    
    l = 0
    min_len = float("inf")
    res = (0, 0)
    
    # Expand the window using the right pointer
    for r in range(len(s)):
        char = s[r]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        # If the frequency of the current char matches the required frequency in t
        # increase 'formed'
        if char in t_freq and window_freq[char] == t_freq[char]:
            formed += 1
        
        # Once all required chars are matched, try shrinking from the left
        while formed == required:
            # Update the result if this window is smaller than the previously best one
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                res = (l, r)
            
            left_char = s[l]
            window_freq[left_char] -= 1
            # If this char no longer satisfies the requirement, decrement formed
            if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                formed -= 1
            
            l += 1  # Contract the window from the left
    
    # If we never found a valid window, return ""
    if min_len == float("inf"):
        return ""
    
    return s[res[0]:res[1] + 1]