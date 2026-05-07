class StrategyByName:
    def __call__(self, student):
        return f"Student: {student.student_name}"

class StrategyByGPA:
    def __call__(self, student):
        if student.student_gpa > 2.5:
            return f"Student {student.student_name} - GPA {student.student_gpa}"
        return f"Student {student.student_name} is at risk; their GPA is {student.student_gpa}"

class StrategyByCourse:
    def __call__(self, student):
        if student.student_course == 6:
            return f"Student {student.student_name} is about to graduate: {student.student_course}"
        return f"Student {student.student_name} is currently on the {student.student_course} course"
    
def print_list_students(students):
    for i, st in enumerate(students, 1):
        print(f"  {i}. {st}")

def filter_last_course(student):
    return student.student_course == 6

def filter_first_course(student):
    return student.student_course == 1

def filter_mature(student):
    return student.student_age >= 18

def make_gpa_filter(min_gpa):
    def filter_min_gpa(st):
        return st.student_gpa > min_gpa
    return filter_min_gpa