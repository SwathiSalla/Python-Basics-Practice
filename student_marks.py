students=[]
for i in range(3):
    name=input("Enter student name: ")
    marks=int(input("Enter student marks: "))
    students.append([name, marks])
print("Student details:")
print("----------------")
for student in students:
    print("Name:", student[0])
    print("Marks:", student[1])
    if student[1] >= 90:
        print("Grade: A")
    elif student[1] >= 80:
        print("Grade: B")
    elif student[1] >= 70:
        print("Grade: C")
    elif student[1] >= 40:
        print("Grade: D")
    else:
        print("Grade: F")
    print("----------------")
    