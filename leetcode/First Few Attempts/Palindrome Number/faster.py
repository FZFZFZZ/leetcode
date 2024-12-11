class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and x < 10:
            return True  
        elif x < 0 or x % 10 == 0:
            return False

        origin = x
        res = 0
        while True:
            if x == res or x == res // 10:
                return True
            if res > x:
                return False
            digit = x % 10
            x //= 10
            res = res * 10 + digit

# this solution is fast enough
