
### Requisitos mínimos
- [Git](https://git-scm.com/)
- Make (Makefile) ([Ubuntu](https://askubuntu.com/questions/161104/how-do-i-install-make) | [MacOS](https://askubuntu.com/questions/161104/how-do-i-install-make))
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Como rodar?

```sh
make build
```

Após este comando, será necessário entrar no banco de dados que foi criado, (para ver as credenciais de acesso basta acessar o docker-compose.yml) e rodar a seguinte query:

```sh
CREATE SCHEMA IF NOT EXISTS lesson;
CREATE SCHEMA IF NOT EXISTS correction;
```

### Como utilizar a aplicação?

```sh
make how-to-use
```

### Para realizar a correção
```sh
make start
```

Ao final da correção voce deve receber um relatório como este abaixo:

![Relatório final](https://i.ibb.co/hDrfq82/image.png)
