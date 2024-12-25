def isHappy(n):
    visited = {}
    def split_and_sum(n):
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n //= 10
        return sum
    
    while n not in visited:
        print(n)
        print(visited) 
        if n == 1:
            return True
        else:
            visited[n] = True
            n = split_and_sum(n)
    
    return False

print(isHappy(19))