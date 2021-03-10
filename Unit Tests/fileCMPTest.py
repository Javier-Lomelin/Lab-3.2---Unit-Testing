import unittest
import filecmp


class FileCMPTest(unittest.TestCase):
    def test_content_is_different_shallow(self):
        file1 = "Text Files/file1.txt"
        file2 = "Text Files/file2.txt"

        a = filecmp.cmp(file1, file2)
        self.assertFalse(a)

    def test_content_equal_shallow(self):
        file1 = "Text Files/file1.txt"
        file2 = "Text Files/file1_copy.txt"

        a = filecmp.cmp(file1, file2)
        self.assertTrue(a)
