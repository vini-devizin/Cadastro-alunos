import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from lib.database import connect
import bcrypt as bc
from tokens import *

def login(username: str, password: str) -> None:
    """
    -> Make the login
    :param username: User's username to search in the database
    :param password: User's password to verify if user is really the user
    """
    con = connect()
    cursor = con.cursor()
    query = "SELECT id, password, type FROM users WHERE username = %s;"
    cursor.execute(query, (username, ))
    user = cursor.fetchone() # User data
    if user is None:
        print(f'\033[0;31mERRO: Usuário {username} não encontrado!\033[0m')
        return None
    user_id, user_password, user_type = user
    if bc.checkpw(password.encode('utf-8'), user_password.encode('utf-8')): # Checking the password
        token = generate_token(user_id, user_type)
        print('\033[0;32mLogin feito com sucesso!\033[0m')
        return token
    else:
        print('\033[0;31mERRO: Senha incorreta!\033[0m')
        return None
