class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course):
        self.courses[course.course_code] = course

    def display_courses(self):
        print(f"Courses enrolled by {self.name}:")
        for course_code, course in self.courses.items():
            print(f"{course_code}: {course.title}")

    def get_gpa(self):
        total_credits = 0
        total_grade_points = 0
        for course in self.courses.values():
            if course.course_code in self.courses and self.courses[course.course_code].grade:
                total_credits += course.credits
                total_grade_points += course.credits * course.grade_points(self.courses[course.course_code].grade)
        if total_credits == 0:
            return 0
        return total_grade_points / total_credits


class Course:
    def __init__(self, course_code, title, credits):
        self.course_code = course_code
        self.title = title
        self.credits = credits
        self.students = {}
        self.grade = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def assign_grade(self, student_id, grade):
        self.grade[student_id] = grade

    def grade_points(self, grade):
        if grade == 'A':
            return 4.0
        elif grade == 'B':
            return 3.0
        elif grade == 'C':
            return 2.0
        elif grade == 'D':
            return 1.0
        else:
            return 0.0


def student_login(students):
    student_id = int(input("Enter your student ID: "))
    if student_id in students:
        student = students[student_id]
        print(f"Welcome, {student.name}!")
        return student
    else:
        print("Student not found.")
        return None


def teacher_login(students):
    # Placeholder for teacher login
    # For now, returning a placeholder teacher object
    return Teacher()


class Teacher:
    def __init__(self):
        pass

    def view_student_grades(self, course):
        print(f"Grades for {course.title}:")
        for student_id, grade in course.grade.items():
            print(f"Student ID: {student_id}, Grade: {grade}")

    def view_student_attendance(self, course):
        # Placeholder for viewing student attendance
        print(f"Attendance for {course.title}:")
        for student_id in course.students:
            print(f"Student ID: {student_id}, Attendance: Present")


def display_menu():
    print("\nMenu:")
    print("1. Student login")
    print("2. Teacher login")
    print("3. Exit")


if __name__ == "__main__":
    students = {1: Student(1, "Alice"), 2: Student(2, "Bob")}
    courses = {"MATH101": Course("MATH101", "Mathematics", 3), "PHY101": Course("PHY101", "Physics", 4)}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            student = student_login(students)
            if student:
                # Student options
                while True:
                    print("\nStudent Menu:")
                    print("1. Enroll in a course")
                    print("2. Display enrolled courses")
                    print("3. Calculate GPA")
                    print("4. Logout")
                    student_choice = input("Enter your choice: ")

                    if student_choice == '1':
                        course_code = input("Enter course code: ")
                        if course_code in courses:
                            student.enroll(courses[course_code])
                            print(f"Enrolled in {courses[course_code].title}")
                        else:
                            print("Course not found.")

                    elif student_choice == '2':
                        student.display_courses()

                    elif student_choice == '3':
                        print(f"GPA of {student.name}: {student.get_gpa()}")

                    elif student_choice == '4':
                        break

        elif choice == '2':
            teacher_login()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
