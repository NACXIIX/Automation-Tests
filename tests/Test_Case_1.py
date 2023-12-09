from page_objects.fw import *
from page_objects.objects import *



class TestCase1(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome.chrome_driver()


    @Given('i am on the user registration screen.')
    def test_a_pantalla_registro(self):
        driver = self.driver
        driver.get(Page_objects.page)
        time.sleep(1)
        
        try:
            WebDriverWait(driver, 10).until(EC.title_contains(Page_objects.page_title))
            assert Page_objects.page_title == driver.title
        finally:
            pass


    @when('I complete all the required fields with valid information and click on the "Register" button.')
    @then('I should be able to see the details of the new user in the Users table.')
    def test_b_validacion_usuario_registrado_aparece_en_tabla(self):
        driver = self.driver
        driver.get(Page_objects.page)
        
        name1 = driver.find_element(By.NAME, Page_objects.name_input)
        name1.send_keys(Users.name_1)
        email1 = driver.find_element(By.NAME, Page_objects.email_input)
        email1.send_keys(Users.email_1)
        password1 = driver.find_element(By.NAME, Page_objects.password_input)
        password1.send_keys(Users.password_1)
        try:
            register = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, Page_objects.register_button)))
            register.send_keys(Keys.ENTER)
        finally:
            pass

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.table_xpath), Users.name_1))
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.table_xpath), Users.email_1))


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())