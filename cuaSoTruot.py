#tìm tổng dãy con liên tiếp cỡ k của a[n]
if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    tong = sum(a[:k])
    print(tong, end = ' ')
    for i in range(1, n-k+1):
        tong = tong - a[i-1] + a[i+k-1]
        print(tong, end = ' ')
    