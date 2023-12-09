from page_objects.objects import *
from page_objects.fw import *



class TestCase5(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome.chrome_driver()


    @Given('I am on the user registration screen and there are registered users.')
    @when('I click on the Delete button for a specific user.')
    @then('the user should be removed from the users table.')
    def test_a_validacion_user_removed(self):
        driver = self.driver
        driver.get(Page_objects.page)
        time.sleep(1)
        
        try:
            WebDriverWait(driver, 10).until(EC.title_contains(Page_objects.page_title))
            assert Page_objects.page_title == driver.title
        finally:
            pass
        
        # Primer usuario
        name1 = driver.find_element(By.NAME, Page_objects.name_input)
        name1.send_keys(Users.name_1)
        email1 = driver.find_element(By.NAME, Page_objects.email_input)
        email1.send_keys(Users.email_1)
        password1 = driver.find_element(By.NAME, Page_objects.password_input)
        password1.send_keys(Users.password_1)
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        
        # Segundo usuario
        name2 = driver.find_element(By.NAME, Page_objects.name_input)
        name2.send_keys(Users.name_2)
        email2 = driver.find_element(By.NAME, Page_objects.email_input)
        email2.send_keys(Users.email_2)
        password2 = driver.find_element(By.NAME, Page_objects.password_input)
        password2.send_keys(Users.password_2)
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        time.sleep(2)
        
        # Tercer usuario
        name3 = driver.find_element(By.NAME, Page_objects.name_input)
        name3.send_keys(Users.name_3)
        email3 = driver.find_element(By.NAME, Page_objects.email_input)
        email3.send_keys(Users.email_3)
        password3 = driver.find_element(By.NAME, Page_objects.password_input)
        password3.send_keys(Users.password_3)
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        time.sleep(2)
        
        delete_2 = driver.find_element(By. ID, Page_objects.remove_2)
        delete_2.click()
        time.sleep(2)
        
        


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())