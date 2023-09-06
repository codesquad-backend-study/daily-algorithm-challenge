# 국영수
import sys

N = int(sys.stdin.readline().strip())
students = [sys.stdin.readline().strip().split() for _ in range(N)]

students.sort(key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

print(*[student[0] for student in students], sep="\n")
