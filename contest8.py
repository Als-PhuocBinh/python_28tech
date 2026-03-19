from functools import cmp_to_key
#các số khác nhau trong mảng
#có thể dùng mảng đánh dâu nhưng chỉ phù hợp với dữ liệu nhỏ và không âm
def func1(a):  # a là mảng đã được sort
    dem = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            dem += 1
    return dem

#sắp xếp mảng a theo thứ tự giá trị tuyệt đối tăng dần, nếu có cùng giá trị tuyệt đối thì số
#nào xuất hiện trước thì in trước
def func2(a):
    a.sort(key = abs)

#sắp xếp theo tổng chữ số tăng dần, nếu cùng thì số nhỏ hơn in trước
def sum_digit(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res
def cmp(a, b):
    if sum_digit(a) != sum_digit(b):
        return sum_digit(a) - sum_digit(b)
    else:
        return a - b
    
#tìm độ chênh lệch nhỏ nhất giữa 2 phần từ a[i], a[j] với i != j
def func3(a):
    #a đã sort
    res = 1e9
    for i in range(1, len(a)):
        if a[i] - a[i-1] < res:#
            res = a[i] - a[i-1]  #res = min(res, a[i] - a[i-1])
    return res

#số xuất hiện nhiều nhất trong mảng, nếu cùng tần suất thì lấy số nhỏ
def func4(a):
    # a đã sort
    a.append(10**18)
    ans, cnt, res = 1, 1, a[0]
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            if cnt > ans:
                ans = cnt
                res = a[i-1]
            cnt = 1
    return ans, cnt, res

#trộn 2 dãy
def func5(b, n, c, m):
    #b và c đã được sắp xếp tăng dần, n = len(b), m = len(c)
    i, j = 0, 0
    while i < n and j < m:
        if (b[i] <= c[j]):
            print("b", i + 1, sep='', end = ' ')
            i += 1
        else:
            print("c", j + 1, sep='', end = ' ')
            j += 1
    while i < n:
        print("b", i + 1, sep='', end = ' ')
        i += 1
    while j < m:
        print("c", j + 1, sep='', end = ' ')
        j += 1

#1_tìm vị trí xuất hiện đầu tiên của phần tử X trong mảng
def ham1(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            pos = m
            r = m - 1
        elif a[m] < x: l = m + 1
        else: r = m - 1
    return pos

#2_tìm vị trí xuất hiện cuối cùng của phần tử X trong mảng
def ham2(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            pos = m
            l = m + 1
        elif a[m] < x: l = m + 1
        else: r = m - 1
    return pos
#3_tìm vị trí xuất hiện đầu tiên của phần tử >= X
def ham3(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] < x: l = m + 1
        else:
            r = m - 1
            pos = m
    return pos
#4_tìm vị trí xuất hiện đầu tiên của phần tử > X
def ham3(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] <= x: l = m + 1
        else:
            r = m - 1
            pos = m
    return pos
    
#khiêu vũ
def func6(a, n, b, m):
    #a (nam), b(nu) đã sort, ~ merge sort
    i, j, cnt = 0, 0, 0
    while i < n and j < m:
        if a[i] - b[j] > 0:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1
    return cnt

#xếp gạch - KHÓ--------------------------
def func7(a, n):
    res = 1
    a.sort(reverse = True)
    capacity = a[0]
    for i in range(1, n):
        if capacity <= 0:
            break
        else:
            res += 1
            capacity = min(capacity-1, a[i])

#cặp số có tổng bằng k
def binarySearchIndexMin(a, x, l, r):
    pos = -1
    while l <= r:
        m = (l + r)//2
        if a[m] == x:
            pos = m
            r = m - 1
        elif a[m] < x: l = m + 1
        else: r = m - 1
    return pos
def binarySearchIndexMax(a, x, l, r):
    pos = -1
    while l <= r:
        m = (l + r)//2
        if a[m] == x:
            pos = m
            l = m + 1
        elif a[m] < x: l = m + 1
        else: r = m - 1
    return pos
def countNumber(a, x, l, r):
    min_index = binarySearchIndexMin(a, x, l, r)
    max_index = binarySearchIndexMax(a, x, l, r)
    if min_index == -1: return 0
    return max_index - min_index + 1

def capSo(a, n, k):
    #a đã sort, n là số lượng phần tử, k là tổng cặp số  
    cnt = 0
    for i in range(n):
        cnt += countNumber(a, k - a[i], i+1, n - 1)
    return cnt

#điền số còn thiếu từ khoảng min đến max
def dienSo(a, n):
    # a.sort()
    res = 0
    for i in range(1, n):
        res += max(0, a[i] - 1 - a[i-1])
    return res

#tìm kiếm cặp có số hiệu là X
def binarySearchReverse(a, x, l, r):
    while l <= r:
        m = (l + r) // 2
        if a[m] == x: return True
        elif a[m] > x: l = m + 1
        else: r = m - 1
    return False
def hieuCapSo(a, x, n):
    a.sort(reverse = True)
    #x là hiệu cặp sô
    for i in range(n-1):
        if binarySearchReverse(a, a[i] - x, i+1, n - 1): return True
    return False 

#đèn lồng
def denLong(a, n, l):
    a.sort()
    d = max(a[0], l - a[-1])
    for i in range(1, n):
        d = max((a[i] - a[i-1])/2, d)
    return d

#dragon
def dragon(a, s, n):
    a.sort(key = lambda x : (x[0], x[1]))
    for i in range(n):
        if s - a[i][0] > 0:
            s = s +a[i][1]
        else:
            return False
    return True

#xếp trẻ 
def xepTre(a, n, x):
    res = 0
    a.sort()
    i, j = 0, n-1
    while i <= j:
        if a[j] + a[i] > x:
            j -= 1
            res += 1
        else:
            j -=1
            i +=1
            res += 1
    return res

#biểu thức lớn nhất
def bieuThuc(a, n, k):
    #k: +, (n- k): -
    res = a[0]
    tmp = a[1:]
    tmp.sort()
    return res - sum(tmp[:n - k - 1]) + sum(tmp[n-k-1:])







if __name__ == '__main__':
    #n = int(input())
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    #a.sort()
    
    

    

