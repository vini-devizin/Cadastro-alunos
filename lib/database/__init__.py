import psycopg2 as ps # Importing psycopg2 for databases manipulation
from psycopg2 import sql # Importing module sql from psycopg2 to protect from sql injection
from dotenv import load_dotenv # Importing library load_dotenv for more security
import os # Importing library os to acess the .env
from datetime import date # importing date from datetime to register the birth of the student
import re # Importing re to verify names of tables

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

def create_database() -> None:
    """
    -> Create database if not exists.
    :return: None
    """
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
            print('\033[0;32mBanco de dados criado!\033[0m')
        else:
            print('\033[0;32mBanco de dados já existente!\033[0m')
    except:
        print('\033[0;31mErro: Falha ao criar banco de dados\033[0m')
    finally:
        cursor.close()
        con.close()

def verify_table(table: str) -> bool:
    """
    -> Verify if the name of table isn't a try of sql injection
    :param table: The name that be verified in this function
    :return: If the name of table is secure
    """
    if re.match(r'^[A-Za-z0-9_]+$', table):
        return True
    return False

def create_table(name: str) -> None:
    """
    -> Create table if not exists
    :param name: name of the table
    :return: None
    """
    try:
        con = connect()
        cursor = con.cursor()
        query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        nasc DATE NOT NULL,
        cpf VARCHAR(11) NOT NULL UNIQUE
        ); 
""").format(sql.Identifier(name)) # I'm using sql.Identifier to protect from sql injection
        cursor.execute(query)
        con.commit()
        
        print(f'\033[0;32mTabela criada com sucesso!\033[0m')
    except:
        print(f'\033[0;31mERRO: Falha ao criar tabela\033[0m')
    finally:
        cursor.close()
        con.close()

def add_student(name: str, birth: date, cpf: str, table: str) -> None:
    """
    -> add a student to the table
    :param name: Student's name
    :param birth: Student's birth date
    :param cpf: Student's cpf
    :param table: The table that will be added this data
    :return: None
    """
    try:
        con = connect()
        cursor = con.cursor()
        query = f"INSERT INTO {table} (nome, nasc, cpf) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, birth, cpf))
        con.commit()
    except:
        print('\033[0;31mERRO: Falha ao cadastrar aluno!\033[0m')
    else:
        print(f'\033[0;32mAluno {name} cadastrado com sucesso\033[0m')
    finally:
        cursor.close()
        con.close()

# if __name__ == '__main__':
    # create_table('test1') # I'm using this to debug, but i will remove this