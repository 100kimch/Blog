N = int(input())

for i in range(N):
    score, ret = 0, 0
    for val in str(input()):
        if (val == 'O'):
            score += 1
            ret += score
        else:
            score = 0
    print(ret)
