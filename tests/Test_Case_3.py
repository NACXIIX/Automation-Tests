from page_objects.objects import *
from page_objects.fw import *



class TestCase3(unittest.TestCase):
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


    @when('I fill in the name field with only the first name and click on the register option.')
    @then('I should see the message "Por favor, insira um nome completo." for the name field.')
    def test_b_validando_mensajes_error(self):
        
        driver = self.driver
        driver.get(Page_objects.page)
        
        name = driver.find_element(By.NAME, Page_objects.name_input)
        name.send_keys(Users.incorrect_name)
        
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        
        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Page_objects.field_error_name), Page_objects.error_message_name_2))
        finally:
            pass


    @then('the user table should not be altered.')
    def test_c_validando_tabla_sinalterar(self):
        
        driver = self.driver
        driver.get(Page_objects.page)
        
        # Primer usuario
        name1 = driver.find_element(By.NAME, Page_objects.name_input)
        name1.send_keys(Users.name_1)
        email1 = driver.find_element(By.NAME, Page_objects.email_input)
        email1.send_keys(Users.email_1)
        password1 = driver.find_element(By.NAME, Page_objects.password_input)
        password1.send_keys(Users.password_1)
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # Segundo usuario
        name2 = driver.find_element(By.NAME, Page_objects.name_input)
        name2.send_keys(Users.name_2)
        email2 = driver.find_element(By.NAME, Page_objects.email_input)
        email2.send_keys(Users.email_2)
        password2 = driver.find_element(By.NAME, Page_objects.password_input)
        password2.send_keys(Users.password_2)
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #Tercer usuario
        name3 = driver.find_element(By.NAME, Page_objects.name_input)
        name3.send_keys(Users.name_3)
        email3 = driver.find_element(By.NAME, Page_objects.email_input)
        email3.send_keys(Users.email_3)
        password3 = driver.find_element(By.NAME, Page_objects.password_input)
        password3.send_keys(Users.password_3)
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #Acá se ubica la tabla actual
        table = driver.find_element(By. XPATH, Page_objects.table_xpath)
        rows_before = len(table.find_elements(By.TAG_NAME, "tr"))
        
        #Cuarto usuario
        name4 = driver.find_element(By.NAME, Page_objects.name_input)
        name4.send_keys(Users.incorrect_name)
        
        register = driver.find_element(By.ID, Page_objects.register_button)
        register.send_keys(Keys.ENTER)
        
        #Acá se ubica la tabla despues del ingreso de usuario incorrectamente
        rows_after = len(table.find_elements(By.TAG_NAME, "tr"))
        time.sleep(2)
        
        #Se comparan las dos tablas, buscando que no hayan cambiado.
        assert rows_after == rows_before, "La tabla no se modifica después de registrar nombre de usuario incorrectamente"


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())