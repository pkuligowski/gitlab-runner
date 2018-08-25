"""
Coding style tests according to the PEP8 standard.
For more information see https://www.python.org/dev/peps/pep-0008/

To append new dirs fill the `SOURCE_DIRS` list.
"""
import unittest
import pep8

QUIET_RUN = True
SOURCE_DIRS = ['../tests',
               '../src']


class StyleTest(unittest.TestCase):
    """
    Coding style test cases.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_style(self):
        """
        Test case for PEP8 coding style checker.
        """
        checker = pep8.StyleGuide(quiet=QUIET_RUN)
        report = checker.init_report()

        errors_counter = 0

        for dir_str in SOURCE_DIRS:
            checker.input_dir(dir_str)

        for msg_key in report.messages.keys():
            errors_counter += report.counters[msg_key]

        self.assertEqual(0, errors_counter)

if __name__ == "__main__":
    QUIET_RUN = False
    unittest.main(verbosity=0)
