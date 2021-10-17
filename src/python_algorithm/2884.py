H, M = map(int, input().split())
M -= 45
if (M < 0):
    H = (H - 1) % 24
M %= 60
print(str(H) + ' ' + str(M))
