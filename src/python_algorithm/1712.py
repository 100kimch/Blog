A, B, C = map(int, input().split())
try:
    ret = int(A / (C - B)) + 1
    print(ret if ret > 0 else -1)
except ZeroDivisionError:
    print(-1)
