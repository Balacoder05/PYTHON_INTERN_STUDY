marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / n

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print("Average:", average)
print("Grade:", grade)