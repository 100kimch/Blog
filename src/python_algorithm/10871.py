N, X = map(int, input().split())
arr = [int(i) for i in input().split()]
result = []

for key, val in enumerate(range(N)):
    if arr[key] < X:
        result.append(arr[key])

print(' '.join(map(str, result)))
