import os
import unittest

from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):
    def test_something(self):
        setUp(self)
        inputA = WebDriverWait(webdriver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
        )
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

    uuid = os.system("adb devices")
    desired_caps = {
        'platformName': 'Android',
        'uuid': uuid,
        'deviceName': 'Samsung Galaxy Note 3',
        'automationName': 'Appium',
        'app': 'eribank.apk',
        'appPackage': 'com.experitest.ExperiBank',
        'appActivity': '.LoginActivity'
    }


    def setUp(self):
        webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


    def shutDown(self):
        webdriver.quit()
