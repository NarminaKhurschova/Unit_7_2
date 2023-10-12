import json
import os.path


def load_students():  # загружает список студентов из файла
    with open(os.path.join("data", "students.json"), "r") as file:
        stud_content = file.read()
        stud_content_json = json.loads(stud_content)
        return stud_content_json


def load_professionals():  # загружает список профессий из файла
    with open(os.path.join("data", "professions.json"), 'r') as file:
        prof_content = file.read()
        prof_content_json = json.loads(prof_content)
        return prof_content_json


def get_student_by_pk(pk):    # получает словарь с данными студента по его pk
    all_students = load_students()
    for student in all_students:
        if student['pk'] == pk:
            return student
    else:
        pass


def get_profession_by_title(title):   # Получает словарь с инфо о профессии по названию
    all_professions = load_professionals()
    for profession in all_professions:
        if profession['title'].lower() == title.lower():
            return profession
        else:
            pass


def check_fitness(student, profession):     # сравнивает навык студента с нужными навыками в профессии
    all_fit = {}
    check_skills = sorted(set(student['skills']).intersection(set(profession['skills'])))
    check_lacks = sorted(set(student['skills']).symmetric_difference(set(profession['skills'])))
    all_fit["has"] = check_skills
    all_fit["lacks"] = check_lacks
    per = 100 // len(profession["skills"]) * len(check_skills)
    all_fit["fit_percent"] = per
    return all_fit
