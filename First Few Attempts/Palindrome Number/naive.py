def isPalindrome(x):
    if x == 0:
        return True  
    elif x < 0 or x % 10 == 0:
        return False
    
    origin = x
    res = 0
    while x != 0:
        digit = x % 10
        x //= 10
        res *= 10
        res += digit
    
    return res == origin

