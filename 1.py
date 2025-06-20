 # 1. наследование
 class Mentor:
     def __init__(self, name, surname):
         self.name = name
         self.surname = surname
         self.courses_attached = []

 
 class Lecturer(Mentor):
     def __init__(self, name, surname):
         super().__init__(name, surname)
         self.grades = None

     pass


 class Reviewer(Mentor):
     pass


 lecturer = Lecturer('Иван', 'Иванов')
 reviewer = Reviewer('Пётр', 'Петров')

 print(isinstance(lecturer, Mentor))
 print(isinstance(reviewer, Mentor))
 print(lecturer.courses_attached)
 print(reviewer.courses_attached)

 # 2. Атрибуты и взаимодействие классов

 class Mentor:
     def __init__(self, name, surname):
         self.name = name
         self.surname = surname
         self.courses_attached = []


 class Lecturer(Mentor):
     def __init__(self, name, surname):
         super().__init__(name, surname)
         self.grades = {}  # ключ - курс, значение - список оценок


 class Reviewer(Mentor):
     def rate_hw(self, student, course, grade):
         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
             if course in student.grades:
                 student.grades[course].append(grade)
             else:
                 student.grades[course] = [grade]
         else:
             return 'Ошибка'


 class Student:
     def __init__(self, name, surname, gender):
         self.finished_courses = None
         self.name = name
         self.surname = surname
         self.gender = gender
         self.courses_in_progress = []
         self.grades = {}

     def rate_lecture(self, lecturer, course, grade):
         if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
             if course in lecturer.grades:
                 lecturer.grades[course].append(grade)
             else:
                 lecturer.grades[course] = [grade]
         else:
             return 'Ошибка'


 # Тестирование
 lecturer = Lecturer('Иван', 'Иванов')
 reviewer = Reviewer('Пётр', 'Петров')
 student = Student('Алёхина', 'Ольга', 'Ж')

 student.courses_in_progress += ['Python', 'Java']
 lecturer.courses_attached += ['Python', 'C++']
 reviewer.courses_attached += ['Python', 'C++']

 print(student.rate_lecture(lecturer, 'Python', 7))   # None (успех)
 print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка (лектор не ведёт Java)
 print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка (студент не на С++)
 print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка (reviewer не лектор)

 print(lecturer.grades)  # {'Python': [7]}

 # 3. Полиморфизм и магические методы

 class Reviewer:
     def __init__(self, name, surname):
         self.name = name
         self.surname = surname

     def __str__(self):
         return f'Имя: {self.name}\nФамилия: {self.surname}'


 some_reviewer = Reviewer('Some', 'Buddy')
 print(some_reviewer)

 class Lecturer:
     def __init__(self, name, surname):
         self.name = name
         self.surname = surname
         self.grades = []  # список всех оценок

     def average_grade(self):
         if self.grades:
             return round(sum(self.grades) / len(self.grades), 1)
         return 0

     def __str__(self):
         avg = self.average_grade()
         return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg:.1f}'

     def __lt__(self, other):
         if not isinstance(other, Lecturer):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() < other.average_grade()

     def __le__(self, other):
         if not isinstance(other, Lecturer):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() <= other.average_grade()

     def __eq__(self, other):
         if not isinstance(other, Lecturer):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() == other.average_grade()

     def __ne__(self, other):
         if not isinstance(other, Lecturer):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() != other.average_grade()

     def __gt__(self, other):
         if not isinstance(other, Lecturer):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() > other.average_grade()

     def __ge__(self, other):
         if not isinstance(other, Lecturer):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() >= other.average_grade()

 some_lecturer = Lecturer('Some', 'Buddy')
 some_lecturer.grades = [9.9] * 10  # например, 10 оценок по 9.9

 print(some_lecturer)

 class Student:
     def __init__(self, name, surname, gender):
         self.name = name
         self.surname = surname
         self.gender = gender
         self.courses_in_progress = []
         self.finished_courses = []
         self.grades = {}  # {курс: [оценки]}

     def average_grade(self):
         all_grades = []
         for grades in self.grades.values():
             all_grades.extend(grades)
         if all_grades:
             return round(sum(all_grades) / len(all_grades), 1)
         return 0

     def __str__(self):
         avg = self.average_grade()
         courses_in_progress = ', '.join(self.courses_in_progress)
         finished_courses = ', '.join(self.finished_courses)
         return (
             f'Имя: {self.name}\n'
             f'Фамилия: {self.surname}\n'
             f'Средняя оценка за домашние задания: {avg:.1f}\n'
             f'Курсы в процессе изучения: {courses_in_progress}\n'
             f'Завершенные курсы: {finished_courses}'
         )

     def __lt__(self, other):
         if not isinstance(other, Student):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() < other.average_grade()

     def __le__(self, other):
         if not isinstance(other, Student):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() <= other.average_grade()

     def __eq__(self, other):
         if not isinstance(other, Student):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() == other.average_grade()

     def __ne__(self, other):
         if not isinstance(other, Student):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() != other.average_grade()

     def __gt__(self, other):
         if not isinstance(other, Student):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() > other.average_grade()

     def __ge__(self, other):
         if not isinstance(other, Student):
             raise TypeError("Нельзя сравнивать разные типы")
         return self.average_grade() >= other.average_grade()
 some_student = Student('Ruoy', 'Eman', 'М')
 some_student.courses_in_progress = ['Python', 'Git']
 some_student.finished_courses = ['Введение в программирование']
 some_student.grades = {
     'Python': [10, 9, 10],
     'Git': [9, 9, 10]
 }

 print(some_student)
 lecturer1 = Lecturer('Иван', 'Иванов')
 lecturer1.grades = [9.5, 9.7, 9.9]

 lecturer2 = Lecturer('Петр', 'Петров')
 lecturer2.grades = [9.0, 9.2, 9.4]

 print(lecturer1 > lecturer2)  # True

 student1 = Student('Анна', 'Смирнова', 'ж')
 student1.grades = {'Python': [9, 8, 10]}

 student2 = Student('Олег', 'Попов', 'м')
 student2.grades = {'Python': [10, 10, 10]}

 print(student1 < student2)  # True

#4
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # {курс: [оценки]}

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        avg = self.get_average_grade()
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {avg:.1f}'
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Нельзя сравнивать лектора с другим типом")
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}  # {курс: [оценки]}

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {avg:.1f}\n'
            f'Курсы в процессе изучения: {courses_in_progress}\n'
            f'Завершенные курсы: {finished_courses}'
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Нельзя сравнивать студента с другим типом")
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()


# Функции для подсчёта средних оценок
def average_student_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


def average_lecturer_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


# Создание экземпляров
student1 = Student('Ruoy', 'Eman', 'М')
student2 = Student('Alice', 'Smith', 'Ж')

lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('John', 'Doe')

reviewer1 = Reviewer('Petr', 'Ivanov')
reviewer2 = Reviewer('Anna', 'Smirnova')

# Назначение курсов
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2.courses_in_progress = ['Python', 'Java']
student2.finished_courses = ['Введение в программирование']

lecturer1.courses_attached = ['Python', 'Git']
lecturer2.courses_attached = ['Python', 'Java']

reviewer1.courses_attached = ['Python', 'Git']
reviewer2.courses_attached = ['Python', 'Java']

# Выставление оценок
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Java', 9)

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Git', 9)

student2.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Java', 10)

# Вывод информации
print('--- Студенты ---')
print(student1)
print('\n')
print(student2)

print('\n--- Лекторы ---')
print(lecturer1)
print('\n')
print(lecturer2)

print('\n--- Проверяющие ---')
print(reviewer1)
print('\n')
print(reviewer2)

# Сравнение
print('\n--- Сравнение ---')
print(f'student1 > student2: {student1 > student2}')
print(f'lecturer1 > lecturer2: {lecturer1 > lecturer2}')

# Подсчёт средних
print('\n--- Средние оценки ---')
print(f'Средняя оценка студентов по Python: {average_student_grade([student1, student2], "Python")}')
print(f'Средняя оценка лекторов по Python: {average_lecturer_grade([lecturer1, lecturer2], "Python")}')
