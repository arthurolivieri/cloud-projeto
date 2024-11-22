# Projeto de Computação em Nuvem - AWS

## Feito por: **Arthur Olivieri**

#### A proposta do projeto:
Nessa etapa do projeto, fizemos o deploy em um cluster EKS (Kubernetes) na AWS da nossa aplicação criada e dockerizada na primeira etapa.

#### O meu projeto:
O meu projeto cobre os requisitos da proposta, permitindo cadastrar e autenticar usuários e expondo piadas provenientes de uma [API externa](https://v2.jokeapi.dev/joke/Any?safe-mode).

----

## Links e Informações Rápidas:

1. [Link para o repositório do projeto no github](https://github.com/arthurolivieri/cloud-projeto)

2. [Link para o repositório da imagem no dockerhub](https://hub.docker.com/repository/docker/aolivieri03/cloud-projeto-1/general)

3. [Link para o vídeo de demonstração no youtube](https://youtu.be/CnLoiLQRv14)
4. [Link para o serviço de consultas rodando na AWS](http://a27025c21229a4b2081bf6fb37ad3df1-327827612.us-east-2.elb.amazonaws.com/docs)

5. No repositório github, os arquivos de configuração de deploy (`app-deployment.yaml` e `postgres-deployment.yaml`) encontram-se na pasta `aws-files` e, também, nas abas da documentação.

----

## Executando o serviço:

Como o serviço está hospedado na aws, não é necessária nenhuma configuração para consumi-lo. Basta entrar no link http://a27025c21229a4b2081bf6fb37ad3df1-327827612.us-east-2.elb.amazonaws.com/docs e testar da mesma maneira que fez na primeira etapa do projeto. Na parte a seguir, estão as diretrizes sobre como testar a API (exatamente da mesma maneira da primeira parte do projeto).

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