from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def email(self):
        return self._email

    @abstractmethod
    def get_info(self):
        pass


class Student(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self._courses = []

    def enroll(self, course):
        self._courses.append(course)

    def get_info(self):
        return f"Student: {self._name}, email: {self._email}"


class Instructor(Person):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.expertise = expertise

    def create_course(self, title):
        return Course(title, self)

    def get_info(self):
        return f"Instructor: {self._name}, expertise: {self.expertise}"


class Course:
    def __init__(self, title, instructor):
        self._title = title
        self._instructor = instructor
        self._assignments = []

    def add_assignment(self, assignment):
        self._assignments.append(assignment)

    def show_assignments(self):
        return [a.title for a in self._assignments]


class Assignment(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def evaluate(self, submission):
        pass


class CodingAssignment(Assignment):
    def evaluate(self, submission):
        return "Passed" if "code" in submission.lower() else "Failed"


class QuizAssignment(Assignment):
    def evaluate(self, submission):
        return f"Score: {len(submission.split()) * 10}"


class AssignmentFactory:
    @staticmethod
    def create_assignment(atype, title):
        if atype == "coding":
            return CodingAssignment(title)
        elif atype == "quiz":
            return QuizAssignment(title)
        raise ValueError("Unknown assignment type")


if __name__ == "__main__":
    instructor = Instructor("Aidar", "aidar@example.com", "Python")
    course = instructor.create_course("Python for Beginners")

    a1 = AssignmentFactory.create_assignment("coding", "Homework 1")
    a2 = AssignmentFactory.create_assignment("quiz", "Quiz 1")

    course.add_assignment(a1)
    course.add_assignment(a2)

    student = Student("Dana", "dana@example.com")
    student.enroll(course)

    print(student.get_info())
    print(course.show_assignments())
    print(a1.evaluate("my code solution"))
    print(a2.evaluate("answer1 answer2"))