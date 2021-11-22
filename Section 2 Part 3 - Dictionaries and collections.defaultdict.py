from collections import defaultdict
student_grades = {"Jack": [85, 90], "Jill": [80, 95]}


def get_grades_naive(name):
    if name in student_grades:
        return student_grades[name]
    return []

# >>> get_grades("Jack")
# [85, 90]
# >>> get_grades("Jill")
# [80, 95]
# >>> get_grades("Joe")
# []


def get_grades_better(name):
    # If you don't pass in 2nd argument, it will default to None
    return student_grades.get(name, [])


def get_grades_with_assignment(name):
    if name not in student_grades:
        student_grades[name] = []
    return student_grades[name]


def get_grades_with_assignment_better(name):
    return student_grades.setdefault(name, [])


def set_grade_naive(name, score):
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]
    grades.append(score)


def set_grade_better(name, score):
    grades = student_grades.setdefault(name, [])
    grades.append(score)

# >>> set_grade_better("Jennifer", 100)
# >>> student_grades


# now to improve it so we don't even have to use setdefault!

student_grades = defaultdict(list)


def set_grade_best(name, score):
    # this is evaluated student_grades[name] which either gets
    # the value bound to name, or binds empty list to name.
    # then it appends the score
    student_grades[name].append(score)
