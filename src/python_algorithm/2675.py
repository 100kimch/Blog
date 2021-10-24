N = int(input())
for _ in range(N):
    T, S = input().split()
    print("".join([int(T) * s for s in S]))
