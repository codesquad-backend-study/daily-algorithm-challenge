student_list = []
for _ in range(int(input())):
    student_list.append(input().split())

student_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in student_list:
    print(student[0])
