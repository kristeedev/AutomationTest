import unittest
from time import sleep
import sys
from appium import webdriver

class SimpleSpeedTest(unittest.TestCase):
    def setUp(self):
        self.udid = sys.argv[1]
        self.app_package = "org.zwanoo.android.speedtest"
        self.app_activity = "com.ookla.mobile4.screens.main.MainActivity"
        dc = {}
        dc['platformName'] = 'Android'
        dc['udid'] = self.udid
        dc['deviceName'] = self.udid
        dc['appPackage'] = self.app_package
        dc['appActivity'] = self.app_activity
        dc['noReset'] = True
        dc['automationName'] = "uiautomator2"
        dc['adbExecTimeout'] = 200000

        url = str(sys.argv[2])

        self.driver = webdriver.Remote(url, dc)


    def tearDown(self):
        self.driver.quit()

    def test_speed(self):
        self.driver.implicitly_wait(300)
        go_button = self.driver.find_element_by_id(self.app_package + ":id/go_button")
        sleep(1)
        go_button.click()

        end_of_test = self.driver.find_element_by_id(self.app_package + ":id/shareIcon")
        
        result_array = self.driver.find_elements_by_id(self.app_package + ":id/txt_test_result_value")

        download_speed = result_array[0].text
        upload_speed = result_array[1].text

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleSpeedTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

