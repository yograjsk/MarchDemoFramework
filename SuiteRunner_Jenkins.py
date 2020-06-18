import os
import unittest

import HtmlTestRunner

from TestCases.TC01_AddUser import TC01_AddUser
from TestCases.TC02_DeleteUser import TC02_DeleteUser
from TestCases.TC03_HandleSimpleAlerts import TC03_HandleSimpleAlerts
from TestCases.TC04_UploadFile import TC04_UploadFile
from TestCases.TC05_DownloadFile import TC05_DownloadFile
from commonUtils.commonUtilities import commonUtils

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
config = cu.readProperties("commonUtils/config.properties")
suiteName = config["suiteName"]

# below runner is the alternate way of suite execution with report
# test_runner = HtmlTestRunner.HTMLTestRunner(output="../Reports/NewHTMLReports", verbosity=1)

if suiteName == "SMOKE":
    print("Runing SMOKE Test Suite")
    # test_runner.run(smokeTestSuite)               #this is the alternate way of suite execution with report
    # unittest.TextTestRunner().run(smokeTestSuite) #this runner will run the tests but it wil lnot generate the report
elif suiteName == "REGRESSION":
    print("Runing REGRESSION Test Suite")
    # test_runner.run(regressionTestSuite)
    # unittest.TextTestRunner().run(regressionTestSuite)
elif suiteName == "FUNCTIONAL":
    print("Runing FUNCTIONAL Test Suite")
    # test_runner.run(functionalTestSuite)
    # unittest.TextTestRunner().run(functionalTestSuite)
elif suiteName == "INTEGRATION":
    print("Runing INTEGRATION Test Suite")
    # test_runner.run(integrationTestSuite)
    # unittest.TextTestRunner().run(integrationTestSuite)

unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports/HTMLReports"))



