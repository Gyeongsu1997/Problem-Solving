k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]
lo = 0
hi = max(lst) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    cnt = 0
    for x in lst:
        cnt += x // mid
    if cnt >= n:
        lo = mid
    else:
        hi = mid
print(lo)
