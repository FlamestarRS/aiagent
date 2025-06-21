# tests.py

import unittest
import fnmatch
from functions.get_files_info import get_files_info


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


if __name__ == "__main__":
    unittest.main()