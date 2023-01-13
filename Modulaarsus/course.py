"""Course class with name and grades, test."""


class Course:
    """Class course."""

    def __init__(self, name: str):
        """Set name and create list."""
        self.name = name
        self.grades = []

    def set_grades(self, student, grade):
        """Pair student with grade."""
        self.grades.append(tuple([student, grade]))

    def get_grades(self):
        """Return grades."""
        return self.grades

    def get_average_grade(self):
        """Return average grade."""
        if len(self.grades) > 0:
            total = 0
            times = 0
            for item in self.grades:
                total += item[1]
                times += 1
            total = total / times
            return total
        else:
            return -1

    def __repr__(self):
        """Represent self."""
        return self.name
