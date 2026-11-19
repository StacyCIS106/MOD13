students = {
   "Stacy": [85, 90, 70],
   "Alyssa": [90, 85, 88],
   "Jenny": [78, 82, 75],
   "Simon": [88, 92, 85],
   "Marcy": [92, 95, 90],
   "Teddy": [80, 85, 82],
}
print ("Student Names\tGrades\t\tAverage:")

def calculate_average(students):
    averages = []
    for i in range(3):
        total = 0 
        for grade in students.values():
            total += grade[i]
        averages.append(total / len(students))
    return averages

for name, grade in students.items():
    student_average = sum(grade) / len(grade)
    print(name, "\t\t", grade, "\t", format(student_average, ".2f"))

class_average = calculate_average(students)
print("Student Average:", format(student_average, ".2f"))

for i in range(3):
    print("Grade", i + 1, "Average:", format(class_average[i], ".2f"))

