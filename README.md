![](https://media.tenor.com/3AV9En0ZpkIAAAAC/tarjeta-de-cr%C3%A9dito-mojo-jojo.gif)

# MaisTodos credit-card-api

API de cadastro e listagem de cartão. A aplicação também contém autenticação.

A aplicação foi desenvolvida em FastAPI e possui documentação Swagger e Redoc

### Bibliotecas usadas no projeto

* FastAPI (Web framework)
* JWT (Para geração de token e controle de autenticação)
* Fernet (Usado para criptografar dados do cartão e senha)
* Pytest
* SQLite
* SQLAlchemy
* Docker

#### TODO Melhorias

- [ ] Testar domínio de `user`
- [ ] Config banco de dados teste
- [ ] Docker-compose
- [x] ~~Melhorar a doc com exemplo de response e request~~
- [ ] Conf de env var

## Instruções de uso dos recursos da API

A API tem esquema de autenticação via JWT.
No docs, você precisará criar um usuário pelo endpoint de Create User, após usuário criado, ir
em authenticate e fazer o login. Feito isso, você conseguirá consumir os endpoints.

## Rodando a aplicação
Para rodar aplicação foi criado um `makefile` que se encontra na raiz do projeto. Para rodar
basta seguir os passos abaixo:

1:

    make build
_o `make build` irá criar a imagem a partir do dockerfile_

2:

    make run
_o `make run` irá criar criar o container e subi-lo_

Após ter rodado a aplicação, você poderá acessar a doc no endereço:

http://0.0.0.0:8000/docs

Para parar a aplicação

    make stop
_o `make stop` irá parar o container e o remover, portanto, caso queira
rodar de novo, será necessário buildar `make build`_

![alt text](https://i.ibb.co/3p9Zp8h/Design-sem-nome-5.png)

## Testes
Fora feito testes de integração cobrindo o domínio de `credit_cards`

Para rodas os testes a aplicação deve estar rodando conforme as instruções acima

Basta rodar:

    make test

## Diagramas
O projeto contém diagramas de sequencia usando o plantuml assim
podendo ser versionado conforme evolução do projeto

![alt text](https://i.ibb.co/S035ScN/Selection-279.png)
