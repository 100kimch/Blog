counts = [-1] * 26
word = input()[::-1]
L = len(word)

for i in range(L):
    counts[ord(word[i]) - 97] = L - i - 1

print(" ".join(map(str, counts)))
