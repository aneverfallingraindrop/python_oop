from model import Student
from datetime import date

class StudentValidation:
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
    
    def assert_raises(self, func, exception_type, description):
        try:
            func()
            print(f"  FAIL: {description} - Expected {exception_type.__name__} but no exception raised")
            self.failed += 1
            return False
        except exception_type:
            print(f"  PASS: {description}")
            self.passed += 1
            return True
        except Exception as exc:
            print(f"  FAIL: {description} - Expected {exception_type.__name__} but got {type(exc).__name__}: {exc}")
            self.failed += 1
            return False
    
    def assert_equals(self, actual, expected, description):
        if actual == expected:
            print(f"  PASS: {description}")
            self.passed += 1
            return True
        else:
            print(f"  FAIL: {description} - Expected {expected}, got {actual}")
            self.failed += 1
            return False
    
    def run_all_tests(self):
        print("STUDENT VALIDATION")
        
        self.test_constructor()
        self.test_grades()
        self.test_sick_leave()
        self.test_activity()
        self.test_infomanager()
        self.test_magic()
        
        print(f"{self.passed} passed, {self.failed} failed")
        return self.failed == 0
    
    def test_constructor(self):
        print("\nTesting Constructor")
        
        # Valid creation
        try:
            s = Student("Somebody Somewhere", 18, "BIVT-25-8", 1)
            print(f"Valid student creation")
            self.passed += 1
        except Exception as e:
            print(f"Valid student creation failed: {e}")
            self.failed += 1
        
        # Invalid name
        self.assert_raises(
            lambda: Student("", 18, "BIVT-25-8", 1),
            ValueError, "Empty name raises ValueError"
        )
        self.assert_raises(
            lambda: Student(62245, 18, "BIVT-25-8", 1), #type: ignore
            ValueError, "Non-string name raises ValueError"
        )
        
        # Invalid age
        self.assert_raises(
            lambda: Student("Somebody Somewhere", 4, "BIVT-25-8", 1), # THERES NO WAY A 4YO GETS INTO UNIVERSITY PLEASE
            ValueError, "Age < 6 raises ValueError"
        )
        self.assert_raises(
            lambda: Student("Somebody Somewhere", 105, "BIVT-25-8", 1),
            ValueError, "Age > 100 raises ValueError"
        )
        self.assert_raises(
            lambda: Student("Somebody Somewhere", "18", "BIVT-25-8", 1), #type: ignore
            ValueError, "Non-int age raises ValueError"
        )
        
        # Invalid group
        self.assert_raises(
            lambda: Student("Somebody Somewhere", 18, "", 1),
            ValueError, "Empty group raises ValueError"
        )
        
        # Invalid course
        self.assert_raises(
            lambda: Student("Somebody Somewhere", 18, "BIVT-25-8", 0),
            ValueError, "Course below 1 raises ValueError"
        )
        self.assert_raises(
            lambda: Student("Somebody Somewhere", 18, "BIVT-25-8", 7),
            ValueError, "Course above 6 raises ValueError"
        )
    
    def test_grades(self):
        print("\n Testing GPA and Grades")
        
        stud = Student("Somebody Somewhere", 18, "BIVT-25-8", 1)
        
        # Valid GPA
        stud.grade(5)
        self.assert_equals(stud.student_gpa, 5.0, "First rating of 5 gives score 5.0")
        
        stud.grade(3)
        self.assert_equals(stud.student_gpa, 4.0, "Average of 5.0 and 3.0 is 4.0")
        
        stud.grade(4)
        self.assert_equals(stud.student_gpa, 4.0, "Average of three ratings is correct")
        
        # Invalid GPA
        self.assert_raises(lambda: stud.grade(6), ValueError, "Rating > 5 raises ValueError")
        self.assert_raises(lambda: stud.grade(1), ValueError, "Rating < 2 raises ValueError")
        self.assert_raises(lambda: stud.grade("5"), ValueError, "String grade raises ValueError") #type: ignore
        self.assert_raises(lambda: stud.grade(4.0), ValueError, "Float grade raises ValueError") #type: ignore
        
        # Grading inactive student
        stud.deactivate()
        self.assert_raises(lambda: stud.grade(4), AttributeError, "Rating inactive student raises AttributeError")
    
    def test_sick_leave(self):
        print("\n Testing Sick Leave System")
        
        s = Student("Somebody Somewhere", 18, "BIVT-25-8", 1)
        
        s.add_sick_leave(date(2025, 5, 5), date(2025, 5, 12))
        self.assert_equals([date(2025, 5, 5), date(2025, 5, 12)] in s.student_sick_leave_log, True, "Sick leave added successfully")
        
        s.add_sick_leave(date(2025, 6, 5), date(2025, 6, 12))
        self.assert_equals(len(s.student_sick_leave_log), 2, "Two sick leaves added")
        
        self.assert_raises(
            lambda: s.add_sick_leave(1, date(1, 1, 1)), #type: ignore
            ValueError, "Non-date Start causes ValueError"
        )

        self.assert_raises(
            lambda: s.add_sick_leave(date(1, 1, 1), 1), #type: ignore
            ValueError, "Non-date End causes ValueError"
        )

        self.assert_raises(
            lambda: s.add_sick_leave(date(2, 1, 1), date(1, 1, 1)),
            ValueError, "Start after End causes ValueError"
        )

        self.assert_raises(
            lambda: s.add_sick_leave(date(2, 1, 1), date(1, 1, 1)),
            ValueError, "Start after End causes ValueError"
        )
        
        # Assign to inactive student
        s2 = Student("bum", 18, "BIVT-25-8", 1)
        s2.deactivate()
        self.assert_raises(
            lambda: s2.add_sick_leave(date(1, 1, 1), date(2, 1, 1)),
            AttributeError, "Assigning to inactive teacher raises AttributeError"
        )
        
    def test_activity(self):
        print("\n Testing Activity Manager")
        
        s = Student("Somebody Somewhere", 18, "BIVT-25-8", 1)
        self.assert_equals(s.active, True, "Student starts as active")
        
        # Group disappears after being deactivated
        s.deactivate()
        self.assert_equals(s.student_group, '', "Group removed successfully")
        
        # Reactivate
        s.activate()
        self.assert_equals(s.active, True, "Student reactivated successfully")
    
    def test_infomanager(self):
        print("\n Testing Information Manager")
        
        s = Student("old name", 18, "BIVT-25-8", 1)
        
        # Update name
        s.update_name("New Name")
        self.assert_equals(s.student_name, "New Name", "Name updated successfully")
        self.assert_raises(
            lambda: s.update_name(""),
            ValueError, "Empty name update raises ValueError"
        )
        
        # Update age
        s.update_age(19)
        self.assert_equals(s.student_age, 19, "Age updated successfully")
        self.assert_raises(
            lambda: s.update_age(5),
            ValueError, "Invalid age update raises ValueError"
        )
        
        # Update group
        s.update_group("new group")
        self.assert_equals(s.student_group, "new group", "Group updated successfully")

        self.assert_raises(
            lambda: s.update_group(""),
            ValueError, "Empty group update causes value error"
        )
        
        # Cannot update rank when inactive
        s.deactivate()
        self.assert_raises(
            lambda: s.update_group("hero!"),
            AttributeError, "Cannot update group when inactive"
        )
    
    def test_magic(self):
        print("\n Testing Magic")
        
        s1 = Student("Somebody Somewhere", 18, "BIVT-25-8", 1)
        s2 = Student("Somebody Somewhere", 18, "BIVT-25-8", 1)
        s3 = Student("Somebody Somewhere", 18, "BIVT-25-8", 2)      # Different Course
        s4 = Student("Somebody Nowhere", 18, "BIVT-25-8", 1)      # Different name
        s5 = Student("Somebody Somewhere", 28, "BIVT-25-8", 1)      # Different age
        
        self.assert_equals(s1 == s2, True, "Same students are equal")
        self.assert_equals(s1 == s3, False, "Different courses are not equal")
        self.assert_equals(s1 == s4, False, "Different names are not equal")
        self.assert_equals(s1 == s5, False, "Different ages are not equal")
        self.assert_equals(s1 == "goku", False, "Comparison with non-Student is False")
        
        # Test __repr__
        repr_str = repr(s1)
        self.assert_equals("Student" in repr_str, True, "__repr__ contains class name")
        self.assert_equals("Somebody Somewhere" in repr_str, True, "__repr__ contains name")

        # Test __str__
        str_str = str(s1)
        self.assert_equals("18" in str_str, True, "__repr__ contains age")
        self.assert_equals("Somebody Somewhere" in str_str, True, "__repr__ contains name")


if __name__ == "__main__":
    validator = StudentValidation()
    success = validator.run_all_tests()
    exit(0 if success else 1)