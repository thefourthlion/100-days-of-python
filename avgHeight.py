#!/usr/bin/env python3

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
students = 0

for height in student_heights:
    total_height += height
    students += 1

print(round(total_height/students))
