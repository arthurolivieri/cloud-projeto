# Projeto de Computação em Nuvem

## Feito por: **Arthur Olivieri**

#### A proposta do projeto:
O projeto do semestre consistiu em criar uma API RESTful para cadastrar e autenticar usuários e expor algum conteúdo externo, seja consumindo uma outra API ou fazendo um scraping de alguma página web. Essa API, em conjunto com o banco de dados PostgreSQL deve ser conteinerizado.

#### O meu projeto:
O meu projeto cobre os requisitos da proposta, permitindo cadastrar e autenticar usuários e expondo piadas provenientes de uma [API externa](https://v2.jokeapi.dev/joke/Any?safe-mode).

----

## Links e Informações Rápidas:

1. [Link para o repositório do projeto no github](https://github.com/arthurolivieri/cloud-projeto)

2. [Link para o repositório da imagem no dockerhub](https://hub.docker.com/repository/docker/aolivieri03/cloud-projeto-1/general)

3. [<a href="compose.yaml" download>Link para o download do compose.yaml</a>](#)

4. [Link para o vídeo de demonstração no youtube](https://youtu.be/9XHn0FeS8_Y)

5. No repositório github, o compose.yaml encontra-se na raíz do projeto.

----

## Executando o contêiner:

1. Tenha o docker instalado no seu computador. [Esse tutorial](https://docs.docker.com/desktop/) pode te ajudar caso ainda não tenha baixado.

2. Clique [<a href="compose.yaml" download>aqui</a>](#) para baixar o arquivo compose.yaml. Outra alternativa é clonar o [repositório do projeto](https://github.com/arthurolivieri/cloud-projeto) no github e encontrar o arquivo compose.yaml na raíz do repositório.

3. Em um terminal, entre na pasta em que se encontra o arquivo baixado e execute o comando `docker compose up -d`

4. Se tudo ocorreu bem, você pode consumir a API de acordo com os endpoints abaixo no link [http://localhost:8000]() utilizando um método de sua preferência. Uma sugestão é utilizar a própria documentação do FastAPI no link [http://localhost:8000/docs](), onde é possível testar todos os endpoints.



----

## Testando e utilizando a API:

Para utilizar a API, você deve se registrar como usuário, fazer login, guardar o token obtido no login, e rir da piada exposta utilizando o token no header da requisição de acordo com os endpoints a seguir.

### POST /register

**Payload de request - informações de registro**

    {
    "nome": "seu-nome",
    "email": "seu-email",
    "senha": "sua-senha"
    }

**Payload de resposta - um token de autenticação**

    {
    "jwt": "iOiIxMjM0NTY...",
    }

### POST /login

**Payload de request - informações de login.** Note que nesse momento um registro já deve ter sido feito, ou seja, você deve existir como usuário.

    {
    "email": "seu-email",
    "senha": "sua-senha"
    }

**Payload de resposta - um token de autenticação**

    {
    "jwt": "iOiIxMjM0NTY...",
    }

### GET /consultar

**No header, deve haver o token obtido no login no seguinte formato**

    Authorization: Bearer <JWT>

**Payload de resposta - uma piada no seguinte formato:**

    {
    "setup": "What's the difference between a hot potato and a flying pig?",
    "delivery": "One's a heated yam, the other's a yeeted ham.",
    }