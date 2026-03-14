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
            res = a[i] - a[j]  #res = min(res, a[i] - a[i-1])
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


if __name__ == '__main__':
    a = [2, 3, 5, 4, 9, 3, 2, 3, 2, 5, 2, 10]
    #a.sort(key = cmp_to_key(cmp)) #a.sort(key = lambda x : (sum_digit(x), x))
    a.sort()
    print(func4(a))