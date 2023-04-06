n = int(input())
haystack = sorted(list(map(int, input().split())))
m = int(input())
needle = list(map(int, input().split()))
for x in needle:
    lo = 0
    hi = n - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if haystack[mid] <= x:
            lo = mid
        else:
            hi = mid
    if haystack[lo] == x or haystack[hi] == x:
        print(1)
    else:
        print(0)