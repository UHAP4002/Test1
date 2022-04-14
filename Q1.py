
from unittest import TestCase, main


class TestStudents(TestCase):
    def test_api(self):
        import students
        self.assertTrue(hasattr(students, "Students"))
        self.assertTrue(hasattr(students.Students, "add"))
        self.assertTrue(hasattr(students.Students, "list"))

    def test_simple_case(self):
        from students import Students
        s = Students()
        s.add("Ali", "11")
        self.assertEqual(s.list(), [("Ali", "11")])
        s.add("Reza", "12")
        c = False
        b = False
        for name, _id in s.list():
            if _id == "11":
                self.assertEqual(name, "Ali")
                c = True
            elif _id == "12":
                b = True
                self.assertEqual(name, "Reza")
            else:
                raise ValueError("Data Didn't Match :|")
        if not (c and b):
            raise ValueError("Data Didn't Match :|")


if __name__ == '__main__':
    main()