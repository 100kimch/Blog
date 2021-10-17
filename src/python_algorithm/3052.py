digits = [0] * 42

for i in range(10):
    digits[int(input()) % 42] = 1

print(sum(digits))
