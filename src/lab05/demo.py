import sys
import os
from pathlib import Path

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, project_root)

from src.lab01.model import *

from src.lab05.collection import *
from src.lab05.strategies import *


student1 = Student("student one", 16, "BIVT-25-8", 1)
student2 = Student("student two", 17, "BIVT-25-8", 2)
student3 = Student("student three", 18, "BIVT-25-8", 3)
student4 = Student("student four", 19, "BIVT-25-8", 4)
student5 = Student("student five", 20, "BIVT-25-8", 5)
student6 = Student("student six", 21, "BIVT-25-8", 6)

student1.grade(2)
student1.grade(2)
student2.grade(2)
student2.grade(3)
student3.grade(3)
student3.grade(3)
student4.grade(3)
student4.grade(4)
student5.grade(4)
student5.grade(4)
student6.grade(4)
student6.grade(5)

student_collection = StudentGroup("BIVT-25-8")
student_collection.add(student1)
student_collection.add(student2)
student_collection.add(student3)
student_collection.add(student4)
student_collection.add(student5)
student_collection.add(student6)



print("\n---Сценарий 1: сортировка коллекции---")

print("\n1) сотрировка по фамилии (алфавитный порядок)")
namesort = student_collection
namesort.sort_by_name()
for i in namesort:
    print(i)

print("\n2) сотрировка по курсу (от 1 до 6)")
coursesort = student_collection
coursesort.sort_by_course()
for i in coursesort:
    print(i)

print("\n3) Сортировка по среднему баллу")
gpasort = student_collection
gpasort.sort_by_gpa()
for i in gpasort:
    print(i)

print("\n---Сценарий 2: фильтрация коллекции---")

print("\n1) студенты с 6-го курса (фильтр и именованную функцию)")
last_course = list(filter(filter_last_course, student_collection))
print_list_students(last_course)

print("\n2) студенты с 1-го курса (фильтр filter_first_course)")
first_course = list(filter(filter_first_course, student_collection))
print_list_students(first_course)

print("\n3) фильтрация по совершеннолетним (через lambda)")
coll_st_age = student_collection
coll_st_age = coll_st_age.sort_by(key = lambda st: st.student_age >= 18)
print_list_students(coll_st_age)

print("\n4) фильтрация по совершеннолетним (через функцию filter_by_age)")
coll_st_age2 = student_collection
coll_st_age2 = coll_st_age2.sort_by(key = filter_mature)
print_list_students(coll_st_age2)


print("\n---Сценарий 3: map, lambda и фабрика функций---")

print("\n1) список средногго балла студентов (через map и lambda)")
gpa_list = list(map(lambda st: st.gpa, student_collection))
print(f"> GPA: {gpa_list}")

print("\n2) лучшие студенты (GPA > 4) через фабрику функций")
gpa_filter = make_gpa_filter(4)
best_students = list(filter(gpa_filter, student_collection))
print_list_students(best_students)
    

print("\n---Сценарий 4: паттерн стратегия через callable-объекты---\n   Цепочки операций над коллекцией")

print("\n> Стратегия 1")
print("- Цепочка: фильтр(6 курс) → стратегия(о курсе)")
result = student_collection.sort_by(filter_last_course).apply(StrategyByCourse())
print_list_students(result)

print("\n> Стратегия 2")
print("- Цепочка с другой стратегией (StrategyByName)")
result = student_collection.sort_by(filter_last_course).apply(StrategyByName())
print_list_students(result)

print("\n> Стратегия 3")
print("- Стратегия StrategyByGPA (информация о GPA):")
resalt03 = student_collection.apply(StrategyByGPA())
print_list_students(resalt03)