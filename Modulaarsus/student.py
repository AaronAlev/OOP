"""Student class with student name and grades."""


class Student:
    """Class student."""

    def __init__(self, name: str):
        """Set name, id and create lists."""
        self.id_list = []
        self.id = None
        self.name = name
        self.grades = []

    def set_id(self, id: int):
        """Set new id."""
        if self.id is None:
            self.id_list.append(id)
            self.id = id
        else:
            pass


    def get_id(self) -> int:
        """Return id."""
        return self.id

    def set_grades(self, course, grade: int):
        """Set new grades."""
        self.grades.append(tuple([course, grade]))

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

    def __repr__(self) -> str:
        """Represent self."""
        return self.name
