def input_students():
    return int (input("Enter the number of the students: "))

def input_information():
    student_id = input("Enter your student ID: ")
    name = input("Enter your name: ")
    dob = input("Enter your date of birth: ")
    students.append({"id": student_id, "name": name, "dob": dob})

def input_course():
    return int(input("Enter the number of course: "))

def input_course_information():
    course_id = input("Enter your course ID: ")
    name = input("Enter your name: ")
    courses.append({"id": couse_id, "name": name})    

def input_marks_for_course():
    course_id = input("Enter course ID to input marks: ")
    if course_id not in [course["id"] for course in courses]:
        print("Invalid course ID!")
        return
    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        student_id = student["id"]
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student_id}): "))
        marks[course_id][student_id] = mark
def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks_for_course():
    course_id = input("Enter course ID to view marks: ")
    if course_id not in marks:
        print("No marks available for this course!")
        return
    
    print(f"Marks for course {course_id}:")
    for student_id, mark in marks[course_id].items():
        student_name = next((s["name"] for s in students if s["id"] == student_id), "Unknown")
        print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")

        
def main():
    while True:
        print("\nMenu:")
        print("1. Input number of students")
        print("2. Input student information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Input marks for a course")
        print("6. List courses")
        print("7. List students")
        print("8. Show student marks for a course")
        print("9. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            num_students = input_number_of_students()
            print(f"Number of students: {num_students}")
        elif choice == 2:
            input_student_information()
        elif choice == 3:
            num_courses = input_number_of_courses()
            print(f"Number of courses: {num_courses}")
        elif choice == 4:
            input_course_information()
        elif choice == 5:
            input_marks_for_course()
        elif choice == 6:
            list_courses()
        elif choice == 7:
            list_students()
        elif choice == 8:
            show_student_marks_for_course()
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()