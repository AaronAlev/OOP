"""School class which stores information about courses and students, test."""
import random

from course import Course
from student import Student


class School:
    """Class school."""

    def __init__(self, name):
        """Set name and create lists."""
        self.name = name
        self.courses = []
        self.students = []
        self.average = []
        self.student_by_grade = []

    def add_course(self, course: Course):
        """Add course to list."""
        if course in self.courses:
            pass
        else:
            self.courses.append(course)

    def add_student(self, student: Student):
        """Add student to list."""
        if student not in self.students:
            id = random.randint(1, 1000)
            while any(student.get_id() == id for student in self.students):
                id = random.randint(1, 1000)
            student.set_id(id)
            self.students.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Set student grade."""
        if student not in self.students:
            pass
        elif course not in self.courses:
            pass
        else:
            student.set_grades(course, grade)
            course.set_grades(student, grade)

    def get_students(self) -> list[Student]:
        """Return students."""
        return self.students

    def get_courses(self) -> list[Course]:
        """Return courses."""
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        """Return students ordered by grade."""
        grade_dict = {}
        ordered_by_grade = []
        for student in self.students:
            grade_dict[student] = student.get_average_grade()
        a = sorted(grade_dict.items(), key=lambda item: item[1], reverse=True)
        for item in a:
            ordered_by_grade.append(item[0])
        return ordered_by_grade
