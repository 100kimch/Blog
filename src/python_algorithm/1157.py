word = str(input()).casefold()
data = {}

for w in word:
    try:
        data[w] += 1
    except KeyError:
        data[w] = 1

largest, ret = max(data.values()), None

for key in data:
    if largest == data[key]:
        if ret is None:
            ret = key
        else:
            ret = '?'
            break

print(ret.capitalize())
