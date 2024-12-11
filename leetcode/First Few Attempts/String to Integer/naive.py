def myAtoi(s):
    
    res = 0
    sign = 1
    allspace = True

    for char in s:


        if char == ' ' and allspace:
            continue

        if char == '-' and allspace:
            sign = -1
        elif char == '+' and allspace:
            sign = 1
        elif ord(char) > 57 or ord(char) < 48:
            break
        else:
            res *= 10
            res += int(char)

        if char != ' ':
            allspace = False
    
    if sign * res > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif sign * res < -2 ** 31:
        return -2 ** 31
    else:
        return sign * res

print(int("   -0042"))

# the solution is efficient enough
