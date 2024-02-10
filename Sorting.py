def sort_by_name(students):
    return sorted(students, key=lambda x: x[0])

def sort_by_regno(students):
    return sorted(students, key=lambda x: x[1])

def sort_by_cgpa(students):
    return sorted(students, key=lambda x: x[2], reverse=True)

students = []
for i in range(5):
    name = input("Enter name of student {}: ".format(i+1))
    regno = input("Enter regno of student {}: ".format(i+1))
    cgpa = float(input("Enter cgpa of student {}: ".format(i+1)))
    students.append((name, regno, cgpa))

while True:
    print("\nMenu:")
    print("1. Sort by name")
    print("2. Sort by regno")
    print("3. Sort by cgpa")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sorted_students = sort_by_name(students)
        print("\nSorted by name:")
        for student in sorted_students:
            print(student)
    elif choice == 2:
        sorted_students = sort_by_regno(students)
        print("\nSorted by regno:")
        for student in sorted_students:
            print(student)
    elif choice == 3:
        sorted_students = sort_by_cgpa(students)
        print("\nSorted by cgpa:")
        for student in sorted_students:
            print(student)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
