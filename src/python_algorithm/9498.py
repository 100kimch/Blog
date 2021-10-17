a = int(input())
grade = ['A', 'B', 'C', 'D']

if (a == 100):
    print('A')
elif (a >= 60):
    print(grade[(99 - a) // 10])
else:
    print('F')
