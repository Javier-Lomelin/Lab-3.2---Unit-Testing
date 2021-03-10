import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

loader = unittest.TestLoader()
start = "Unit Tests/"
a = loader.discover(start)

run_tests = unittest.TextTestRunner(verbosity=2)
run_tests.run(a)
