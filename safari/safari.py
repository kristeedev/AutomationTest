import unittest
from time import sleep
import sys
from appium import webdriver

class SimpleSpeedTest(unittest.TestCase):
    def setUp(self):
        self.udid = sys.argv[1]
        dc = {}
        dc['platformName'] = 'iOS'
        dc['udid'] = self.udid
        dc['deviceName'] = "iPhone 11"
        dc['platformVersion'] = "13.2"
        dc['automationName'] = "XCUITest"
        dc['browserName'] = 'safari'
        dc['autoWebview'] = True
        url = str(sys.argv[2])

        self.driver = webdriver.Remote(url, dc)


    def tearDown(self):
        self.driver.quit()

    def test_speed(self):
        self.driver.get("https://www.lambdatest.com") 
        print(self.driver.find_element_by_tag_name("h1").text)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleSpeedTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

