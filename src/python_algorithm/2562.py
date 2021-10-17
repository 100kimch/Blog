data = []
largest, largest_num = 0, 0

for i in range(9):
    n = int(input())
    data.append(n)
    if largest < n:
        largest = n
        largest_num = i + 1

print(largest)
print(largest_num)