import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestShop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Вадюша/tms05_onl/vadim_shmelev/test_dir/chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_passwd(self):
        driver = self.driver

        driver.find_element(by=By.NAME, value='email').send_keys('smelev88@gmail.com')
        driver.find_element(by=By.NAME, value="passwd").send_keys('12345')
        driver.find_element(by=By.NAME, value="SubmitLogin").click()

        now_url = driver.current_url
        self.assertEqual(now_url, "http://automationpractice.com/index.php?controller=my-account")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
