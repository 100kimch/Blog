num = int(input())
result = num
cnt = 0

while (num != result) or (cnt == 0):
    result = (((result // 10 % 10 + result % 10) % 10) + (result % 10 * 10))
    cnt += 1
print(cnt)
