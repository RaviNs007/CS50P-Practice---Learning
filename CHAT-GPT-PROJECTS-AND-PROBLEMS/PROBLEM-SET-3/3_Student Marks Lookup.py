marks = {
    "RAVI": 85,
    "AMIT": 72,
    "SITA": 91
}
student = input('Enter student name: ').strip().upper()
if student in marks:
    print(f"{student} scored {marks[student]}")
else:
    print("Student not found")