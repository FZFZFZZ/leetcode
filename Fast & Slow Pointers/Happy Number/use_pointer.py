def isHappy(n):
    def split_and_sum(n):
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n //= 10
        return sum
    
    slow = n
    fast = n
    while fast != 1 and slow != 1:
        slow = split_and_sum(slow)
        fast = split_and_sum(split_and_sum(fast))
        if slow == fast and slow != 1:
            return False
    
    return True