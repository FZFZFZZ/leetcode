def mySqrt(x):
    last = 10
    curr = 100
    while (abs(last - curr) > 0.5):
        last = curr
        curr -= curr / 2 - x / (2 * curr)
    return int(curr)

print(mySqrt(6))