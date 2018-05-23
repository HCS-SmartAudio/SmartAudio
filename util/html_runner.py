import unittest
import HtmlTestRunner
from tests.sanity_test_suite import SanityTestSuite


sanity_suite = unittest.TestLoader().loadTestsFromTestCase(SanityTestSuite)
unittest.TextTestRunner(verbosity=2)
#outfile = open("reports.html", "w")
runner = HtmlTestRunner.HTMLTestRunner("C:\\Users\\ininsako\\PycharmProjects\\SmartAudio\\Reports")
runner.run(sanity_suite)

