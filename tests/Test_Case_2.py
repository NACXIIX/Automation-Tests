from page_objects.objects import *
from page_objects.fw import *



class TestCase2(unittest.TestCase):
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


    @when('I try to register a new user with insufficient or incorrect information.')    
    def test_b_informacion_incorrecta(self):
        
        driver = self.driver
        driver.get(Page_objects.page)
        
        name = driver.find_element(By.NAME, Page_objects.name_input) 
        name.send_keys(Users.incorrect_name)
        
        email = driver.find_element(By.NAME, Page_objects.email_input)
        email.send_keys(Users.incorrect_email)
        
        contraseña = driver.find_element(By.NAME, Page_objects.password_input)
        contraseña.send_keys(Users.incorrect_password)
        
        try:
            register = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, Page_objects.register_button)))
            register.send_keys(Keys.ENTER)
        finally:
            pass


    @then('I should see error messages indicating the fields not filled or filled incorrectly.')
    def test_c_mensaje_error(self):
        
        driver = self.driver
        driver.get(Page_objects.page)
        
        name = driver.find_element(By.NAME, Page_objects.name_input) 
        name.send_keys(Users.incorrect_name)
        
        email = driver.find_element(By.NAME, Page_objects.email_input)
        email.send_keys(Users.incorrect_email)
        
        contraseña = driver.find_element(By.NAME, Page_objects.password_input)
        contraseña.send_keys(Users.incorrect_password)
        
        try:
            register = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, Page_objects.register_button)))
            register.send_keys(Keys.ENTER)
        finally:
            pass
        
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.field_error_name), Page_objects.error_message_name_2))
        finally:
            pass
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.field_error_email), Page_objects.error_message_email_2))
        finally:
            pass
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.field_error_password), Page_objects.error_message_password_2))
        finally:
            pass


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())