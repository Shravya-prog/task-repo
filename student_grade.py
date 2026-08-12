# Student Grade Calculator

print("===================================")
print("       STUDENT GRADE CALCULATOR")
print("===================================")

name = input("Enter student name: ")

print("\nEnter marks for 5 subjects")

maths = float(input("Mathematics: "))
python = float(input("Python: "))
dbms = float(input("DBMS: "))
os = float(input("Operating System: "))
cn = float(input("Computer Networks: "))

total = maths + python + dbms + os + cn
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===================================")
print("          STUDENT RESULT")
print("===================================")

print("Student Name :", name)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)

if grade == "F":
    print("Result       : FAIL")
else:
    print("Result       : PASS")

print("===================================")