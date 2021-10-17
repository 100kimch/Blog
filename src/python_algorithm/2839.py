N = int(input())
a, b = 0, 0

ret = -1
for i in range(N // 5, -1, -1):
    target = N - (i * 5)
    if (target % 3 == 0):
        ret = i + (target // 3)
        break

print(ret)
