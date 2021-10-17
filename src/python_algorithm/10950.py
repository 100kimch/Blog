num = int(input())
result = []

for i in range(num):
    a, b = map(int, input().split())
    result.append(a + b)

for i in result:
    print(i)
