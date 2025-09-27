# 🍊 Laranjinha de Mel

## O que é o Laranjinha de Mel?

O Laranjinha de Mel é a minha primeira tentativa de criar um blog/rede social para testar minhas habilidades e lógica de programação em Python e Flask.

## O que já temos?

No momento já criei a página home, da qual é encarregada de exibir todos os posts já feitos, além dela ter um botão que nos possibilitar criar novos posts.

Tambem criei páginas para registro de novos usuarios e login, tudo isso linkado ao um banco de dados [sqlite3](https://docs.python.org/3/library/sqlite3.html), utilizei a ORM [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) e [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/) para facilitação do gerenciamento das querys.

## Coisas das quais desejo adicionar

Pretendo adicionar uma página de recuperação de senha, da qual dispara uma mensagem para o email solicitado, caso esse email esteja armazenado no bando de dados.

Também tenho o desejo de deixar o perfil do usuario mais personalizado com coisas como bio e foto de perfil.

## Rotas

#### `/`
#### metodos: `GET`

Essa é a página principal do site, ela tem como papel principal exibir os posts junto da sua data de criação. Ela também é o unico local do qual nos possibilita criar novos posts através de um botão.

#### `/register`
#### metodos: `GET e POST`

Essa página se encarrega de registrar novos usuários ao banco de dado, caso tudo ocorra bem o usuário é automáticamente logado, graças a biblioteca [flask-login](https://flask-login.readthedocs.io/en/latest/).

#### `/login`
#### metodos: `GET e POST`

Essa página se encarrega de logar os usuários casos já tenha anteriormente se registrado em nosso site.

A vantagem de se registrar e se logar, está na capacidade de acessar certas páginas que só podem ser acessadas caso o usuário esteja logado, tais como a página para fazer os posts e a de logout.

#### `/rec_password`
#### metodos: `GET`

Essa página ainda está em construção, ela basicamente serve para que usuários que já tem conta no site, recuperarem sua senha ou alterar elas, tudo isso com a autenticação de email. Basicamente sera disparado um email para a pessoa que solicitou a recuperação/troca de senha, mas isso só funciona caso o email solicitado esteja em nosso banco de dados.

#### `/logout (login necessário)`
#### metodos: `GET`

Essa é uma simples página para deslogar o usuário até o próximo login, ela não afeta o banco de dados.

#### `/send-post (login necessário)`
#### metodos: `GET e POST`

Essa é segunda página principal do site, ela basicamente se encarrega de criar e enviar novos posts ao site.

## Dependências do projeto

###### [Flask](https://flask.palletsprojects.com/en/stable/)

###### [sqlite3](https://docs.python.org/3/library/sqlite3.html)

###### [dotenv](https://pypi.org/project/python-dotenv/)

###### [flask-login](https://flask-login.readthedocs.io/en/latest/)

###### [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

###### [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/)

###### [datetime](https://docs.python.org/3/library/datetime.html)