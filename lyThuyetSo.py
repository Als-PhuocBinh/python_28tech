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
        
    
        

if __name__ == "__main__":
    n = int(input("Please enter number: "))
    phanTich(n)