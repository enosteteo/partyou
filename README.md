# partyou

[![Build Status](https://travis-ci.org/enosteteo/partyou.svg?branch=master)](https://travis-ci.org/enosteteo/partyou)
[![codecov](https://codecov.io/gh/enosteteo/partyou/branch/master/graph/badge.svg)](https://codecov.io/gh/enosteteo/partyou)
[![Updates](https://pyup.io/repos/github/enosteteo/partyou/shield.svg)](https://pyup.io/repos/github/enosteteo/partyou/)
[![Python 3](https://pyup.io/repos/github/enosteteo/partyou/python-3-shield.svg)](https://pyup.io/repos/github/enosteteo/partyou/)

Aplicação criada no Python 3.8

---
# Levantar e conferir a aplicação:
Para fazer a configuração básica:

```console
   pip install pipenv
   pipenv sync -d
   cp contrib/env-sample .env
```
* Obs, no arquivo env-sample, insira sua SECRET_KEY
* Obs, Caso prefira utilizar o SQLite, remova a var DATABASE_URL do arquivo env-sample.

Para criar o banco de dados Postgres*

 *Caso prefira utilizar o SQLite, sugere-se que este passo seja ignorado
```console
    psql -c "CREATE DATABASE testdb;" -U postgres
```

Para instalar as dependências necessárias*:

*Obs, caso em ambiente de produção, remova o `-d`, pois o mesmo é utilizado para instalar as dependências de desenvolvimento
```console
    pipenv sync -d
```

Para conferir a qualidade de código:

```console
   pipenv run flake8 .
```

Para executar os testes e conferir a cobertura de código:

```console
    pipenv run pytest --cov=ccprod
```

Em ambiente CI, utilizar comando abaixo após a conclusão dos testes, para enviar o relatório para o codecov

```console
    pipenv run codecov
```

Levantar aplicação:
```console
    pipenv runserver
``` 

---
