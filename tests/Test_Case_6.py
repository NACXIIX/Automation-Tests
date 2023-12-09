from page_objects.objects import *
from page_objects.fw import *



class TestCase5(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome.chrome_driver()


    @Given('I am on the user screen nd there are several elements in the users table.')
    @when('I click on the Delete button for a specific user.')
    @then('the queue corresponding to the element in question must be removed from the table and the table must be displayed without interfering with the identifications or orders of other elements. ')
    def test_a_validacion_tabla_sin_cambios_en_id_elements_al_eliminar_usuario(self):
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
        
        tabla = driver.find_element(By.XPATH, Page_objects.table_xpath)
        rows = tabla.find_elements(By.TAG_NAME, "tr")
        after_deletion = [row.find_elements(By.TAG_NAME, "td")[0].text for row in rows[1:]]
        assert after_deletion == sorted(after_deletion)



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())