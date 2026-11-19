students = {
   "Stacy": 85,
   "Alyssa": 90,
   "Jenny": 78,
   "Simon": 88,
   "Marcy": 92,
   "Teddy": 80,
}
print ("Student Names\tGrades:")
for name, grade in students.items():
    print(name, "\t\t", grade)

total = sum(students.values())
average = total / len(students)
print("Average Grade:", average)