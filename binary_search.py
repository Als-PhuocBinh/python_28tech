def binarySearch(a, value):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == value: return True
        elif a[m] > value:
            r = m - 1
        else: l = m + 1
    return False

def binarySearchRecursion(a, l, r, value):
    if l > r: return False
    m = (l + r) // 2
    if a[m] == value: return True
    elif a[m] > value: return binarySearchRecursion(a, l, m-1, value)
    else: return binarySearchRecursion(a, m+1, r, value)

#tìm vị trí xuất hiện đầu tiên của phần tử có giá trị x trong mảng đã sắp tăng dần
def first_pos(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m - 1
            if a[m] == x:
                pos = m
    return pos

#tìm vị trí xuất hiện cuối cùng của phần tử có giá trị x trong mảng đã sắp tăng dần
def last_pos(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] > x:
            r = m - 1
        else:
            l = m + 1
            if a[m] == x:
                pos = m
    return pos

#tìm vị trí xuất hiện đầu tiên của phần tử có giá trị >= x trong mảng đã sắp tăng dần
def funct1(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] < x:
            l = m = 1
        else:
            r = m - 1
            pos = m
    return pos

#tìm vị trí xuất hiện đầu tiên của phần tử có giá trị > x trong mảng đã sắp tăng dần
def funct2(a, l, r, x):
    pos = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m - 1
            pos = m
    return pos
            
