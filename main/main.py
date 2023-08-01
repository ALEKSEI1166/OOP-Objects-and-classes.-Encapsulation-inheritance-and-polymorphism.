# ДЗ по теме ОПП: "Объекты и классы. Инкапсуляция, наследие и полиформизм".

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grasdes_spisok = []

    def grade_list(self, lecturer, course, grade):
        """Реализует возможность выставления оценки лектору студентом, если это лектор ведет лекции по данному курсу у этого студента
        Принимает на вход переменные grade_list(self, lecturer, course, grade)"""
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        """метод класса студентов - подсчет средней оценки студента"""
        if not self.grades:
            return 0
        grades_spisok = []  # создаем пустой список куда буду складывать оценки
        for rating in self.grades.values():  # проходим в цикле по словарю с оценками
            grades_spisok.extend(rating)  # добавляем в ранее созданный список кортеж, полученный при итерации
            return round(sum(grades_spisok) / len(grades_spisok), 2)

    def __str__(self):
        """Метод должен выводить информацию в следующем виде:
    #             print(some_student)
    #             Имя: Ruoy
    #             Фамилия: Eman
    #             Средняя оценка за домашние задания: 9.9
    #             Курсы в процессе изучения: Python,
    #             Завершенные курсы: Введение в программирование"""
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.average_rating()}\n' \
               f'Курсы в процессе обучения: {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}'

    def __le__(self, other: 'Student'):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.average_rating() > other.average_rating()

    def __lt__(self, other: 'Student'):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.average_rating() < other.average_rating()

    def __eq__(self, other: 'Student'):
        if not isinstance(other, Student):
            return 'Такое сравнение некорректно'
        return self.average_rating() == other.average_rating()


class Mentor:
    def __init__(self, name, surname):  # переопределение метода _init_ для определения атрибутов класса <Mentor>
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # наследуем класс <Lecturer> от родительского класса <Mentor>
    def __init__(self, name, surname):  # инициализируем и прописываем аргументы
        super().__init__(name, surname)  # обращаюсь (вызываю в наследники) метод <init> родителя <Mentor>
        self.grades = {}  # создаем пустой словарь

    def average_rating(self):
        if not self.grades:
            return 0
        grades_spisok = []
        for rating in self.grades.values():
            grades_spisok.extend(rating)
        return round(sum(grades_spisok) / len(grades_spisok), 2)

    def __str__(
            self) -> str:  # метод "str" внутри себя по пользовательскому указу собирает информацию для вывода в консоль
        """У лекторов он должен выводить информацию в следующем виде:
            print(some_lecturer)
            Имя: Some
            Фамилия: Buddy
            Средняя оценка за лекции: 9.9"""
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
        return res

    def __le__(self, other: 'Lecturer'):
        if not isinstance(other, Lecturer):
            return 'Такое сравнение некорректно'
        return self.average_rating() > other.average_rating()

    def __lt__(self, other: 'Lecturer'):
        if not isinstance(other, Lecturer):
            return 'Такое сравнение некорректно'
        return self.average_rating() < other.average_rating()

    def __eq__(self, other: 'Lecturer'):
        if not isinstance(other, Lecturer):
            return 'Такое сравнение некорректно'
        return self.average_rating() == other.average_rating()


class Reviewer(Mentor):  # наследуем класс <Reviewer> от родительского класса <Mentor>
    """Реализует возможность выставления оценки студенту за домашние задания,
       #     если этот проверяющий закреплен за этим студентом по данному курсу,
       #     или возвращает ошибку."""

    def grade_list(self, student, course, grade):
        """Реализует возможность выставления оценки лектору студентом, если это лектор ведет лекции по данному курсу у этого студента"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(
            self) -> str:  # метод "str" внутри себя по пользовательскому указу собирает информацию для вывода в консоль
        """ У проверяющих он должен выводить информацию в следующем виде:
            print(some_reviewer)
            Имя: Some
            Фамилия: Buddy"""
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# Создаем лекторов и закрепляем их за курсом
best_lecturer_1 = Lecturer('Nikolai', 'Sviridov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Albus', 'Dumbledore')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Oleg', 'Gezhin')
best_lecturer_3.courses_attached += ['Python']

# Создаем проверяющих и закрепляем их за курсом
cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Ostap', 'Bender')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Aleksei', 'Dolgov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Harry', 'Potter')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Bilbo', 'Baggins')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Выставляем оценки лекторам за лекции
student_1.grade_list(best_lecturer_1, 'Python', 10)
student_1.grade_list(best_lecturer_1, 'Python', 10)
student_1.grade_list(best_lecturer_1, 'Python', 10)

student_1.grade_list(best_lecturer_2, 'Python', 5)
student_1.grade_list(best_lecturer_2, 'Python', 7)
student_1.grade_list(best_lecturer_2, 'Python', 8)

student_1.grade_list(best_lecturer_1, 'Python', 7)
student_1.grade_list(best_lecturer_1, 'Python', 8)
student_1.grade_list(best_lecturer_1, 'Python', 9)

student_2.grade_list(best_lecturer_2, 'Java', 10)
student_2.grade_list(best_lecturer_2, 'Java', 8)
student_2.grade_list(best_lecturer_2, 'Java', 9)

student_3.grade_list(best_lecturer_3, 'Python', 5)
student_3.grade_list(best_lecturer_3, 'Python', 6)
student_3.grade_list(best_lecturer_3, 'Python', 7)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.grade_list(student_1, 'Python', 8)
cool_reviewer_1.grade_list(student_1, 'Python', 9)
cool_reviewer_1.grade_list(student_1, 'Python', 10)

# Реализует возможность выставления оценки студенту за домашние задания, если этот проверяющий закреплен за этим студентом по данному курсу или возвращает ошибку.
cool_reviewer_2.grade_list(student_2, 'Java', 8)
cool_reviewer_2.grade_list(student_2, 'Java', 7)
cool_reviewer_2.grade_list(student_2, 'Java', 9)

# Реализует возможность выставления оценки лектору студентом, если это лектор ведет лекции по данному курсу у этого студента
cool_reviewer_2.grade_list(student_3, 'Python', 8)
cool_reviewer_2.grade_list(student_3, 'Python', 7)
cool_reviewer_2.grade_list(student_3, 'Python', 9)
cool_reviewer_2.grade_list(student_3, 'Python', 8)
cool_reviewer_2.grade_list(student_3, 'Python', 7)
cool_reviewer_2.grade_list(student_3, 'Python', 9)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

# выводим характеристики созданных рецензентов в требуемом виде
print(f'Перечень рецендентов:\n\n{cool_reviewer_1}\n\n{cool_reviewer_2}')
print()
print()

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Создаем список студентов
student_list = [student_1, student_2, student_3]

# Создаем список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]
# создаем список всех студентов, лекторов, курсов
oll_students = [student_1, student_2]
oll_lecturers = [best_lecturer_1, best_lecturer_2]
oll_courses = input('Введите название курса: ')


# Функция для подсчета средней оценки за лекции всех студентов в рамках курса в качестве аргумента принимает список студентов и название всех курсов
def student_rating(oll_students, oll_courses):
    sum_all = 0
    count_all = 0
    grades_list = []
    for nil in oll_students:
        grades_list.extend(nil.grades.get(oll_courses, []))
    if not grades_list:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(grades_list) / len(grades_list), 2)


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса в качестве аргумента принимает список лекторов и название всех курсов
def lecturer_rating(oll_lecturer, oll_courses):
    return student_rating(oll_lecturer, oll_courses)
    print(f'Сравнения всех студентов по средним оценкам за домашние задания: '
          f'{student_1.name} {student_1.surname} {"<" if student_1 < student_2 else (">" if student_1 > student_2 else "=")} {student_2.name} {student_2.surname}')


print()

# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
