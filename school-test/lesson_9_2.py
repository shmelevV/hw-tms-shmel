class Students:

    def __init__(self, surname: str, group_number: int, estimates: list):
        self.surname = surname
        self.group_number = group_number
        self.estimates = estimates


class School:

    def __init__(self):
        self.students = list()

    def add_student(self, student):
        self.students.append(student)

    def show_student_with_marks(self, *marks):
        for student in self.students:
            if all([mark in marks for mark in student.estimates]):
                print(f"Student {student.surname} in the "
                      f"{student.group_number} group has only {marks} marks")

    def show_student_with_group(self, group: int):
        for student in self.students:
            if student.group_number == group:
                print(f"Student {student.surname} in the group {group}")

    def show_students_with_automat(self, average_number_for_automat: int):
       stundets_with_automat = [student for student in self.students
                                if sum(student.estimates)/len(student.estimates) >= average_number_for_automat]

       for student in stundets_with_automat:
            print(f"Student {student.surname} has automat")


