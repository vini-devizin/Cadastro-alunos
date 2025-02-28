import psycopg2 as ps # Importing psycopg2 for databases manipulation
from dotenv import load_dotenv # Importing library load_dotenv for more security
import os # Importing library os for acess the .env

load_dotenv(dotenv_path='../../.env') # Load the .env in his directory

data = { # The credentials of database 
    'name': os.getenv("DB_NAME"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': os.getenv("DB_PORT")
}

def connect():
    """
    -> Connect to the database
    :return: The connection with the database
    """
    load_dotenv()
    try:
        con = ps.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
    except(Exception, ps.DatabaseError):
        print(f'\033[0;31mERRO: Falha ao tentar conectar ao banco de dados\033[0m')
    else:
        return con

def create_database_if_not_exists() -> None:
    try:
        con = ps.connect( # Connect to postgres database
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
    except:
        print('\033[0;31mErro: Falha ao criar banco de dados\033[0m')

if __name__ == '__main__':
    create_database_if_not_exists() # I used this to debug, but i will remove this
