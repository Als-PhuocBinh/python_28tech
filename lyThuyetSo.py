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
#kiểm tra số nguyên tố
def prime(n):
    can = math.isqrt(n)
    if n < 2: return False
    for i in range(2, can + 1):
        if n % i == 0: return False
    return True
#phân tích thừa số nguyên tố
def phanTich(n):
    if n == 1: 
        print(n)
        return
    i = 2
    while i*i <= n:
        if n % i == 0:
            while(n % i == 0):
                print(i, end = ' ')
                n //= i
        i += 1
    #n là số nguyên tố     
    if n > 1: #tinh tế vch =))
        print(n)
#kiểm tra số chính phương
def square(n):
    can = math.isqrt(n)
    return can * can == n   
#ước chung lớn nhất
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)
#kiểm tra số fibo
def fibo1(n):
    f0, f1 = 0, 1
    if n < 0: return False
    if n == 0 or n == 1: return True
    while True:
        fn = f0 + f1
        f0, f1 = f1, fn
        if fn == n: return True
        if fn > n: return False     
#in ra n số file đầu tiên
def fibo2(n):
    if n == 1: print(0)
    else:
        print('0 1', end = ' ')
        f0, f1 = 0, 1
        for i in range(2, n):
            fn = f0 + f1
            print(fn, end = ' ')
            f0, f1 = f1, fn
#in ra số filo thứ n
def fibo3(n):
    if n == 0 or n == 1:
        return n
    f0, f1 = 0, 1
    for i in range(2, n+1):
        fn = f0 + f1
        f0, f1 = f1, fn
    return fn
#kiểm tra số fibo bằng tính chất
def checkFibo(n):
    return square(5*n*n + 4) or square(5*n*n - 4)
#số thuận nghịch/ parindrome
def parindrome(n):
    tmp = n
    so = 0
    while tmp != 0:
        so = so * 10 + tmp % 10
        tmp //= 10
    return so == n
#số hoàn hảo (tổng các ước nhỏ hơn nó bằng chính nó)
def perfectNumber(n):
    res = 1
    for i in range(2, math.isqrt(n)+1): #-> số rất lớn thì căn của nó của lớn
        if n % i == 0:
            res += i
            if i != n // i:
                res += n // i
    return res == n
#định lý euclid-euler
#nếu p là số nguyên tố và 2^p - 1 cx nguyên tố => (2^p - 1) * 2^(p-1) là số hoàn hảo
def perfect(n):
    for p in range(2, 33):
        if prime(p) and prime(2**p - 1):
            res = (2**p - 1) * 2**(p - 1)
            if res == n: return True
    return False



if __name__ == "__main__":
    n = int(input("Please enter number: "))
    print(perfectNumber(n))
    