import unittest
import os
import HtmlTestRunner
from tests.sanity_test_suite import SanityTestSuite

current_folder_path = os.path.split(os.getcwd())
sanity_suite = unittest.TestLoader().loadTestsFromTestCase(SanityTestSuite)
unittest.TextTestRunner(verbosity=2)
#outfile = open("reports.html", "w")
runner = HtmlTestRunner.HTMLTestRunner(current_folder_path[0] + "\\Reports")
runner.run(sanity_suite)

