name = input("Enter student name: ")

mark1 = int(input("Enter subject 1 marks: "))
mark2 = int(input("Enter subject 2 marks: "))
mark3 = int(input("Enter subject 3 marks: "))

total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total:", total, "/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)