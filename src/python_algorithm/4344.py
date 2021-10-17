N = int(input())

for i in range(N):
    n, *scores = map(int, input().split())
    avg, ret = sum(scores) / n, 0
    for j in scores:
        ret += 1 if j > avg else 0
    print('%.3f%%' % (ret / n * 100))
