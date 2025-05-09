import psycopg2 as ps # Importing psycopg2 for databases manipulation
from psycopg2 import sql # Importing module sql from psycopg2 to protect from sql injection
from dotenv import load_dotenv # Importing library load_dotenv for more security
import os # Importing library os to acess the .env
from datetime import date # importing date from datetime to register the birth of the student
from tabulate import tabulate # importing tabulate to write the table

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
            query = f"""
            CREATE DATABASE {data['name']} 
            WITH ENCODING 'UTF8'
            LC_COLLATE 'pt_BR.UTF-8'
            LC_CTYPE 'pt_BR.UTF-8'
            TEMPLATE template0
            """
            cursor.execute(f'CREATE DATABASE {data["name"]}')
            print('\033[0;32mBanco de dados criado!\033[0m')
        else:
            print('\033[0;32mBanco de dados já existente!\033[0m')
    except:
        print('\033[0;31mErro: Falha ao criar banco de dados\033[0m')
    finally:
        cursor.close()
        con.close()

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
        sexo CHAR(1) CHECK (sexo IN ('M', 'F')),
        nascimento DATE NOT NULL,
        cpf VARCHAR(11) NOT NULL UNIQUE,
        email varchar(100) NOT NULL UNIQUE,
        ensino VARCHAR(13) NOT NULL,
        serie SMALLINT NOT NULL,
        adicionado DATE DEFAULT CURRENT_DATE
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

def add_student(name: str, sex: str, birth: date, cpf: str, email: str, edu: str, grade: str, table: str) -> None:
    """
    -> add a student to the table
    :param name: Student's name
    :param birth: Student's birth date
    :param cpf: Student's cpf
    :param edu: Student's education
    :param grade: Student's grade
    :param table: The table that will be added this data
    :return: None
    """
    try:
        con = connect()
        cursor = con.cursor()
        query = sql.SQL("INSERT INTO {} (nome, sexo, nascimento, cpf, email, ensino, serie) VALUES (%s, %s, %s, %s, %s, %s, %s);").format(sql.Identifier(table))
        cursor.execute(query, (name, sex, birth, cpf, email, edu, grade))
        con.commit()
    except Exception as e:
        print('\033[0;31mERRO: Falha ao cadastrar aluno!\033[0m', e)
    else:
        print(f'\033[0;32mAluno {name} cadastrado com sucesso\033[0m')
    finally:
        cursor.close()
        con.close()

def remove_student(id: int, table: str) -> None:
    """
    -> remove a student using the id
    :param id: Id of student that will be removed
    :param table: The table that the student is registered
    """
    try:
        con = connect()
        cursor = con.cursor()
        query = sql.SQL("DELETE from {} WHERE id = %s;").format(sql.Identifier(table))
        cursor.execute(query, (id, ))
        con.commit()
    except:
        print('\033[0;31mERRO: Falha ao remover aluno!\033[0m')
    else:
        print(f'\033[0;32mAluno com id {id} removido com sucesso!\033[0m')
    finally:
        cursor.close()
        con.close()

def update_student(id: int, value, column: str, table: str) -> None:
    """
    -> Update a student data
    :param id: Student's id
    :param value: The new value
    :param column: Column that will be the value changed
    :param table: The table that the student is registered
    """
    try:
        con = connect()
        cursor = con.cursor()
        query = sql.SQL("""
        UPDATE {}
        SET {} = %s 
        WHERE id = %s;
    """).format(sql.Identifier(table), sql.Identifier(column))
        cursor.execute(query, (value, id))
        con.commit()
    except Exception as e:
        print(f'\033[0;31mERRO: Falha ao atualizar aluno com id {id}!\033[0m', e)
    else:
        print(f'\033[0;32mDados do aluno com id {id} atualizados com sucesso!\033[0m')
    finally:
        cursor.close()
        con.close()

def show_students(table: str) -> None:
    """
    -> Show the students registered in the table
    :param table: Table that will show the registers
    """
    try:
        con = connect()
        cursor = con.cursor()
        query = sql.SQL("SELECT * FROM {};").format(sql.Identifier(table))
        cursor.execute(query)
        data = cursor.fetchall()
        colunms = [desc[0] for desc in cursor.description]
        print(tabulate(data, headers=colunms, tablefmt="psql"))
    except:
        print('\033[0;31mERRO: Falha ao exibir alunos cadastrados!\033[0m')
    finally:
        cursor.close()
        con.close()

def search_student(id: int, table: str) -> None:
    """
    -> Search student by id
    :param id: Student's id
    :table: Table that will be searched the student
    """
    try:
        con = connect()
        cursor = con.cursor()
        query = sql.SQL("SELECT * FROM {} WHERE id = %s;").format(sql.Identifier(table))
        cursor.execute(query, (id, ))
        data = cursor.fetchall()
        colunms = [desc[0] for desc in cursor.description]
        print(tabulate(data, headers=colunms, tablefmt="psql"))
    except:
        print(f'\033[0;31mERRO: Falha ao buscar aluno com id {id}!\033[0m')
    finally:
        cursor.close()
        con.close()

def greater_id(table: str) -> None:
    con = connect()
    cursor = con.cursor()
    query = sql.SQL("SELECT MAX(id) FROM {};").format(sql.Identifier(table))
    cursor.execute(query)
    greater_id = cursor.fetchone()[0]
    if greater_id is None:
        greater_id = 0
    return greater_id
