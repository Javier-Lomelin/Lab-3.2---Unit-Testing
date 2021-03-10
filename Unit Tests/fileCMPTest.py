import unittest
import filecmp


class FileCMPTest(unittest.TestCase):
    def test_content_is_different_shallow(self):
        file1 = "resources/file1.txt"
        file2 = "resources/file2.txt"

        comp = filecmp.cmp(file1, file2)
        self.assertFalse(comp)

    def test_content_equal_shallow(self):
        file1 = "resources/file1.txt"
        file2 = "resources/file1_copy.txt"

        comp = filecmp.cmp(file1, file2)
        self.assertTrue(comp)
