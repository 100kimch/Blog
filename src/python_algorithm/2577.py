A = int(input())
B = int(input())
C = int(input())
digits = [0] * 10

for digit in str(A * B * C):
    digits[int(digit)] += 1

print('\n'.join(str(x) for x in digits))
