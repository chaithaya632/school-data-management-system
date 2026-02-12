students = {
    24811: {
        "name": "chaitanya",
        "age": 20,
        "marks": (85, 90, 88),
        "section": "A"
    },
    24812: {
        "name": "satya",
        "age": 21,
        "marks": (78, 80, 75),
        "section": "B"
    },
    24813: {
        "name": "mani",
        "age": 20,
        "marks": (92, 89, 95),
        "section": "A"
    },
    24814: {
        "name": "nandhu",
        "age": 22,
        "marks": (70, 72, 68),
        "section": "C"
    }
}

while True:
    print("\n--- School Data Management System ---")
    print("1. Add student")
    print("2. Display all students")
    print("3. Search student by roll number")
    print("4. Remove student by roll number")
    print("5. Show class topper")
    print("6. Display unique sections")
    print("7. Exit")

    try:
        choice = int(input("Enter your option: "))

        if choice == 1:
            roll = int(input("Enter roll number: "))

            if roll in students:
                print("Roll number already exists.")
            else:
                name = input("Enter name: ")
                age = int(input("Enter age: "))

                print("Enter marks of three subjects:")
                sub1 = int(input("Subject 1: "))
                sub2 = int(input("Subject 2: "))
                sub3 = int(input("Subject 3: "))

                section = input("Enter section: ")

                students[roll] = {
                    "name": name,
                    "age": age,
                    "marks": (sub1, sub2, sub3),
                    "section": section
                }

                print("Student added successfully.")

        elif choice == 2:
            if not students:
                print("No student records found.")
            else:
                for roll, data in students.items():
                    print("\nRoll:", roll)
                    print("Name:", data["name"])
                    print("Age:", data["age"])
                    print("Marks:", data["marks"])
                    print("Section:", data["section"])

        elif choice == 3:
            roll = int(input("Enter roll number to search: "))

            if roll in students:
                data = students[roll]
                print("\nStudent Found:")
                print("Name:", data["name"])
                print("Age:", data["age"])
                print("Marks:", data["marks"])
                print("Section:", data["section"])
            else:
                print("Student not found.")

        elif choice == 4:
            roll = int(input("Enter roll number to remove: "))

            if roll in students:
                del students[roll]
                print("Student removed successfully.")
            else:
                print("Student not found.")

        elif choice == 5:
            if not students:
                print("No students available.")
            else:
                topper_roll = None
                highest = 0

                for roll, data in students.items():
                    total = sum(data["marks"])
                    if total > highest:
                        highest = total
                        topper_roll = roll

                print("\nClass Topper:")
                print("Roll No:", topper_roll)
                print("Name:", students[topper_roll]["name"])
                print("Total Marks:", highest)
                
        elif choice == 6:
            sections = set()

            for data in students.values():
                sections.add(data["section"])

            print("Unique Sections:", sections)

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Enter correct data type.")
