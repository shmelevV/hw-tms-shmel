from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Вадюша/tms05_onl/vadim_shmelev/test_dir/chromedriver.exe")
        self.driver.get('https://demo.guru99.com/test/newtours/register.php')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_login(self):
        driver = self.driver

        driver.find_element(by=By.NAME, value='firstName').send_keys('vadim')
        driver.find_element(by=By.NAME, value='lastName').send_keys('shmel')
        driver.find_element(by=By.NAME, value='phone').send_keys('+79221110500')
        driver.find_element(by=By.NAME, value='userName').send_keys('mailmail@gmail.com')
        driver.find_element(by=By.NAME, value='address1').send_keys('address')
        driver.find_element(by=By.NAME, value='city').send_keys('City')
        driver.find_element(by=By.NAME, value='state').send_keys('State')
        driver.find_element(by=By.NAME, value='postalCode').send_keys('0000')
        driver.find_element(by=By.NAME, value='email').send_keys('shmel2')
        driver.find_element(by=By.NAME, value='password').send_keys('12345')
        driver.find_element(by=By.NAME, value='confirmPassword').send_keys('12345')
        select = Select(driver.find_element(By.NAME, value='country'))
        select.select_by_value('ZIMBABWE')
        driver.find_element(by=By.NAME, value='submit').click()

        name = driver.find_element(by=By.XPATH,
                                       value="/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b").text
        self.assertEqual(name, f'Dear vadim shmel,')

        user = driver.find_element(by=By.XPATH,
                                           value="/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b").text
        self.assertEqual(user, f'Note: Your user name is shmel2.')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
