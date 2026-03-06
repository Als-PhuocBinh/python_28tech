#cho mảng a có n phần tử, yêu cầu tính tổng các phần tử từ chỉ số l đến r
#chú ý khi left = 0: F[r]
#F[r] - F[l-1]
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    l, r = map(int, input().split())
    F = [0] * n
    F[0] = a[0]
    for i in range(1, n):
        F[i] = F[i-1] + a[i]
    if l == 0:
        print(F[r])
    else:
        print(F[r] - F[l-1])
    #có thể thực hiện rất nhiều truy vấn với O(1)
    
        
    
   
        