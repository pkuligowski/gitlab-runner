"""
Code quality tests based on the Pylint.
For more see https://www.pylint.org

To append new dirs fill the `SOURCE_DIRS` list.
"""
import unittest
import os
from pylint import epylint

PYLINT_CONFIG = '/.pylintrc'
SOURCE_DIRS = ['../tests',
               '../src']


class QualityTest(unittest.TestCase):
    """
    Code quality test cases.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_quality(self):
        """
        Test case for the Pylint called from python.
        """

        config_file_path = '--rcfile=' + os.getcwd() + PYLINT_CONFIG

        pylint_exit_code = 0

        for dir_str in SOURCE_DIRS:
            print("\n=============\nCurrent directory: " + dir_str + '\n')

            pylint_exit_code |= epylint.lint(filename=dir_str,
                                             options=([config_file_path]))

        self.assertEqual(0, pylint_exit_code)

if __name__ == "__main__":
    unittest.main(verbosity=0)
