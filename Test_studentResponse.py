import re, unittest
import requests
from regexValidation import EmailRegexValidation, NamesRegexValidation, GradeRegexValidation

class TestStudentClassResponse(unittest.TestCase):
    url = "https://gist.githubusercontent.com/edotus/bd63eefb9b4b1eacb641811f9a1a780d/raw/60e04520584f7a436917b0d5be2b6c18f039fadb/students_classes.json" 
    json_response = {}
    students = None
    classes_list = None

    def setUp(self):
        print("getting json response")   
        response = requests.get(self.url)
        if response.status_code not in range(200, 300):
            print("error getting json")

        self.json_response = response.json()
        self.students = self.json_response.get("students", [])
        self.classes_list = self.json_response.get("classes", [])

    def test_response_validation(self):
        for idx, student in enumerate(self.students):
            if not student:
                print("no student found")
            print("\nValidating student: " + str(idx))
            print("validating email format")
            self.assertTrue(EmailRegexValidation("email", student.get("email", "")).validate())
            print("validating first name format")
            self.assertTrue(NamesRegexValidation("first", student.get("first", "")).validate())
            print("validating last name format")
            self.assertTrue(NamesRegexValidation("last", student.get("last", "")).validate())
            classes = student.get("studentClasses", [])
            print("validating Classes")
            for student_class in classes:
                print("validating id")
                self.assertIn(str(student_class.get("id", 0)), self.classes_list)
                print("validating grades format")
                self.assertTrue(GradeRegexValidation("grade", str(student_class.get("grade", 0))).validate())

    def tearDown(self):
        print ("Ending session")

if __name__ == '__main__':
    unittest.main()
