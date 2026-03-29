from model import Student
from datetime import date

print("CREATING VALID STUDENTS")

try:
    andrew = Student("Andrew", 18, "BIVT-25-8", 1)
    print(f"Created: {andrew.student_name}, {andrew.student_age} years old")
    print(f"    Details: {andrew}")
except Exception as e:
    print(f"Unexpected error: {e}")

try:
    matthew = Student("Matthew", 19, "BIVT-24-13", 2)
    print(f"Created: {matthew.student_name}, course {matthew.course}, group {matthew.student_group}")
except Exception as e:
    print(f"Unexpected error: {e}")

print("INVALID CREATION")

# Empty name
try:
    invalid = Student("", 19, "BIVT-25-8", 1)
    print("expected to raise ValueError")
except ValueError as e:
    print(f"caught empty name: {e}")

try:
    invalid = Student("young prodigy", 5, "BIVT-25-8", 1)
    print("expected to raise ValueError for age under 6")
except ValueError as e:
    print(f"caught underage: {e}")

try:
    invalid = Student("Mammoth", 1004, "Group!", 5)
    print("expected to raise ValueError for age over 100")
except ValueError as e:
    print(f"caught too old: {e}")

try:
    invalid = Student("filler", "Eighteen", "whadaheeeell", 1) #type: ignore
    print("expected to raise ValueError for non-int age")
except ValueError as e:
    print(f"caught non-integer age: {e}")
try:
    invalid = Student("boy oh boy", 25, "", 1)
    print("expected raise ValueError for empty group")
except ValueError as e:
    print(f"caught empty group: {e}")

try:
    invalid = Student("No Subject", 38, "Instructor", 0)
    print("expected raise ValueError for invalid course")
except ValueError as e:
    print(f"caught invalid course: {e}")

print("GRADE SYSTEM")

print("adding grades for andrew!")
andrew.grade(5)
print(f"Added grade=5, Current GPA: {andrew.student_gpa}")
andrew.grade(4)
print(f"Added grade=4, Current GPA: {andrew.student_gpa}")
andrew.grade(4)
print(f"Added grade=4, Current GPA: {andrew.student_gpa}")

print("\n  attempting invalid grades...")

try:
    andrew.grade(6)
    print("expected raise ValueError for grade over 5")
except ValueError as e:
    print(f"caught grade over 5: {e}")

try:
    andrew.grade(-1)
    print("expected raise ValueError for negative grade")
except ValueError as e:
    print(f"caught negative grade: {e}")

try:
    andrew.grade("Splendiforous.") #type: ignore
    print("expected raise ValueError for non-numeric grade")
except ValueError as e:
    print(f"caught non-numeric: {e}")

try:
    andrew.deactivate()
    andrew.grade(5) #type: ignore
    print("expected raise AttributeError for grading inactive")
except AttributeError as e:
    print(f"caught grading inactive: {e}")

andrew.activate()
andrew.update_group = 'BIVT-25-8'

print("SICK LEAVE SYSTEM")

print("putting da man on sick leave")
andrew.add_sick_leave(date(2025, 5, 5), date(2025, 5, 10))
print(f"added sick leave, sick leave log: {andrew.student_sick_leave_log}")
andrew.add_sick_leave(date(2025, 6, 5), date(2025, 6, 10))
print(f"added the second sick leave, sick leave log: {andrew.student_sick_leave_log}")
andrew.add_sick_leave(date(2025, 10, 10), date(2025, 10, 30))
print(f"added the really long sick leave, sick leave log: {andrew.student_sick_leave_log}")

print("\n  Attempting invalid sick leave operations...")

try:
    andrew.add_sick_leave(date(2025, 10, 10), date(2025, 9, 30))
    print("expected raise ValueError for invalid dates")
except ValueError as e:
    print(f"caught invalid dates: {e}")

try:
    andrew.add_sick_leave("today", date(2025, 10, 30)) #type: ignore
    print("expected raise ValueError for invalid start")
except ValueError as e:
    print(f"saught invalid start: {e}")

try:
    andrew.add_sick_leave(date(2025, 10, 10), "tomorrow") #type: ignore
    print("expected raise ValueError for invalid end")
except ValueError as e:
    print(f"caught invalid end: {e}")

try:
    andrew.deactivate()
    andrew.add_sick_leave(date(2025, 10, 10), date(2025, 10, 15)) 
    print("expected raise AttributeError for inactive student")
except AttributeError as e:
    print(f"caught inactive student: {e}")

andrew.activate()
andrew.update_group = "BIVT-25-8"

print("ACTIVITY MANAGER")

print(f"  Andrew activity status: {andrew.active}")

print("\n  Deactivating Andrew")
andrew.deactivate()
print(f"Deactivated Andrew: {andrew.active}")
print(f"Deactivation removes the group: {andrew.student_group}")

print("\n  Attempting operations on inactive student")

try:
    andrew.grade(4)
    print("expected raise AttributeError for grading inactive student")
except AttributeError as e:
    print(f"caught grading inactive: {e}")

try:
    andrew.update_group = "woag,h."
    print("expected raise AttributeError for updating inactive")
except AttributeError as e:
    print(f"caught update inactive: {e}")

try:
    andrew.add_sick_leave(date(2020, 1, 1), date(2020, 2, 1))
    print("expected raise AttributeError for adding sickleave to inactive")
except AttributeError as e:
    print(f"caught sick leave inactive: {e}")

# Reactivate
print("\n  Reactivating Andrew")
andrew.activate()
andrew.update_group = "BIVT-25-8"
print(f"Reactivated: {andrew.active}")

print("INFOMANAGER")

print(f"Current info: Name='{andrew.student_name}', Age={andrew.student_name}, Group='{andrew.student_name}'")

print("\n  Updating name")
andrew.update_name = "Sire Andrew the Fourth"
print(f"Name updated: '{andrew.student_name}'")

try:
    andrew.update_name = ""
    print("expected raise ValueError for empty name")
except ValueError as e:
    print(f"caught empty name update: {e}")

print("\n  Updating age")
andrew.update_age = 19
print(f"Age updated: {andrew.student_age}")

try:
    andrew.update_age = 17
    print("expected raise ValueError for decreasing age")
except ValueError as e:
    print(f"caught age decrease: {e}")

try:
    andrew.update_age = 5
    print("expected raise ValueError for age < 6!")
except ValueError as e:
    print(f"caught underage update: {e}")

try:
    andrew.update_age = 1005
    print("expected raise ValueError for age > 100!")
except ValueError as e:
    print(f"caught overage update: {e}")

# Update group
print("\n  Updating group")
andrew.update_group = "BIVT-25-10"
print(f"group updated: '{andrew.student_group}'")

# Invalid group
try:
    andrew.update_group = ""
    print("expected raise ValueError for empty group")
except ValueError as e:
    print(f"caught empty group update: {e}")

print("MAGIC METHODS")

print(f"  __repr__ output:")
print(f"    {repr(andrew)}")

print("\n  Testing equality")
andrew_copy = Student("Sire Andrew the Fourth", 19, "BIVT-25-10", 1)

print(f"  Andrew: name='{andrew.student_name}', age={andrew.student_age}, subject='{andrew.course}'")
print(f"  Copy: name='{andrew_copy.student_name}', age={andrew_copy.student_age}, subject='{andrew_copy.course}'")

if andrew == andrew_copy:
    print("equality check passed successfully (same name, age, course)")
else:
    print("equality check failed unexpectedly. man what the hell")

matthew = Student("Matthew", 19, "BIVT-24-13", 2)

if andrew != matthew:
    print("inequality check passed")
else:
    print("inequality check failed unexpectedly")

if matthew != "goober":
    print("type safety check passed")
else:
    print("type safety check failed unexpectedly")



print("WORKFLOW DEMO")

print("  creating a new student!")

david = Student("David Akrimov", 28, "BIVT-21-15", 5)
print(f"created: {david.student_name}")

david.add_sick_leave(date(2023, 1, 5), date(2023, 1, 17))
david.add_sick_leave(date(2023, 9, 16), date(2023, 9, 26))
print(f"added sick leaves: {david.sick_leave_log}")

david.grade(4)
david.grade(4)
david.grade(5)
print(f"received gpa: {david.student_gpa}")

david.update_group = "BIVT-21-16"
print(f"changed to: {david.student_group}")

david.update_age = 29
print(f"Grew older. Now {david.student_age}")

# Take academic leave
david.deactivate()
print(f"On academic leave: active={david.active}")

# Return from academic leave
david.activate()
david.update_group = "BIVT-22-16"
david.add_sick_leave(date(2026, 1, 6), date(2026, 1, 19))
print(f"Returned! New group: {david.student_group}")

print(f"\n  Final state: {repr(david)}")

print("DEMO COMPLETED SUCCESSFULLY")