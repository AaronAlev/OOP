"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Assign values."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Assign values."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty = Empty()
    # 3 x person usage
    person1 = Person("Jb", "Jackson", 1)
    person2 = Person("Machadee", "Zebedee", 2)
    person3 = Person("Raven", "Norwood", 3)
    # 3 x student usage
    student1 = Student("a", "b", 4)
    student2 = Student("c", "d", 5)
    student3 = Student("e", "f", 6)
