#language: pt
Funcionalidade: Registro de Novos Usuários



    Cenário 1: Registrar um novo usuário com dados válidos (HAPPY PATH)
        DADO que estou na tela de registro de Usuários
        QUANDO preencho todos os campos obrigatorios com dados válidos
        E clico no botao Cadastrar
        ENTAO devo ver os dados do novo usuário na tabela de Usuários



    Cenário 2: Validar campos ao tentar cadastrar um novo usuário com informações insuficientes ou incorretas
        DADO que estou na tela de registro de Usuários
        QUANDO tento cadastrar um novo usuário com:
            - Nome inválido
            - Email sem formato correto
            - Senha com menos de 8 caracteres
        ENTAO devo visualizar mensagens de erro indicando os campos não preenchidos ou preenchidos incorretamente



    Cenário 3: Validar campo Nome com apenas o primeiro nome ao acionar o botão Cadastrar
        DADO que estou na tela de registro de Usuários
        QUANDO preencho o campo Nome apenas com o primeiro nome
        e aciono a opção Cadastrar
        ENTAO devo visualizar a mensagem ''Por favor, insira um nome completo.'' para o campo Nome
        e a tabela de usuários não deve ser alterada



    Cenário 4: Validar campos vazios ao tentar regristrar um novo Usuários sem preencher os campos
        DADO que estou na tela de registro de Usuários
        QUANDO clico no botao Cadastrar sem preencher os campos obrigatórios
        OU clico nos campos sem preencher o mínimo obrigatório
        ENTAO devo ver mensagens de erro para cada campo nao preenchido



    Cenário 5: Excluir um usuario da tabela de Usuários
        DADO que estou na tela de registro de usuários e há usuários registrados
        QUANDO clico no botao de Excluir de um usuário especifico
        ENTAO o usuário deve ser removido da tabela de usuários



    Cenário 6: Excluir um elemento específico da tabela de usuários sem interferir nas identificações ou ordens dos outros elementos
        Dado que estou na tela de usuários
        E existem vários elementos na tabela de usuários
        Quando eu ativo a opção Excluir para um elemento específico na tabela de usuários
        Então a linha correspondente ao elemento específico deve ser excluída da tabela
        E a tabela deve ser exibida sem interferir nas identificações ou ordens dos outros elementos



    Cenário Outline: Validar campos ao tentar cadastrar um novo usuário com informações insuficientes ou incorretas
        DADO que estou na tela de registro de Usuários
        QUANDO tento cadastrar um novo usuário com "<Nome>", "<Email>" e "<Senha>"
        ENTAO devo visualizar mensagens de erro indicando os campos não preenchidos ou preenchidos incorretamente
    Exemplos:
        | Nome            | Email                  | Senha    | Formato
        | Chiquitito Bebe | chqiuitint@hotmail.com | 12345678 | correto
        | Maggie Dulce    | fgsjdkkaja@gmail.com   | 87654321 | correto
        | Anshue Mortetor | jejeju2023@outlook.com | 23939432 | correto
        | Chiquiriru      | OundrCover             | 123456   | incorreto



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Casos de teste

    TC #1 : Validar el registro de um novo usuário com dados válidos (HAPPY PATH)
    TC #2 : Validar que os campos ao tentar cadastrar um novo usuário com informações insuficientes ou incorretas
    TC #3 : Validar que o campo Nome com apenas o primeiro nome ao acionar o botão Cadastrar
    TC #4 : Validar que os campos vazios ao tentar regristrar um novo Usuários sem preencher os campos
    TC #5 : Validar a exclusão de um usuario da tabela de Usuários
    TC #6 : Validar a exclusão de um elemento específico da tabela do usuário sem interferir nas identificações ou ordens de outros elementos