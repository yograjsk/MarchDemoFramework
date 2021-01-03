import os
import unittest

import HtmlTestRunner
import xmlrunner as xmlrunner

from TestCases.TC01_AddUser import TC01_AddUser
from TestCases.TC02_DeleteUser import TC02_DeleteUser
from TestCases.TC03_HandleSimpleAlerts import TC03_HandleSimpleAlerts
from TestCases.TC04_UploadFile import TC04_UploadFile
from TestCases.TC05_DownloadFile import TC05_DownloadFile
from commonUtils.commonUtilities import commonUtils
from concurrencytest import ConcurrentTestSuite, fork_for_tests

testCase1 = unittest.TestLoader().loadTestsFromTestCase(TC01_AddUser)
testCase2 = unittest.TestLoader().loadTestsFromTestCase(TC02_DeleteUser)
testCase3 = unittest.TestLoader().loadTestsFromTestCase(TC03_HandleSimpleAlerts)
testCase4 = unittest.TestLoader().loadTestsFromTestCase(TC04_UploadFile)
testCase5 = unittest.TestLoader().loadTestsFromTestCase(TC05_DownloadFile)

# Create Test Suites
smokeTestSuite = unittest.TestSuite([testCase1, testCase4])
regressionTestSuite = unittest.TestSuite([testCase1, testCase2, testCase5])
functionalTestSuite = unittest.TestSuite([testCase1, testCase2, testCase3, testCase4, testCase5])
integrationTestSuite = unittest.TestSuite([testCase4, testCase5])

cu = commonUtils()
config = cu.readProperties("C:\\Users\\USER\\PycharmProjects\\MarchDemoFramework\\commonUtils\\config.properties")
suiteName = config["suiteName"]
parallelRun = config["parallelRun"]

# Open report file
# outputFile = open(os.getcwd()+"\\Reports\\SuiteReports\\SuiteReport.html", "w")
# runner = HtmlTestRunner

test_runner = HtmlTestRunner.HTMLTestRunner(output="../Reports/NewHTMLReports",
                                            verbosity=2,
                                            report_title=suiteName+" TEST REPORT",
                                            combine_reports=True)

# Parallel runs:
runner = unittest.TextTestRunner()

# test_runner = HtmlTestRunner.HTMLTestRunner(stream=outputFile, report_title=suiteName+" TEST REPORT")
if suiteName == "SMOKE":
    print("Runing SMOKE Test Suite")
    parallelRun = ConcurrentTestSuite(smokeTestSuite, fork_for_tests(5))
    serialRun = smokeTestSuite
    # test_runner.run(smokeTestSuite)
    # unittest.TextTestRunner().run(smokeTestSuite)
elif suiteName == "REGRESSION":
    print("Runing REGRESSION Test Suite")
    parallelRun = ConcurrentTestSuite(regressionTestSuite, fork_for_tests(5))
    serialRun = regressionTestSuite
    # test_runner.run(regressionTestSuite)
    # unittest.TextTestRunner().run(regressionTestSuite)
elif suiteName == "FUNCTIONAL":
    print("Runing FUNCTIONAL Test Suite")
    parallelRun = ConcurrentTestSuite(functionalTestSuite, fork_for_tests(5))
    serialRun = functionalTestSuite
    # test_runner.run(functionalTestSuite)
    # unittest.TextTestRunner().run(functionalTestSuite)
elif suiteName == "INTEGRATION":
    print("Runing INTEGRATION Test Suite")
    parallelRun = ConcurrentTestSuite(integrationTestSuite, fork_for_tests(5))
    serialRun = integrationTestSuite
    # test_runner.run(integrationTestSuite)
    # unittest.TextTestRunner().run(integrationTestSuite)

# runner.run(parallelRun)
test_runner.run(serialRun)

# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/HTMLReports"))
# unittest.main(testRunner=xmlrunner.XMLTestRunner(output="../Reports/XMLReports"))


