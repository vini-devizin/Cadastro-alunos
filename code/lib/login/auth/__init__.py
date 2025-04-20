import bcrypt as bc
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.database import connect

def register_new_user(username: str, password: str, type: str):
    """
    -> Register a new user in the table 'users'
    :param username: User's username
    :param password: User's password
    :param type: User's type
    """
    try:
        con = connect()
        cursor = con.cursor()
        crypted_password = bc.hashpw(password.encode('utf-8'), bc.gensalt()).decode('utf-8')
        query = "INSERT INTO users (username, password, type) VALUES (%s, %s, %s) RETURNING id;"
        cursor.execute(query, (username, crypted_password, type))
        user_id = cursor.fetchone()[0]
    except:
        print(f'\033[0;31mERRO: Falha ao registrar novo usuário {username}!\033[0m')
    else:
        print(f'\033[0;32mUsuário {username} cadastrado com sucesso!\033[0m')
    finally:
        cursor.close()
        con.close()
        return user_id

if __name__ == '__main__':
    register_new_user('vinizera da quebrada', '11022013Vini!', 'student')