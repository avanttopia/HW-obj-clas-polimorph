class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (
                course in self.courses_in_progress or course in self.finished_courses):
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def ave_grade(self):
        return sum([sum(i) for i in self.grades.values()]) / len([sum(i) for i in self.grades.values()])

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.ave_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(map(str, self.courses_in_progress))}\n" \
               f"Завершенные курсы: {', '.join(map(str, self.finished_courses))}"

    def __gt__(self, other):
        if self.ave_grade() > other.ave_grade():
            return f"Средняя оценка за домашние задания у студента {self.name} {self.surname} выше, чем у студента {other.name} {other.surname}"
        elif self.ave_grade() == other.ave_grade():
            return f"Средние оценки за домашние задания у студентов {self.name} {self.surname} и {other.name} {other.surname} равны"
        else:
            return f"Средняя оценка за домашние задания у студента {self.name} {self.surname} меньше, чем у студента {other.name} {other.surname}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def ave_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ave_grade()}"

    def __gt__(self, other):
        if self.ave_grade() > other.ave_grade():
            return f"Средняя оценка за лекции у преподавателя {self.name} {self.surname} выше, чем у лектора {other.name} {other.surname}"
        elif self.ave_grade() == other.ave_grade():
            return f"Средние оценки за лекции у преподавателей {self.name} {self.surname} и {other.name} {other.surname} равны"
        else:
            return f"Средняя оценка за лекции у преподавателя {self.name} {self.surname} меньше, чем у лектора {other.name} {other.surname}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student_one = Student('Carol', 'Danvers', 'female')
student_one.courses_in_progress += ['Python']
student_one.courses_in_progress += ['Git']
student_one.finished_courses += ['Введение в программирование']

student_two = Student('Steve', 'Rogers', 'male')
student_two.courses_in_progress += ['Python']
student_two.courses_in_progress += ['Git']
student_two.finished_courses += ['Введение в программирование']

mentor_one = Mentor('John', 'Wick')
mentor_one.courses_attached += ['Python']

mentor_two = Mentor('Duncan', 'MacLeod')
mentor_two.courses_attached += ['Git']

reviewer_one = Reviewer('Ellen', 'Ripley')
reviewer_one.courses_attached += ['Python']
reviewer_one.rate_homework(student_one, 'Python', 10)
reviewer_one.rate_homework(student_two, 'Python', 8)

reviewer_two = Reviewer('Katherine', 'Daniels')
reviewer_two.courses_attached += ['Git']
reviewer_two.rate_homework(student_one, 'Git', 9)
reviewer_two.rate_homework(student_two, 'Git', 10)

lecturer_one = Lecturer('Peter', 'Weyland')
lecturer_one.courses_attached += ['Python']
lecturer_one.courses_attached += ['Введение в программирование']

lecturer_two = Lecturer('Hideo', 'Yutani')
lecturer_two.courses_attached += ['Python']
lecturer_two.courses_attached += ['Git']

student_one.rate_lectures(lecturer_one, 'Python', 9)
student_one.rate_lectures(lecturer_one, 'Введение в программирование', 6)
student_one.rate_lectures(lecturer_two, 'Git', 5)
student_two.rate_lectures(lecturer_one, 'Python', 8)
student_two.rate_lectures(lecturer_one, 'Введение в программирование', 7)
student_two.rate_lectures(lecturer_two, 'Git', 4)

students_list = [student_one, student_two]
lecturers_list = [lecturer_one, lecturer_two]


def ave_grades_students(students_list, course_name):
    s, c = 0, 0
    for i in students_list:
        if course_name in i.grades:
            s += i.grades[course_name][0]
            c += 1
    return f"Средняя оценка за домашние задания по предмету {course_name} у всех студентов: {s / c}"


def ave_grades_lecturers(lecturers_list, course_name):
    s, c = 0, 0
    for i in lecturers_list:
        if course_name in i.courses_attached:
            s += sum(i.grades)
            c += len(i.grades)
    return f"Средняя оценка за лекции по предмету {course_name} у всех лекторов: {s / c}"


print(student_two)
print(reviewer_one)
print(lecturer_one)
print(ave_grades_students(students_list, 'Python'))
print(ave_grades_lecturers(lecturers_list, 'Git'))
print(student_two < student_one)
print(lecturer_one > lecturer_two)
