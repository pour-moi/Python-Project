student_heights = input("Input a list of student heihgts ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0

for average_height in student_heights:
    sum += average_height

average = sum / len(student_heights)

print(round(average))