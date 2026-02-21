import math

#đếm tổng ước của một số
def demUoc(n):
    cnt = 0
    can = math.isqrt(n)
    for i in range (1, can + 1):
        if n % i == 0:
            cnt += 1
    if can * can == n:
        return 2*cnt - 1
    return 2*cnt
#tính tổng ước của một số
def tongUoc(n):
    s = 0
    can = math.isqrt(n)
    for i in range (1, can + 1):
        if n % i == 0:
            s += i + n // i
    if can * can == n:
        return s - can
    return s


if __name__ == "__main__":
    n = int(input("Please enter number: "))
    print(demUoc(n))
    print(tongUoc(n))