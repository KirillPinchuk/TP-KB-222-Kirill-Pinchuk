import unittest
import io
from unittest.mock import patch
from lab_02 import load_data, save_data, addNewElement, deleteElement, updateElement, printAllList

class TestLab02(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_lab2.csv"
        self.test_data = [
            {"name": "Bob", "phone": "0631234567", "age": "22", "grade": "83"},
            {"name": "Emma", "phone": "0631234567", "age": "16", "grade": "65"},
        ]

    def test_load_data(self):
        with open(self.test_file, "w") as file:
            file.write("name,phone,age,grade\nBob,0631234567,22,83\nEmma,0631234567,16,65")

        data = load_data(self.test_file)
        self.assertEqual(data, [
            {"name": "Bob", "phone": "0631234567", "age": "22", "grade": "83"},
            {"name": "Emma", "phone": "0631234567", "age": "16", "grade": "65"},
        ])

    def test_save_data(self):
        save_data(self.test_file, self.test_data)
        loaded_data = load_data(self.test_file)
        self.assertEqual(loaded_data, self.test_data)

    def test_addNewElement(self):
        with patch('builtins.input', side_effect=["Jon", "0631234567", "19", "87"]):
            addNewElement(self.test_data)
            self.assertEqual(len(self.test_data), 3)

    def test_deleteElement(self):
        with patch('builtins.input', return_value="Emma"):
            deleteElement(self.test_data)
            self.assertEqual(len(self.test_data), 1)

    def test_updateElement(self):
        with patch('builtins.input', side_effect=["Bob", "Jon", "5555555555", "30", "35"]):
            updateElement(self.test_data)
            self.assertEqual(self.test_data[1]["name"], "Jon")

    def test_printAllList(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(self.test_data)
            output = mock_stdout.getvalue()
            self.assertIn("Bob", output)
            self.assertIn("Emma", output)

if __name__ == '__main__':
    unittest.main()