n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]
schedules.sort(key=lambda x : (x[1], x[0]))
end_time = 0
cnt = 0
for i in range(n):
    if schedules[i][0] >= end_time:
        end_time = schedules[i][1]
        cnt += 1
print(cnt)