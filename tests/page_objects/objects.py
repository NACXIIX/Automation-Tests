class Page_objects():
    
    page = "https://cadastro-de-usuarios.s3.us-east-1.amazonaws.com/index.html"
    page_title = "Cadastro de usuários"
    table_name = "Usuários cadastrados"
    name_input = "name" #NAME
    email_input = "email" #NAME
    password_input = "password" #NAME
    register_button = "register" #ID
    field_error_name = "//*[@id='root']/div/div/div[2]/form/div[1]/p" # XPATH
    field_error_email = "//*[@id='root']/div/div/div[2]/form/div[2]/p" # XPATH
    field_error_password = "//*[@id='root']/div/div/div[2]/form/div[3]/p" # XPATH
    remove_1 = "removeUser1" # ID
    remove_2 = "removeUser2" # ID
    remove_3 = "removeUser3" # ID
    table_xpath = "//*[@id='root']/div/div/div[2]" #XPATH
    error_message_name_1 = "O campo Nome é obrigatório."
    error_message_email_1 = "O campo E-mail é obrigatório."
    error_message_password_1 = "O campo Senha é obrigatório."
    error_message_name_2 = "Por favor, insira um nome completo."
    error_message_email_2 = "Por favor, insira um e-mail válido."
    error_message_password_2 = "A senha deve conter ao menos 8 caracteres."



class Users():

        # Este es un usuario que no cumple los requerimientos de login, fue hecho para que aparezcan mensajes de error.
        incorrect_name = "Chiquiriru"
        incorrect_email = "OundrCover"
        incorrect_password = 123456

        #Usuario 1
        name_1 = "Chiquitito Bebe"
        password_1 = 12345678
        email_1 = "chqiuitint@hotmail.com"

        #Usuario 2
        name_2 = "Maggie Dulce"
        email_2 = "fgsjdkkaja@gmail.com"
        password_2 = 87654321

        #Usuario 3
        name_3= "Anshue Mortetor"
        email_3 = "jejeju2023@outlook.com"
        password_3 = 23939432


