counts = [-1] * 26
c = 0
for i in input():
    if counts[ord(i) - 97] == -1:
        counts[ord(i) - 97] = c
    c += 1

print(" ".join(map(str, counts)))
