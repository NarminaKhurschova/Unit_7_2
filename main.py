from utils import *

search_student_by_pk = int(input("Введите номер студента"))

student = get_student_by_pk(search_student_by_pk)

if student:
    print(f"Студент {student['full_name']} \nЗнает {','.join(student['skills'])}")
else:
    print("Нет такого студента")
    quit()

search_profession_by_title = input(f"Выберите специальность для оценки студента {student['full_name']}")

profession = get_profession_by_title(search_profession_by_title)

if profession:
    skills, lacks, fitness = check_fitness(student, profession).values()
    print(f"Пригодность: {fitness}%\n{student['full_name']} знает {','.join(skills)}\n{student['full_name']} не знает {','.join(lacks)}")
else:
    print("У нас нет такой специальности")

