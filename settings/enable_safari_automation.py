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
        dc['deviceName'] = self.udid
        dc['bundleId'] = "com.apple.Preferences"
        dc['platformVersion'] = "11.0"
        dc['automationName'] = "XCUITest"
        dc['noReset'] = True
        dc['adbExecTimeout'] = 200000

        url = str(sys.argv[2])

        self.driver = webdriver.Remote(url, dc)


    def tearDown(self):
        self.driver.quit()

    def test_speed(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("Safari").click()
        self.driver.find_element_by_name("ADVANCED").click()
        switch = self.driver.find_elements_by_class_name("XCUIElementTypeSwitch")
        print(len(switch))
        switch[1].click()
        switch[2].click()
        self.driver.save_screenshot(self.udid+".png")
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleSpeedTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

