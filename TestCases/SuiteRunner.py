import unittest
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

smokeTestSuite = unittest.TestSuite([testCase1, testCase4])
regressionTestSuite = unittest.TestSuite([testCase1, testCase2, testCase5])
functionalTestSuite = unittest.TestSuite([testCase1, testCase2, testCase3, testCase4, testCase5])
integrationTestSuite = unittest.TestSuite([testCase4, testCase5])

cu = commonUtils()
config = cu.readProperties("C:\\Users\\USER\\PycharmProjects\\MarchDemoFramework\\commonUtils\\config.properties")
suiteName = config["suiteName"]

if suiteName == "SMOKE":
    print("Runing SMOKE Test Suite")
    unittest.TextTestRunner().run(smokeTestSuite)
elif suiteName == "REGRESSION":
    print("Runing REGRESSION Test Suite")
    unittest.TextTestRunner().run(regressionTestSuite)
elif suiteName == "FUNCTIONAL":
    print("Runing FUNCTIONAL Test Suite")
    unittest.TextTestRunner().run(functionalTestSuite)
elif suiteName == "INTEGRATION":
    print("Runing INTEGRATION Test Suite")
    unittest.TextTestRunner().run(integrationTestSuite)