n = int(input())

students = []
for _ in range(n):
    inputs = input().split()
    kor, eng, math, = map(int, inputs[1:])

    students.append((inputs[0], kor, eng, math))

students.sort(key=lambda x:(-x[1], x[2], -x[-1], x[0]))

for each in students:
    print(each[0])
