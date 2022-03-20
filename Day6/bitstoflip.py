def countBits(n):
    count = 0
    while n:
        count += n &1
        n >>=1
    return count


def KeepCount(a, b):
    return countBits(a^b)

a = 10
b = 20

print(KeepCount(a, b))