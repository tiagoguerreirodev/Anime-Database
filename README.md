# Anime-Database <!-- omit in toc -->

- [*Todos os animes em um só lugar*](#todos-os-animes-em-um-só-lugar)
- [Instalação](#instalação)
- [Execução](#execução)
  - [Opção 1 (recomendada): Docker Compose](#opção-1-recomendada-docker-compose)
  - [Opção 2: Manualmente](#opção-2-manualmente)
## *Todos os animes em um só lugar*

Essa aplicação acessa a API GraphQL do [Anilist](https://anilist.co/), disponível [nesse link](https://anilist.gitbook.io/anilist-apiv2-docs/). Com ela, é possível buscar animes no banco de dados do Anilist e salvá-los localmente, em um banco de dados [MongoDB](https://www.mongodb.com/). A AnimeAPI é composta de diversos métodos para deletar, incluir e buscar os animes salvos pelo usuário. Neste momento, uma aplicação frontend está sendo desenvolvida para interagir com essa API.

## Instalação

AnimeAPI é uma aplicação desenvolvida em [Python](https://www.python.org/). Caso ainda não o tenha instalado, pode fazê-lo através [deste link](https://www.python.org/downloads/). Também será necessário possuir o [Git](https://git-scm.com/) instalado no computador.

Primeiramente, é necessário clonar a aplicação:

    $ git clone https://github.com/tiagoguerreirodev/Anime-Database.git

Com a aplicação em seu computador, há duas formas de executá-la.

## Execução

### Opção 1 (recomendada): Docker Compose
 
[Docker](https://www.docker.com/) é uma ferramenta que facilita a criação de ambientes isolados. O Docker Compose é uma ferramenta inclusa no Docker para facilitar a execução de vários containers ao mesmo tempo, como é o caso da Anime-Database.

Para executar o projeto, navegue até a pasta raiz, na qual se encontra o arquivo **docker-compose.yml**, e execute o seguinte comando:

    $ docker compose up -d

Obs: verifique se o serviço do Docker está ativo no computador.

Após essa etapa, se nenhum erro tiver ocorrido na subida dos containers, o projeto já está pronto para ser utilizado. Como o frontend ainda está em desenvolvimento, é possível testar a aplicação através da documentação criada automaticamente pelo [FastAPI](https://fastapi.tiangolo.com/), através do link http://localhost:5000/docs.

### Opção 2: Manualmente

Também é possível executar o projeto da forma mais clássica, subindo localmente os serviços necessários. Para tal, também é necessário ter o [MongoDB](https://www.mongodb.com/) instalado localmente, além do [Python](https://www.python.org/). Certifique-se que o serviço do MongoDB esteja sendo executado e, na pasta raiz do projeto, execute os seguintes comandos:

    $ cd AnimeAPI
    $ python3 main.py

Após essa etapa, o projeto está pronto para ser utilizado. Como o frontend ainda está em desenvolvimento, é possível testar a aplicação através da documentação criada automaticamente pelo [FastAPI](https://fastapi.tiangolo.com/), através do link http://localhost:5000/docs.