#mảng đánh dấu
#sử dụng chỉ số của mảng để đánh dấu số lần xuất hiện của phần tử trong mảng a
#chỉ áp dung với phần tử >= 0 và  <= 10^7
a = [5, 1, 2, 1, 2, 4, 1, 5, 5]
cnt = [0] * 10000001
for x in a:
    cnt[x] += 1
l, r = min(a), max(a)
for y in range(l, r + 1):
    if cnt[y] > 0:
        print(y, cnt[y]) #in theo thứ tự tăng dần của phần tử
print('----------')
for x in a:
    if cnt[x] > 0:
        print(x, cnt[x]) #in theo thứ tự xuất hiện của phần tử trong mảng a
        cnt[x] = 0
#tìm số lượng phần tử khác nhau trong mảng a
cnt = [0] * 10000001
l, r = min(a), max(a)
for x in a:
    cnt[x] = 1

# Count unique elements
unique_count = sum(cnt[l:r+1])
print(f"Số phần tử khác nhau trong mảng: {unique_count}")