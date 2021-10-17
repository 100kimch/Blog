N = int(input())
scores = list(map(int, input().split()))

largest, total = 0, 0
for i in scores:
    largest = i if largest < i else largest
    total += i

print(total / largest * 100 / N)
