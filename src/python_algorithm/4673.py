N = 10000
numbers = [False] * (N - 1)


def get_dr_number(num: int) -> int:
    """D.R. Kaprekar permutation"""
    ret = num
    for i in str(num):
        ret += int(i)
    return ret


for i in range(N):
    j = get_dr_number(i + 1)
    if j < N:
        numbers[j - 1] = True

print(
    "\n".join(
        list(map(lambda x: str(x[0] + 1), filter(lambda x: x[1] is False, enumerate(numbers))))
    )
)
