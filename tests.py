# tests.py

import unittest
import fnmatch
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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


if __name__ == "__main__":
    unittest.main()