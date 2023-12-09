from page_objects.objects import *
from page_objects.fw import *



class TestCase4(unittest.TestCase):
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


    @when('I click on the register button without filling in the required fields.')
    def test_b_click_boton_registro(self):
        
        driver = self.driver
        driver.get(Page_objects.page)
        time.sleep(1)
        
        try:
            register = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Page_objects.register_button)))
            register.send_keys(Keys.ENTER)
        finally:
            pass
            


    @then('I should see an error message for each field that is not completed.')    
    def test_c_mensaje_error(self):
        
        driver = self.driver
        driver.get(Page_objects.page)
        time.sleep (1)
        
        register = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Page_objects.register_button)))
        register.send_keys(Keys.ENTER)
        
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.field_error_name), Page_objects.error_message_name_1))
        finally:
            pass
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.field_error_email), Page_objects.error_message_email_1))
        finally:
            pass
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.field_error_password), Page_objects.error_message_password_1))
        finally:
            pass


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())