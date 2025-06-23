# tests.py

import unittest
import fnmatch
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class TestGetFilesInfo(unittest.TestCase):
    def test_current_directory(self):
        result = get_files_info("calculator", ".")
        pattern = "- *: file_size=* bytes, is_dir=True*"
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_inside_directory(self):
        result = get_files_info("calculator", "pkg")
        pattern = "- *: file_size=* bytes, is_dir=True*"
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_not_directory(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')
    def test_outside_directory(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')


class TestGetFileContent(unittest.TestCase):
    def test_main(self):
        result = get_file_content("calculator", "main.py")
        pattern = "# main.py*"
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_subdirectory(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        pattern = "# calculator.py*"
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_no_access(self):
        result = get_file_content("calculator", "/bin/cat")
        pattern = "Error: Cannot read * as it is outside the permitted working directory"
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_lorem(self):
        result = get_file_content("calculator", "lorem.txt")
        pattern = "* truncated at 10000 characters]"
        self.assertTrue(fnmatch.fnmatch(result, pattern))


class TestWriteFile(unittest.TestCase):
    def test_write_file(self):
        result = write_file("calculator", "lorem2.txt", "wait, this isn't lorem ipsum")
        pattern = "Successfully wrote to * characters written)"
        #print(result)
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_write_subdirectory_file(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        pattern = "Successfully wrote to * characters written)"
        #print(result)
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_no_write_access(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        pattern = "Error: Cannot write to * as it is outside the permitted working directory"
        #print(result)
        self.assertTrue(fnmatch.fnmatch(result, pattern))


class TestRunPythonFile(unittest.TestCase):
    def test_run_main(self):
        result = run_python_file("calculator", "main.py")
        pattern = "*STDOUT*"
        #print(result)
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_run_tests(self):
        result = run_python_file("calculator", "tests.py")
        pattern = "*OK*"
        #print(result)
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_run_outside_dir(self):
        result = run_python_file("calculator", "../main.py")
        pattern = 'Error: Cannot execute * as it is outside the permitted working directory'
        #print(result)
        self.assertTrue(fnmatch.fnmatch(result, pattern))
    def test_nonexistent(self):
        result = run_python_file("calculator", "nonexistent.py")
        pattern = 'Error: File * not found.'
        #print(result)
        self.assertTrue(fnmatch.fnmatch(result, pattern))

if __name__ == "__main__":
    unittest.main()