# Cadastro de alunos v1

Após muito código, estudo e sofriemnto, finalmente acabei a 1° versão do cadastro de alunos

## Pré-requisitos

- Python e pip instalados(Para instalar use: `sudo apt install python3 python3-pip`)
- Postgresql(Para instalar use: `sudo apt install python3 python3-pip`)

## Passo a passo para executar o projeto

1. Escolha um diretório para clonar o projeto com: `cd caminho/para/o/seu/diretório`
2. Clone o repositório com: `git clone https://github.com/vini-devizin/Cadastro-alunos.git`
3. Instale as dependências com: `pip install -r requirements.txt`

- Caso aconteça igual aconteceu comigo, não conseguiu instalar as dependências, tente com um ambiente virtual(venv):

``` bash
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

4. Crie um usuário postgres com:

``` bash
sudo -i -u postgres
psql
CREATE USER seu_usuario WITH
PASSWORD 'sua_senha'
SUPERUSER
CREATEDB
CREATEROLE
REPLICATION
BYPASSRLS;
```

5. Crie um arquivo .env com:

``` .env
DB_NAME=nome_do_seu_banco
DB_USER=seu_usuario_postgres
DB_PASSWORD=sua_senha
DB_HOST=seu_host
DB_PORT=sua_porta
```

6. Rode o projeto com: `python3 main.py`
