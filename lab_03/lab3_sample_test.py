import unittest
from Student import Student
from StudentList import StudentList
from Utils import Utils
from unittest import mock

class Testlab03(unittest.TestCase):

    def test_load_data(self):
        test_file = "test03.csv"
        with open(test_file, "w") as file:
            file.write("name,phone,age,grade\nLiza,12323232,33,98")
        student_list = Utils.load_data(test_file)
        self.assertEqual(len(student_list.students), 1)

    @mock.patch("builtins.input", side_effect=["Liza", "12323232", "33", "98"])
    def test_save_data(self, mock_input):
        test_file = "test_file.csv"
        student_list = StudentList()
        student_list.add_student(Student("Liza", "12323232", "33", "98"))
        Utils.save_data(test_file, student_list)
        with open(test_file, "r") as file:
            content = file.read()
            self.assertIn("Liza", content)

class TestStudentListMethods(unittest.TestCase):

    @mock.patch("builtins.input", side_effect=["Liza", "12323232", "33", "98"])
    def test_addNewElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        self.assertEqual(len(student_list.students), 1)
        self.assertEqual(student_list.students[0].name, "Liza")

    @mock.patch("builtins.input", return_value="Liza")
    def test_deleteElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        student_list.deleteElement()
        self.assertEqual(len(student_list.students), 0)

    @mock.patch("builtins.input", side_effect=["Liza", "Bob", "662622", "22", "88"])
    def test_updateElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        student_list.updateElement()
        self.assertEqual(student_list.students[0].name, "Bob")

if __name__ == '__main__':
    unittest.main()