import psycopg2 as ps # Importing psycopg2 for databases manipulation
from dotenv import load_dotenv # Importing load_dotenv for more security
import os

load_dotenv(dotenv_path='../../.env')

data = {
    'name': os.getenv("DB_NAME"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': os.getenv("DB_PORT")
}

def connect() -> None:
    """
    -> Connect to the database
    :return: None
    """
    try:
        con = ps.connect(
            dbname=data["name"],
            user=data["user"],
            password=data["password"],
            host=data["host"],
            port=data["port"]
        )
    except(Exception, ps.DatabaseError):
        print(f'\033[0;31mERRO: Falha ao tentar conectar ao banco de dados\033[0m')
    else:
        return con

def create_database_if_not_exists() -> None:
    try:
        con = ps.connect(
            dbname="postgres",
            user=data["user"],
            password=data["password"],
            host=data["host"],
            port=data["port"]
        )
        con.autocommit = True
        cursor = con.cursor()
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{data['name']}';")
        exist = cursor.fetchone()
        if not exist:
            cursor.execute(f'CREATE DATABASE {data["name"]}')
            print('\033[0;32mBanco de dados criado!')
        else:
            print('\033[0;32mBanco de dados já existente!\033[0m')
        cursor.close()
        con.close()
    except Exception as e:
        print('\033[0;31mErro: Falha ao criar banco de dados\033[0m', e)

if __name__ == '__main__':
    create_database_if_not_exists()