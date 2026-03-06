if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    min_val, cnt = a[0], 1
    for x in a:
        if x < min_val:
            min_val = x
            cnt = 1
        elif x == min_val:
            cnt += 1
    print(min_val, cnt, sep = '\n')

        
        